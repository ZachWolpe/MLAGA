
from google.cloud import storage
import subprocess

class cloud_persistence_manager_interface:
    def __init__(self) -> None:
        pass

    def write_to_bucket(self):
        pass

    def read_from_bucket(self):
        pass

    @staticmethod
    def write_from_cli(local_file, bucket):
        pass

    @staticmethod
    def list_blobs():
        pass


class persistence_manager_AWS(cloud_persistence_manager_interface):
    def __init__(self) -> None:
        pass

    def write_to_bucket(self):
        pass

    def read_from_bucket(self):
        pass

    @staticmethod
    def write_from_cli(local_file, bucket):
        local_file = local_file.strip().replace('#', '').replace('?', '').replace(' ', '\ ')
        cmd        = f"aws s3 cp {local_file} s3://{bucket}"
        
        try:
            print(f'Executing command on shell: \n {cmd}\n')
            subprocess.run(cmd, shell=True) 
        except Exception as e:
            print(f'\n   - Failed to write to AWS bucket.')
            print(f'\n   - Failed command: {cmd}')
            print(f'\n   - Exception:\n   {e}')


    @staticmethod
    def list_blobs():
        pass
    


class persistence_manager_GCS(cloud_persistence_manager_interface):

    def __init__(self) -> None:
        pass

    def _client_code(self, bucket_name, blob_name):
        storage_client  = storage.Client()
        bucket          = storage_client.bucket(bucket_name)
        blob            = bucket.blob(blob_name)
        return storage_client, bucket, blob

    def write_to_bucket(self, bucket_name, blob_name, object_to_write):
        _, _, blob= self._client_code(bucket_name, blob_name)
        with blob.open("w") as f:
            f.write(object_to_write)
        print(f'{blob_name} written to {bucket_name} successfully.')

    def read_from_bucket(self, bucket_name, blob_name):
        _, _, blob= self._client_code(bucket_name, blob_name)
        with blob.open("r") as f:
            return f.read()
        
    @staticmethod
    def write_to_gcs_terminal(file_path, bucket):
        try:
            file_path   = file_path.strip().replace('#', '').replace('?', '').replace(' ', '\ ')
            cmd         = f'gcloud storage cp {file_path} gs://{bucket}'
            subprocess.run(cmd, shell=True) 
        except Exception as e:
            print('Failed to write to bucket.')
            print(f'Exception:\n   {e}')

        
    @staticmethod
    def list_blobs(bucket_name):
        """Lists all the blobs in the bucket."""
        storage_client  = storage.Client()
        blobs           = storage_client.list_blobs(bucket_name)
        for blob in blobs:
            print(blob.name)
        
        # or 
        # storage_client  = storage.Client()
        # bucket = storage_client.get_bucket(bucket_name)
        # print(bucket.list_blobs())
