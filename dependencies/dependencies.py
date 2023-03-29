

# --------------------------------------------------------------------------------
# ================================================================================
# File: dependencies.py
# 
# Object:  
#       - Centralize import dependencies
#
# --------------------------------------------------------------------------------
# author:   Zach Wolpe
# email:    zach.wolpe@medibio.com.au
# date:     26.03.23
# --------------------------------------------------------------------------------
# ================================================================================

from google.cloud                     import translate_v2 as translate
from google.cloud                     import texttospeech
from google.cloud                     import storage
from dependencies.persistence_manager import *
from dependencies.youtube_downloader  import *
from dependencies.GCS_interface       import *
from dependencies.sys_args            import *
import subprocess
import random
import pickle
import getopt
import boto3
import json
import time
import sys
import io
