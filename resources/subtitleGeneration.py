from __future__ import print_function
from flask_restful import Resource
from loguru import logger
from .awsOperation import AwsOperation
from flask import request, session

import speech_recognition as sr
import moviepy.editor as mp
import time
import boto3
import json
import os

class GenerateSubtitle:

    def __init__(self, video_name):
        self.video_name = video_name


    def generate_subtitle_aws(self):
            try:
                s3 = boto3.client('s3', aws_access_key_id="AKIAWAP4EPNHCC6BXFXV", aws_secret_access_key="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")
                transcribe = boto3.client('transcribe', 'us-east-1')

                job_name = self.video_name+"-job"
                job_uri = "s3://lecvideos/"+self.video_name
                transcribe.start_transcription_job(
                    TranscriptionJobName = job_name,
                    Media = {
                        'MediaFileUri': job_uri
                    },
                    OutputBucketName = 'pamalcodex',
                    OutputKey = 'my-output-files/',
                    LanguageCode = 'en-US',
                    Subtitles = {
                        'Formats': [
                            'srt'
                        ],
                        'OutputStartIndex': 1
                    }   
                )

                while True:
                    status = transcribe.get_transcription_job(TranscriptionJobName = job_name)
                    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                        break
                    print("Not ready yet...")
                    time.sleep(5)
                print(status)

                return True
            
            except Exception as e:
                logger.error(str(e))
                return json.loads(json.dumps({"message" : str(e)})) , 500