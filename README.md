# MLAGA: Multi-Lingual Audiobook Generator (with AI)
-----

MLAGA is an open source, multilingual audiobook generator build to demonstrate the power & ease of integrating AI into your products.



Runtime:

    - `stage_00.py`:    Centralize dependencies
    - `stage_01.py`:    Download YouTube, covert to audio, upload to s3 bucket.
    - `stage_02.py`:    Start AWS Transcribe job, upload to s3 bucket.
    - `stage_03.py`:    Download blob from GSC bucket. (transfer s3 -> GSC done online)
    - `stage_04.py`:    Translate text (En-to-Fr)
    - `stage_05.py`:    TTS: Test-To-Speech!


---
```
author:         zach wolpe
email:          zach.wolpe@medibio.com.au
date:           06.03.23
```
---