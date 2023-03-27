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
    