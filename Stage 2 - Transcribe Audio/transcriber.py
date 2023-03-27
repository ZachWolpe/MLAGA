# --------------------------------------------------------------------------------
# ================================================================================
# File: transcriber.py
# 
# Object:  
#       - Start AWS Transcribe job.
#       - Store output to S3 Bucket.
#
# --------------------------------------------------------------------------------
# author:   Zach Wolpe
# email:    zach.wolpe@medibio.com.au
# date:     05.04.23
# --------------------------------------------------------------------------------
# ================================================================================

from dependencies import *


def transcribe_file(job_name, file_uri, transcribe_client, MediaFormat, LanguageCode, MediaSampleRateHertz):
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media               = {'MediaFileUri': file_uri},
        MediaFormat         = MediaFormat,
        LanguageCode        = LanguageCode,
        MediaSampleRateHertz= int(MediaSampleRateHertz)
    )

    max_tries = 60
    while max_tries > 0:
        max_tries  -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                print(
                    f"Download the transcript from\n"
                    f"\t{job['TranscriptionJob']['Transcript']['TranscriptFileUri']}.")
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)


def execute(job_name, file_uri, MediaFormat, LanguageCode, MediaSampleRateHertz):
    transcribe_client = boto3.client('transcribe')
    transcribe_file(job_name, file_uri, transcribe_client, MediaFormat, LanguageCode, MediaSampleRateHertz)
