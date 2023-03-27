from transcriber import *
import urllib.parse
import boto3
import json

print('Loading transcriber lambda function')
s3 = boto3.client('s3')


def generate_transcriber_params(MediaFormat='mp4', LanguageCode='en-US', MediaSampleRateHertz=44100):
    job_name                = f'AWS-Transcriber-{random.randint(-99999999,+99999999)}'
    MediaFormat             = MediaFormat
    LanguageCode            = LanguageCode
    MediaSampleRateHertz    = MediaSampleRateHertz
    return job_name, MediaFormat, LanguageCode, MediaSampleRateHertz


def _get_transcribe_obj_url(bucket, filename):
    # example: "s3://[BUCKET]/audiofile.FLAC"
    return f's3://{bucket}/{filename}'


def _get_bucket_name_obj_name(event):
    bucket_name  = event['Records'][0]['s3']['bucket']['name']
    objct_name   = event['Records'][0]['s3']['object']['key']
    return bucket_name, objct_name


def _get_log_message(bucket,filename,file_uri,job_name,MediaFormat,LanguageCode,MediaSampleRateHertz):
    message = \
    f"""

    ===========================================================================================
            bucket:                 {bucket}
            filename:               {filename}
            file_uri:               {file_uri}
            job_name:               {job_name}
            MediaFormat:            {MediaFormat}
            LanguageCode:           {LanguageCode}
            MediaSampleRateHertz    {MediaSampleRateHertz}
    ===========================================================================================
    
    """
    print(message)


def lambda_handler(event, context):

    # fetch details ---------++
    bucket, filename    = _get_bucket_name_obj_name(event)
    file_uri            = _get_transcribe_obj_url(bucket, filename)
    key                 = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    # fetch details ---------++
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        print(response)
        
        # execute trancription job -------++
        job_name, MediaFormat, LanguageCode, MediaSampleRateHertz = generate_transcriber_params()
        job_name = filename.replace(".FLAC", '').replace(" ", '-')
        _get_log_message(bucket, filename, file_uri, job_name, MediaFormat, LanguageCode, MediaSampleRateHertz)
        execute(job_name, file_uri, MediaFormat, LanguageCode, MediaSampleRateHertz)
        # execute trancription job -------++

        return {
            'TranscriptionJobName': response['TranscriptionJob']['TranscriptionJobName'],
            'TranscriptionJob':     response['TranscriptionJob'],
            'ContentType':          response['ContentType']
        }

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e