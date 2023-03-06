
# --------------------------------------------------------------------------------
# ================================================================================
# File: stage_04
# 
# Object:  
#       - TTS: Test-To-Speech!
#
# --------------------------------------------------------------------------------
# author:   Zach Wolpe
# email:    zach.wolpe@medibio.com.au
# date:     05.04.23
# --------------------------------------------------------------------------------
# ================================================================================

from stage_00 import *


if __name__ == '__main__':
    
    # argument parser --------------------++
    arguments = [
        argument('json_file',           'f', True, './temp_store/translation.json'),
        argument('language_code',       'l', True, 'fr-FR'),
        argument('output_location',     'o', True, './temp_store/TTS.mp3')
    ]

    ah                      = argument_handlr(arguments)
    json_file               = ah.args_dict['json_file']
    language_code           = ah.args_dict['language_code']
    output_location         = ah.args_dict['output_location']
    ssml_gender             = texttospeech.SsmlVoiceGender.FEMALE
    
    ah.print_configuration()
    # argument parser --------------------++

    # load Translation
    with open(json_file, 'rb') as f:
        json_data = pickle.load(f)
    s = json_data['translatedText']

    GCS_Interface.text_to_speech(text=s, audio_file_location=output_location, language_code=language_code, ssml_gender=ssml_gender)
    
