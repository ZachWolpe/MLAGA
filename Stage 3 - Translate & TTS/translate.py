

# --------------------------------------------------------------------------------
# ================================================================================
# File: translate.py
# 
# Object:  
#       - Translate transcription (default = French)
#
# --------------------------------------------------------------------------------
# author:   Zach Wolpe
# email:    zach.wolpe@medibio.com.au
# date:     10.03.23
# --------------------------------------------------------------------------------
# ================================================================================


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# example documentation: https://docs.aws.amazon.com/translate/latest/dg/examples-python.html
 
import boto3
 
class translation:
    
    def __init__(self):
        self.translate = boto3.client(service_name='translate')
        
    def TranslateText(self, text, SourceLanguageCode="en", TargetLanguageCode='fr'):
        self.text       = text
        self.response   = self.translate.translate_text(Text=self.text, SourceLanguageCode=SourceLanguageCode, TargetLanguageCode=TargetLanguageCode)
        print('Translation complete.\n')
