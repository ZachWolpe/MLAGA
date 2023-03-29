from pytube import YouTube
import os


def download_youtube(url, output):
    """Download YouTube videos.
    Args:
        url (str): YouTube video url.
        output (str): Download directory.

    Returns:
        bool: Return True if the video was downloaded and False if get an exception.
    """
    try:
        YouTube(url).streams.filter(progressive=True, file_extension='mp4').first().download(output)
        return True
    except Exception as e:
        print(e)
        return False 



def download_wav(url, path='./', exe='.wav', remove_spaces=False):
    # yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))
    yt = YouTube(url)
  
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
  
    # download the file
    out_file = video.download(output_path=path)
    
    # save the file
    base, ext = os.path.splitext(out_file)

    if remove_spaces:
        pth  = out_file.split('/')[-1]
        bse  = out_file.split('/')[:-1]
        base = pth.replace(' ','-')
    new_file = '/'.join(bse) + '/' + base.split('.')[0] + exe 
    os.rename(out_file, new_file)

    # result of success
    print(f"Youtube video  \"{yt.title}\" has been successfully downloaded.")
    return yt, base.split('/')[-1]
