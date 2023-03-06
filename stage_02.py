# --------------------------------------------------------------------------------
# ================================================================================
# File: stage_02
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

from stage_00 import *


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



if __name__ == '__main__':
    
    # argument parser --------------------++
    
    arguments = [
        argument('job_name',                'n', True, f'AWS-Transcriber-{random.randint(-99999999,+99999999)}'),
        argument('file_uri',                'f', True),
        argument('MediaFormat',             'm', True, 'mp4'),
        argument('LanguageCode',            'l', True, 'en-US'),
        argument('MediaSampleRateHertz',    's', True, 44100),
    ]

    ah                      = argument_handlr(arguments)
    job_name                = ah.args_dict['job_name']
    file_uri                = ah.args_dict['file_uri']
    MediaFormat             = ah.args_dict['MediaFormat']
    LanguageCode            = ah.args_dict['LanguageCode']
    MediaSampleRateHertz    = ah.args_dict['MediaSampleRateHertz']
    ah.print_configuration()
    # argument parser --------------------++
    
    execute(job_name, file_uri, MediaFormat, LanguageCode, MediaSampleRateHertz)

