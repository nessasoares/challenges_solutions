# coding=utf-8
import json 


def create_all_operations(entities, operation='add'):
    '''
    Método criado para unificar a criação de todas as operações, a partir das entidades mapeadas em entities

    Parameters:
        entities: dict com todos os atributos que devem ser criados e seus atributos
        operation: operação do django-facts a ser executada (add/retract)

    Returns:
        operations: lista de tuplas com todas as operações criadas a partir das entidades listadas em entities

    As entidades a serem criadas precisam estar em um dict, com seus respectivos atributos mapeados.
    Por exemplo, sendo a entrada esse dict abaixo:
        entities = {
            "maneuver_conditioning_after_profiling_options/not_conditioning": {
                "phases": [
                    "three", "four"
                ],
                "attribute_name": "maneuver_conditioning_after_profiling_options/item/3",
                "name": "maneuver_conditioning_after_profiling_options/not_conditioning",
                "label": "Não condicionar poço após perfilagem"
            },
            "enlargement_tax": {
                "phases": [
                    "one"
                ],
                "name": "enlargement_tax",
                "valueType": "number",
                "label": "Taxa de alargamento",
                "number/unit": "m/h",
                "cardinality": "one"
            },
        }

    Gera essa saída:
    [
        ('add', 'drilling/phase_four/maneuver_conditioning_after_profiling_options/item/3', 'name', 'drilling/phase_four/maneuver_conditioning_after_profiling_options/not_conditioning'),
        ('add', 'drilling/phase_four/maneuver_conditioning_after_profiling_options/item/3', 'label', 'N\xc3\xa3o condicionar po\xc3\xa7o ap\xc3\xb3s perfilagem'),
        ('add', 'drilling/phase_three/maneuver_conditioning_after_profiling_options/item/3', 'name', 'drilling/phase_three/maneuver_conditioning_after_profiling_options/not_conditioning'),
        ('add', 'drilling/phase_three/maneuver_conditioning_after_profiling_options/item/3', 'label', 'N\xc3\xa3o condicionar po\xc3\xa7o ap\xc3\xb3s perfilagem'),
        ('add', 'attribute/-3', 'cardinality', 'one')
        ('add', 'attribute/-3', 'name', 'drilling/phase_one/enlargement_tax')
        ('add', 'attribute/-3', 'valueType', 'number')
        ('add', 'attribute/-3', 'number/unit', 'm/h')
        ('add', 'attribute/-3', 'label', 'Taxa de alargamento')
    ]

    Foram adicionados 2 novos atributos que devem ser utilizados de acordo com o tipo de entidade que deverá
    ser criada: phases e attribute_name.

    Phases: caso essa entidade seja referente à fases do projeto.

         Vide o exemplo abaixo:
            {
                "enlargement_tax": {
                    "phases": [
                        "three",
                        "four",
                        "five",
                        "six",
                        "seven",
                        "eight",
                        "nine"
                    ],
                    "name": "enlargement_tax",
                    "valueType": "number",
                    "label": "Taxa de alargamento",
                    "number/unit": "m/h",
                    "cardinality": "one"
                }
            }

    Attribute_name: criado para referenciar entidades que são usadas como opções.
        Por exemplo:
                ('add', 'drilling/phase_one/coating/item/33', 'name', 'drilling/phase_one/coating/coating'),
                ('add', 'drilling/phase_one/coating/item/33', 'label', 'Revestimento')

        'drilling/phase_one/coating/item/33' é o attribute_name.
        Então, o mapeamento dos atributos é:
            "coating/coating": {
                "phases": [
                    "one"
                ],
                "attribute_name": "drilling/phase_one/coating/item/33",
                "name": "coating/coating",
                "label": "Revestimento"
            },

        Caso contrário, o atributo é gerado de forma genérica, como 'attribute/-1', por exemplo.



    '''
    count_id = 1
    operations = []

    # Create normal attributes
    for entity_name, entity_object in entities.iteritems():

        # Caso a entidade seja referente ao projeto
        # e não se repita para as fases
        has_phases = entity_object.get('phases') is not None
        generic_attribute_name = 'attribute/-{}'.format(count_id)

        # Define o id do atributo
        entity_id = entity_object.get('attribute_name', generic_attribute_name)

        # Caso a entidade não tenha fases
        if not has_phases:
            operations.extend(
                create_entity(entity_id, entity_object, operation)
            )
            count_id += 1

        # Caso a entidade tenha fases
        else:
            operations.extend(
                create_phase_entities(entity_id, entity_object, count_id, operation)
            )
            count_id += len(entity_object['phases'])

    return operations


def create_entity(entity_id, attributes, operation):
    '''
    Cria fatos para entidades de acordo com os atributos presentes em attributes
    :param entity_id: nome do atributo (com id negativo, para ser criado)
    :param attributes: atributos da entidade a ser criada
    :param operation: operação do django-facts a ser executada
    '''
    transactions = []
    ignored_attributes = ['phases', 'attribute_name']

    for attr_name, attr_value in attributes.items():
        if attr_name not in ignored_attributes:
            transactions.append((operation, entity_id, attr_name, attr_value))

    return transactions


def create_phase_entities(entity_id, entity, count_id, operation):
    '''
        Cria fatos para entidades relacionadas às fases dos projetos de perfuração
        :param entity: atributos da entidade a ser criada
        :param count_id: contagem do id negativo que deve ser atribuído ao nome do atributo
            para que seja criado
        :param operation: operação do django-facts a ser executada
    '''
    phases = list(set(entity['phases']))
    transactions = []

    # Gera uma entidade para cada fase
    for phase in phases:
        entity_object = entity.copy()

        # Monta o nome juntamente com o prefixo indicativo da fase
        entity_object['name'] = build_phase_attribute_name(phase, entity['name'])

        # Faz a mesma composição dos nomes do atributo para os valores de enum/values
        if 'enum/values' in entity_object.keys():
            entity_object['enum/values'] = [
                build_phase_attribute_name(phase, value)
                for value in entity_object['enum/values']
            ]

        # Verifica se o atributo tem um nome específico ou podemos definir o genérico
        if 'attribute' not in entity_id:
            entity_attribute_id = build_phase_attribute_name(phase, entity_id)
        else:
            entity_attribute_id = 'attribute/-{}'.format(str(count_id))

        transactions.extend(
            create_entity(
                entity_attribute_id,
                entity_object,
                operation
            )
        )
        count_id += 1

    return transactions


def build_phase_attribute_name(phase, entity_name):
    '''
    Facilita a criação dos nomes das entidades, levando em conta as diversas fases

    :param phase: fase em que o atributo deve ser criado
    :param entity_name: nome da entidade
    '''

    return 'drilling/phase_{}/{}'.format(phase, entity_name)


ATTRIBUTE_ID_COUNT = 1

attributes = {
    "maneuver_conditioning_after_profiling_options/not_conditioning": {
        "phases": [
            "three", "four"
        ],
        "attribute_name": "maneuver_conditioning_after_profiling_options/item/3",
        "name": "maneuver_conditioning_after_profiling_options/not_conditioning",
        "label": "Não condicionar poço após perfilagem"
    },
    "enlargement_tax": {
        "phases": [
            "one"
        ],
        "name": "enlargement_tax",
        "valueType": "number",
        "label": "Taxa de alargamento",
        "number/unit": "m/h",
        "cardinality": "one"
    },
}

transactions = create_all_operations(attributes)

for i in transactions:
    print(i)

with open('facts.txt', 'w') as f:
    json.dump(transactions, f, ensure_ascii=False, indent=4)