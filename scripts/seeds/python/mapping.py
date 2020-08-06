PROJECT_VARS = {
    'DIST',
    'VEL',
    'TMBOP',
    'PDA',
    'PFPP',
    'PTPF',
    'PFB',
    'PFB_A',
    'TPF',
    'I',
    'CBAR',
}

PHASE_VARS = {
    'BASE': 'bottom_coring',
    'CBA': 'barrel_size',
    'CC': 'cement_length',
    'EXT_LOT': 'ext_lot',
    'PFF': 'depth',
    'PIF': 'initial_depth',
    'PLH': 'liner_hanger_depth',
    'Q': 'equivalent_flow',
    'TA': 'ream_rate',
    'TC': 'cement_drilling_rate',
    'TDC': 'cable_descend_rate',
    'TDR': 'coating_descend',
    'TJT': 'jet_rate',
    'TMT': 'core_maneuvering_rate',
    'TMPR': 'coated_maneuvering_rate',
    'TMPA': 'open_maneuvering_rate',
    'TOPO': 'top_coring',
    'TPERF': 'logging_time_on_open_well',
    'TRF': 'coating_descend',
    'TT': 'core_rate',
}
AUX_PHASE_SUFFIX = '_A'  # Auxiliar/anterior
NEXT_PHASE_SUFFIX = '_P'  # Posterior


AUTOSHEAR_LBSR = 'LBSR'
AUTOSHEAR_UBSR = 'UBSR'
AUTOSHEAR_DISARMED = 'DISARMED'
AUTOSHEAR_CHOICES = [
    (AUTOSHEAR_LBSR, 'ARM LBSR'),
    (AUTOSHEAR_UBSR, 'ARM UBSR'),
    (AUTOSHEAR_DISARMED, 'DISARM'),
]
