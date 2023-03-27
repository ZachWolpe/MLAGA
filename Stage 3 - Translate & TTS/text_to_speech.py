
# --------------------------------------------------------------------------------
# ================================================================================
# File: test_to_speech.py
# 
# Object:  
#       - TTS: Test-to-Speech
#
# Docs:
#       - https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html

# 
# --------------------------------------------------------------------------------
# author:   Zach Wolpe
# email:    zach.wolpe@medibio.com.au
# date:     10.03.23
# --------------------------------------------------------------------------------
# ================================================================================


import boto3

class Polly_API:
    
    def __init__(self):
        self.polly_client = boto3.client('polly', region_name='us-east-1')
  

    def TTS(self, Text='Je suis Francaise!!! C\'est fantastique! Ce sont beau!',LanguageCode='fr-FR', VoiceId='Bianca', OutputFormat='mp3',Engine='neural'):
        self.response = self.polly_client.synthesize_speech(
            VoiceId      = VoiceId,
            OutputFormat = OutputFormat, 
            Text         = Text ,
            LanguageCode = LanguageCode,
            Engine       = Engine)
            
    def speech_synthesis(self, Text, OutputS3BucketName, OutputS3KeyPrefix, LanguageCode='fr-FR', VoiceId='Lea', OutputFormat='mp3',Engine='neural'):
        self.response = self.polly_client.start_speech_synthesis_task(
            VoiceId             = VoiceId,
            OutputFormat        = OutputFormat, 
            Text                = Text,
            LanguageCode        = LanguageCode,
            Engine              = Engine,
            OutputS3BucketName  = OutputS3BucketName,
            OutputS3KeyPrefix   = OutputS3KeyPrefix
            )



# notes:
    # # polly_fr.TTS(Text=trans.response['TranslatedText'])
    # print('response: \n', polly_fr.response)
    # object_name = polly_fr.response['SynthesisTask']['OutputUri'] #returns entire S3 Path, need to index for key to create S3 Pre-Signed URL
    # startIndex = object_name.find("InputAudio") 
    # keyName = object_name[startIndex: len(object_name)]
    # print(keyName)