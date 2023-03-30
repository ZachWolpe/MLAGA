# --------------------------------------------------------------------------------
# ================================================================================
# File: stage_04
# 
# Object:  
#       - Translate text (En-to-Fr)
#
# --------------------------------------------------------------------------------
# author:   Zach Wolpe
# email:    zach.wolpe@medibio.com.au
# date:     21.04.23
# --------------------------------------------------------------------------------
# ================================================================================

import sys
sys.path.append('../')
from dependencies.dependencies import *

if __name__ == '__main__':
    
    # argument parser --------------------++
    arguments = [
        argument('path_to_bytes',       'b', True, './temp_store/gcs-store'),
        argument('target_language',     't', True, 'fr'),
        argument('output_location',     'l', True, './temp_store/translation.json')
    ]

    ah                      = argument_handlr(arguments)
    path_to_bytes           = ah.args_dict['path_to_bytes']
    target_language         = ah.args_dict['target_language']
    output_location         = ah.args_dict['output_location']
    
    ah.print_configuration()
    # argument parser --------------------++
    
    v = GCS_Interface.convert_utf_to_dict(path_to_bytes)
    v = v['results']['transcripts'][0]['transcript']
    r = GCS_Interface.translater(value=v, target_language='fr')

    # input
    detectedSourceLanguage  = r['detectedSourceLanguage']
    input_text              = r['input']

    # output      
    translatedText          = r['translatedText']

    print(f'\nInput:  (language detected = {detectedSourceLanguage}):\n\n{input_text}\n')
    print(f'\nTranslation (language = {target_language}):\n\n{translatedText}\n')

    with open(output_location, 'wb') as f:
        pickle.dump(r, f)
    


