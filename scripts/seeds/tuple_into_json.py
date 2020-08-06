# -*- coding: utf-8 -*-
import json
from operations import OPS

def tuple_into_json(tuples_list):
    '''
        Passa as tuplas para um formato de json, incluindo quais as fases que os mesmos possues
        {
            "phases": [
            "one"
            ], 
            "name": "jetting_tax", 
            "valueType": "number", 
            "label": "Taxa de Jateamento", 
            "number/unit": "m/h", 
            "cardinality": "one"
        }
    '''
    attributes = {}
    attribute_id = '4'
    name = ''
    object = {}
    phase = None

    for fact in tuples_list:
        op, current_attribute_id, attr_name, attr_value = fact
        if current_attribute_id != attribute_id:
            attribute_id = current_attribute_id

            if name not in attributes.keys():
                attributes[name] = object
            
            if 'phases' not in attributes[name].keys():
                attributes[name]['phases'] = []

            if phase:
                attributes[name]['phases'].append(phase)

            phase = None
            object = {}

        if attr_name == 'name':
            if 'phase_' in attr_value:
                splitted = attr_value.split('/')
                attr_value = '/'.join(splitted[2:])

                for string in splitted:
                    if 'phase_' in string:
                        phase = string.split('_')[1]

            name = attr_value


        if 'attribute/' not in current_attribute_id:
            if 'phase' in current_attribute_id:
                attribute_name = current_attribute_id.split('/')[2:]
                object['attribute_name'] = '/'.join(attribute_name)
            else:
                object['attribute_name'] = current_attribute_id

        # Remove as labels de fase caso o valor do atributo seja uma lista
        if  isinstance(attr_value, list):
            values_list = []
            for v in attr_value:
                if 'phase' in v:
                    values_list.append('/'.join(v.split('/')[2:]))
            if values_list:
                attr_value = values_list

        object[attr_name] = attr_value


    return attributes
        


# == MAIN
obj = tuple_into_json(OPS)
OPERATIONS = []

with open('data.txt', 'w') as f:
    json.dump(obj, f, ensure_ascii=False, indent=4)