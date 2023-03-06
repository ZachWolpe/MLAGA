

# --------------------------------------------------------------------------------
# ================================================================================
# File: stage_00
# 
# Object:  
#       - Centralize import dependencies
#
# --------------------------------------------------------------------------------
# author:   Zach Wolpe
# email:    zach.wolpe@medibio.com.au
# date:     05.03.23
# --------------------------------------------------------------------------------
# ================================================================================

from dependencies.persistence_manager import *
from dependencies.youtube_downloader  import *
from dependencies.GCS_interface       import *
from dependencies.sys_args            import *
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech
from google.cloud import storage
import subprocess
import random
import pickle
import getopt
import boto3
import json
import time
import sys
import io
