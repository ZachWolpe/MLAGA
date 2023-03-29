

# --------------------------------------------------------------------------------
# ================================================================================
# File: stage_01
# 
# Object:  
#       - Download video from YoutTube
#       - Convert to Audio Format (.FLAC, .MP3)
#       - Upload to S3://[BUCKET]
#
# --------------------------------------------------------------------------------
# author:   Zach Wolpe
# email:    zach.wolpe@medibio.com.au
# date:     05.03.23
# --------------------------------------------------------------------------------
# ================================================================================

import sys
sys.path.append('../')
from dependencies.dependencies import *


def audio_in_cache(path_to_cached_file='/', exe=''):
    pth = f'{path_to_cached_file}' + exe
    return pth
 
 
if __name__=='__main__':
    # argument handler --------------++
    arguments = [
        argument('yt_url',      'y', True),
        argument('bucket_name', 'b', True),
        argument('exe',         'e', True),
        argument('path',        'p', True),
        argument('cached_audio','c', False)
    ]

    ah           = argument_handlr(arguments)
    exe          = ah.args_dict['exe']
    yt_url       = ah.args_dict['yt_url']
    bucket_name  = ah.args_dict['bucket_name']
    path         = ah.args_dict['path']
    cached_audio = ah.args_dict['cached_audio']
    # argument handler --------------++

    ah.print_configuration()
    # fetch from youtube ------++
    if not cached_audio:
        try:
            print('Downloading YouTube audio file.')
            yt, fname = download_wav(yt_url, path=path, exe=exe, remove_spaces=True)
        except Exception as e:
            print('FAILED to download & convert YouTube audio file.')
            print(e)
        filepath = path + fname + exe
    else:
        print('Using cached audio.')
        filepath = audio_in_cache(path_to_cached_file=path, exe=exe)

    # upload to bucket --------++
    persistence_manager_AWS.write_from_cli(
        local_file  = filepath,
        bucket      = bucket_name)
    # upload to bucket --------++
