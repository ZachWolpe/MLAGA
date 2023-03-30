
from test_to_speech import *
from translate import *
from urllib import *
import urllib
import boto3
import json
import os
# notes to add packages: https://aws.amazon.com/premiumsupport/knowledge-center/lambda-import-module-error-python/#:~:text=This%20is%20because%20Lambda%20isn,Python%20inside%20the%20%2Fpython%20folder.


print('loading function: Transcription to S3 bucket')
s3          = boto3.resource('s3')
transcribe  = boto3.client('transcribe')

        
def get_log_message(**kwargs):
    lines  = '\n\n=========================================================================================================\n'
    for k,v in kwargs.items():
        lines += f'\n        {k}: {v:<{13}}'
        lines += '\n\n=========================================================================================================\n\n'
    return lines

def lambda_handler(event, context):
    BUCKET_NAME = 'my-aws-bucket-12'
    job_name    = event['detail']['TranscriptionJobName']
    job         = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    uri         = job['TranscriptionJob']['Transcript']['TranscriptFileUri']
    prefix      = f"transcriptions/{job_name}/"
    prt         = get_log_message(BUCKET_NAME=BUCKET_NAME,prefix=prefix,job_name=job_name,uri=uri)
    print(prt)

    content = urllib.request.urlopen(uri).read().decode('UTF-8')
    #write content to cloudwatch logs
    print(json.dumps(content))
    
    data                = json.loads(content)
    transcribed_text    = data['results']['transcripts'][0]['transcript']
    
    # translate -----------------------++
    print('translating: ')
    try:
        trans = translation()
        trans.TranslateText(transcribed_text)
    except Exception as e:
        print(e)
    print('text: \n', trans.text)
    print('response: \n', trans.response)
    # translate -----------------------++
    
    # TTS: FRENCH ---------------------++
    print('TTS French: ')
    polly_fr = Polly_API()
    polly_fr.speech_synthesis(
        Text                = trans.response['TranslatedText'],
        OutputS3BucketName  = BUCKET_NAME,
        VoiceId             = 'Lea', # 'Remi',
        OutputS3KeyPrefix   = prefix + 'french-audio_'
        )
    # TTS: FRENCH ---------------------++
    
    # TTS: ENGLISH --------------------++
    print('TTS English: ')
    polly_en = Polly_API()
    polly_en.speech_synthesis(
        Text                = trans.text,
        LanguageCode        = 'en-US',
        OutputS3BucketName  = BUCKET_NAME,
        OutputS3KeyPrefix   = prefix + 'english-audio_'
        )
    # print('TTS French: ')
    # polly_en = Polly_API()
    # polly_en.TTS(Text=trans.text)
    # print('response: \n', polly_en.response)
    # # TTS: ENGLISH --------------------++
    
    
    # write to s3 ---------------------++
    print('Writing to S3...')
    objects = [transcribed_text, trans.response['TranslatedText']]
    names   = ['English_text.txt', 'French_text.txt']
    for obj, name in zip(objects, names):
        object = s3.Object(BUCKET_NAME, prefix + name)
        object.put(Body=obj)
    print(f'Objects written to {BUCKET_NAME} successfully.')
    
    print('Lambda executed successfully.')
