
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech
from google.cloud import storage
import json

class GCS_Interface:

    @staticmethod
    def list_blobs(bucket):
        storage_client  = storage.Client()
        blobs           = storage_client.list_blobs(bucket)
        blob_names      = []
        for blob in blobs:
            print(blob.name)
            blob_names.append(blob)
        return blob_names

    def get_json_blob(bucket):
        lb = GCS_Interface.list_blobs(bucket)
        bn = [i for i in lb if '.json' in i][0]


    @staticmethod
    def download_blob(bucket_name, source_blob_name, destination_file_name):
        """
        Downloads a blob from the bucket.

        Args:
           bucket_name           = "your-bucket-name"               The ID of your GSC bucket
           source_blob_name      = "storage-object-name"            The ID of your GCS object
           destination_file_name = "local/path/to/file"             The path to which the file should be downloaded

        """
        storage_client  = storage.Client()
        bucket          = storage_client.bucket(bucket_name)

        # Construct a client side representation of a blob.
        # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
        # any content from Google Cloud Storage. As we don't need additional data,
        # using `Bucket.blob` is preferred here.
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)

        print(
            "Downloaded storage object {} from bucket {} to local file {}.".format(
                source_blob_name, bucket_name, destination_file_name)
            )


    @staticmethod
    def download_blob_into_memory(bucket_name, blob_name):
        """
        Downloads a blob into memory.

        Args:
            bucket_name           = "your-bucket-name"               The ID of your GSC bucket
            source_blob_name      = "storage-object-name"            The ID of your GCS object
        
        """
        storage_client  = storage.Client()
        bucket          = storage_client.bucket(bucket_name)

        # Construct a client side representation of a blob.
        # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
        # any content from Google Cloud Storage. As we don't need additional data,
        # using `Bucket.blob` is preferred here.
        blob = bucket.blob(blob_name)
        contents = blob.download_as_string()

        print(
            "Downloaded storage object \n     {} from bucket \n     {} as the following string: \n    {}.".format(
                blob_name, bucket_name, contents)
                )



    @staticmethod
    def convert_utf_to_dict(path_to_utf_string):
        # parse utf-8 string
        with open(path_to_utf_string, 'rb') as file:
            data = file.read()
        return json.loads(data.decode('utf-8'))


    @staticmethod
    def translater(value, target_language='fr'):
        client  = translate.Client()
        r       = client.translate(values=value, target_language='fr')
        return r
        

    @staticmethod
    def text_to_speech(text, audio_file_location, language_code='fr-FR', ssml_gender=texttospeech.SsmlVoiceGender.FEMALE):

        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=text)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(language_code=language_code, ssml_gender=ssml_gender)

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

        # The response's audio_content is binary.
        with open(audio_file_location, "wb") as out:
            out.write(response.audio_content)
            print(f'Audio content written to file "{audio_file_location}"')