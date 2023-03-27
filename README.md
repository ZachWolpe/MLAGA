# MLAGA: Multi-Lingual Audiobook GenerAtor
-----

_*MLAGA converts youtube videos to multilingual audiobooks. Learn language on the go while still consuming the same content you love.*_

It is an open source, multilingual audiobook generator built to demonstrate the power & ease of integrating AI APIs into your products.

![Pipeline architecture](https://github.com/ZachWolpe/MLAGA/blob/main/dependencies/architecture.png)

The pipeline is designed to be modular, fully automated & scalable. It is built using `Python` & `AWS` services.


## Getting Started

1. Clone the repo, install the dependencies & setup an AWS account (including the `cli` setup).
2. Create a private key & update your local AWS credentials after running `aws configure`.
3. Create an `AWS S3 bucket` with $3$ directories. Let's call them `$[S3/BUCKET-1]`, `$[S3/BUCKET-2]` & `$[S3/BUCKET-3]`.
4. Create two `AWS Lambda functions`. Let's call them `$[AWS-LAMBDA-1]` & `$[AWS-LAMBDA-2]`.
5. Upload all code files from the _*Stage 2 - Transcribe Audio*_ folder to `$[AWS-LAMBDA-1]`.
6. Upload all code files from the _*Stage 3 - Translate Text*_ folder to `$[AWS-LAMBDA-2]`.
7. Note: _*layers*_ can be used to install packages on AWS Lambda. [AWS Lambda Layers.](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
7. Setup Triggers using `AWS Event Bridge` to automatically trigger `$[AWS-LAMBDA-1]` & `$[AWS-LAMBDA-2]` when data arrives in `$[S3/BUCKET-1]` & `$[S3/BUCKET-2]` respectively.
8. Activate `AWS Transcribe`, `AWS Translate` & `AWS Polly` services.
9. Update bucket, trigger & lambda names in all files.


## Running the pipeline

Once your AWS is configured correctly, you only need to run _stage 1_ locally & _stage 2_ & _3_ will be triggered automatically.

### Stage 1 - Youtube to Audio (s3)

Run `Stage 1` locally using the built in `cli`. Provide the required arguments (example available in _`default_params.yaml`_).

Usage:

```
clear; python stage_01.py \
    -y $[youtube-url] \
    -e ".FLAC" \
    -b "$[S3/BUCKET-1]" \
    -p "./temp_store/" \
    -c
```

This will:

- Download the youtube video.
- Convert the video to audio.
- Upload the audio to `$[S3/BUCKET-1]`.


### Stage 2 - Transcribe Audio

- `$[AWS-LAMBDA-1]` will be triggered _automatically_ when data arrives in `$[S3/BUCKET-1]` (Triggered by _AWS Event Bridge_).
- `$[AWS-LAMBDA-1]` will convert the audio to text.
- `$[AWS-LAMBDA-1]` will upload the text to `$[S3/BUCKET-2]`.


### Stage 3 - Translate Text

- `$[AWS-LAMBDA-2]` will be triggered _automatically_ when data arrives in `$[S3-BUCKET-2]` (Triggered by _AWS Event Bridge_).
- `$[AWS-LAMBDA-2]` will
    - Translate the text from English to French.
    - Convert the text to speech.
    - Upload the two audio files to `$[S3/BUCKET-3]`.


Voila! Vous disposez d'un générateur de livres audio multilingues! 🎉🎉🎉


## Future work

- Setup a `config.yaml` file to store all parameters.
- Setup a `requirements.txt` file to store all dependencies.
- Tuning & model extention should be used to improve the quality of the generated audio.
- A UI should be added (perhaps using `AWS Amplify`) to interface the product without code/online.


## APIs

The implementation relies on multiple `AWS` APIs:

- `aws s3`              - [Storage.](https://aws.amazon.com/s3/)
- `aws Lambda`          - [Serverless computing.](https://aws.amazon.com/lambda/)
- `aws Event Bridge`    - [Triggering Lambdas.](https://aws.amazon.com/eventbridge/)
- `aws Transcribe`      - [Audio to text.](https://aws.amazon.com/transcribe/)
- `aws Translate`       - [Text to text.](https://aws.amazon.com/translate/)
- `aws Polly`           - [Text to speech.](https://aws.amazon.com/polly/)


### Additional notes

1. The `GCP - Google Cloud Platform` code is not used here, but is available as an alternative to `AWS`. The APIs are almost identical.
2. A "softer" explanation is available on my [Medium](https://medium.com/@zachcolinwolpe).

---
```
author:         zach wolpe
email:          zach.wolpe@medibio.com.au
date:           27.03.23
```
---