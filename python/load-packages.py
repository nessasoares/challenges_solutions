# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json
import re
from mapping import PROJECT_VARS, PHASE_VARS, AUX_PHASE_SUFFIX, NEXT_PHASE_SUFFIX

def read_csv():
    dataframe = pd.read_excel('pacotes.xlsx')

    packages = []
    x_phase_packages = dataframe[dataframe.fase_code == 'X'] 
    counter = 0
    last_key = ''

    batch = []
    for index, row in x_phase_packages.iterrows():
        code = row.codigo_pacote
        if isinstance(code, unicode):
            packages.extend(duplicate_packages(batch))
            batch = []

        batch.append(row)

    packages.extend(duplicate_packages(batch))

    return packages


def duplicate_packages(batch):

    result = []
    phases = [3,4,5,6,7,8,9]

    for phase in phases:
        new_batch = []
        for pkg in batch:
            pkg_copy = pkg.copy()
            pkg_copy.codigo_atividade = '{}_{}'.format(pkg.codigo_atividade, phase)
            pkg_copy.fase = 'FASE {}'.format(phase)
            pkg_copy.fase_code = '{}'.format(phase)

            if not isinstance(pkg_copy.codigo_pacote, float):
                pkg_copy.codigo_pacote = '{}-fase-{}'.format(pkg.codigo_pacote, phase)
            else:
                pkg_copy.codigo_pacote = ''

            if not isinstance(pkg_copy.labels_seeds, float):
                pkg_copy.labels_seeds = '{}-fase-{}'.format(pkg.codigo_pacote, phase)
            else:
                pkg_copy.labels_seeds = ''
            new_batch.append(pkg_copy)
        
        result.extend(new_batch)

    return result        



def duplicate_packages_to_phases():
    '''
    Metodo criado para duplicar todos os pacotes que são da fase X para as fases 3 a 9
    '''

    pkgs = read_csv()

    to_excel(pkgs)


def text(txt):
    if isinstance(txt, float):
        txt = '{:g}'.format(txt)  # ignora trailing 0
    elif isinstance(txt, int):
        txt = unicode(txt)  # NOQA

    txt = txt.replace('\n', '').replace('\t', ' ')
    txt = unicode(txt).strip()  # NOQA

    return txt


def get_phase_const(type, phase):
    name = 'phase{}_{}'.format(int(phase), type)
    return '{'+ name + '}'
   

def replace_values(txt, fase):
    txt = text(txt)

    txt = re.sub(r'DIAMETRO REVESTIMENTO FASE 4', '{phase4_case_diameter}', txt)
    txt = re.sub(r'DIAMETRO REVESTIMENTO FASE 3', '{phase3_case_diameter}', txt)
    txt = re.sub(r'DIAMETRO REVESTIMENTO FASE 2', '{phase2_case_diameter}', txt)
    txt = re.sub(r'DIAMETRO (REVESTIMENTO|REVEST) FASE 1', '{phase1_case_diameter}', txt)
    txt = re.sub(r'DIAMETRO FASE 4', '{phase4_diameter}', txt)
    txt = re.sub(r'DIAMETRO FASE 3', '{phase3_diameter}', txt)
    txt = re.sub(r'DIAMETRO FASE 2', '{phase2_diameter}', txt)
    txt = re.sub(r'DIAMETRO FASE 1', '{phase1_diameter}', txt)
        
    txt = re.sub('\(PROF\. Broca \(i\) m\)', '{bit_depth} m', txt)
    



    # OBS: TOPO = phase_top_coring

    ## NEXT PHASE
    if fase != '--':
        if fase < 9:
            const = get_phase_const('diameter', fase+1)
            txt = re.sub(r'DIAMETRO FASE (X|x)(\s*)\+(\s*)1', const, txt)

            const = get_phase_const('case_diameter', fase+1)
            txt = re.sub(r'DIAMETRO (REV|REVESTIMENTO) FASE X(\s*)\+(\s*)1', const + ' pol', txt)

            const = get_phase_const('TOPO', fase+1)
            txt = re.sub('\sTOPO FASE X(\s*)\+(\s*)1', const, txt)

        #FASE X
        const = get_phase_const('case_diameter', fase)
        txt = re.sub(r'DIAMETRO (REV|REVESTIMENTO) FASE (X|\d)', const + ' pol', txt)

        const = get_phase_const('diameter', fase)
        txt = re.sub(r'DIAMETRO FASE (X|\d)', const, txt)

        const = get_phase_const('depth', fase)
        txt = re.sub('\(PROF\. FASE X m\)', const +' m', txt)

        const = get_phase_const('TOPO', fase)
        txt = re.sub('\sTOPO FASE X', const, txt)

        cba = get_phase_const('CBA', fase)
        txt = re.sub('\(CBA m\)', cba+' m', txt)

        cbar = get_phase_const('CBAR', fase)
        txt = re.sub('\(CBA_2 m\)', cbar+' m', txt)

        ext = get_phase_const('EXT_LOT', fase)
        txt = re.sub('\sEXT_LOT m\s', ext+' m', txt)

        corrida_testemunhagem = get_phase_const('#i', fase)
        txt = re.sub('#i', '#' + corrida_testemunhagem, txt)

        #CURRENT FASE
        const = get_phase_const('TOPO', fase)
        txt = re.sub('\sTOPO\s', const, txt)
        txt = re.sub('\(TOPO m\)', const + ' m', txt)
        
        #FASE ANTERIOR
        const = get_phase_const('TOPO', fase)
        txt = re.sub('\sTOPO FASE X(\s*)\-(\s*)1', const, txt)


    for var in PHASE_VARS.keys():
        # Fase anterior/auxiliar
        aux_phase_var = '{}{}'.format(var, AUX_PHASE_SUFFIX)
        replacement_txt = '{%s}' % aux_phase_var
        txt = re.sub('\s{}\(i-1\)\s'.format(var), replacement_txt, txt)

        # Fase posterior
        next_phase_var = '{}{}'.format(var, NEXT_PHASE_SUFFIX)
        replacement_txt = '{%s}' % next_phase_var
        txt = re.sub('\s{}\(i+1\)\s'.format(var), replacement_txt, txt)

        # Fase atual
        replacement_txt = '{%s}' % var
        txt = re.sub('\s{}\(i\)'.format(var), replacement_txt, txt)
        txt = re.sub('\s{}\s'.format(var), replacement_txt, txt)

    for var in PROJECT_VARS:
        # Fase atual
        replacement_txt = '{%s}' % var
        txt = re.sub('\s{}\(i\)'.format(var), replacement_txt, txt)
        txt = re.sub('\s{}\s'.format(var), replacement_txt, txt)

    if txt.lower() == u'próximo resumo':
        txt = 'PRÓXIMA ATIVIDADE'

    # matem convenção de openoffice / csv original
    if '"' in txt:
        txt = '"%s"' % txt.replace('"', '""')

    return txt

def add_expressions_to_packages_desc():
    dataframe = pd.read_excel('pacotes.xlsx')

    packages = []
   
    batch = []
    print('INIT READING...')
    for index, row in dataframe.iterrows():
        line = row.copy()
        for index_k, value in enumerate(row):
            if isinstance(value, unicode):
                line[index_k] = replace_values(value, row['Fase.1'])

        if index % 300 == 0:
            print('-'*50)
            print("Linha {}".format(index))
            print('-'*50)
            print(line)
        packages.append(line)


    return packages


def to_excel(data, filename='output'):
    df1 = pd.DataFrame(data)

    df1.to_excel("{}.xlsx".format(filename),
                sheet_name='opa')  



pkgs = add_expressions_to_packages_desc()
to_excel(pkgs, filename='output_2')
print(pkgs)