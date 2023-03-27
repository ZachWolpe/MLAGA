# --------------------------------------------------------------------------------
# ================================================================================
# File: stage_03
# 
# Object:  
#       - Download blob from GSC bucket.
#
# --------------------------------------------------------------------------------
# author:   Zach Wolpe
# email:    zach.wolpe@medibio.com.au
# date:     25.04.23
# --------------------------------------------------------------------------------
# ================================================================================

import sys
sys.path.append('../')
from dependencies.dependencies import *


if __name__ == '__main__':
    
    # argument parser --------------------++
    arguments = [
        argument('source_blob_name',        's', True, None),
        argument('bucket_name',             'b', True, None),
        argument('destination_file_name',   'd', True, './temp_store/gcs-store'),
    ]

    ah                      = argument_handlr(arguments)
    source_blob_name        = ah.args_dict['source_blob_name']
    bucket_name             = ah.args_dict['bucket_name']
    destination_file_name   = ah.args_dict['destination_file_name']
    
    ah.print_configuration()
    # argument parser --------------------++

    GCS_Interface.download_blob(source_blob_name=source_blob_name, bucket_name=bucket_name, destination_file_name=destination_file_name)
