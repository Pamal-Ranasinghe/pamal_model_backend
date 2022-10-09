from flask_restful import Resource
from loguru import logger
from .wordsProcessModel import WordModel
from .awsOperation import AwsOperation
from flask import request, session

import speech_recognition as sr
import moviepy.editor as mp
import json
import os

class SpeechExtraction(Resource):

    # This function uses for extract the speech from a video
    # params: self
    # return: json
    # author: Pamal Ranasinghe

    def get(self):
        # def update_record():
        #     record = request.get_json()
        #     user = User(name=record['name'], email=record['email']).save()
        #     # user.save()

        #     logger.info("object", user)

        #     logger.info("record is inserted")

        #     return {"message" : "ok"}

        try:
            
            logger.info("Speech Extraction - GET - hits")
            aws = AwsOperation()
            s3_session = aws.s3_connector()
            bucket = s3_session.Bucket('lecvideos')

            # extension = '.mov'

            record = request.get_json()
            logger.info("record is downloaded")
            logger.info(record['name'])
            # bucket.download_file(record['name']+extension, 'D:/rp_server_one/assets/'+record['name']+extension)
            bucket.download_file(record['name'], 'D:/rp_server_one/assets/'+record['name'])
            # Check the endpoint execution

            clip = mp.VideoFileClip(r"assets/"+record['name'])
            clip.audio.write_audiofile(r"assets/converted_wav/converted.wav")
            r = sr.Recognizer()
            audio = sr.AudioFile("assets/converted_wav/converted.wav")

            with audio as source:
                audio_file = r.record(source)

            result = r.recognize_google(audio_file)


            # Calling word pre processor model
            wm = WordModel(result)
            processed_words = json.dumps(wm.word_pre_processor())

            value = {
                "text" : result,
                "tokens" : json.loads(processed_words)["tokens"],
                "functional_words": json.loads(processed_words)["filtered_words"],
                }

            #remove the coverted.wav for get more space in the server
            os.remove(os.path.join("D:/rp_server_one/assets/converted_wav", "converted.wav"))

            #return the json object which is having converted speech
            return json.loads(json.dumps(value)), 200
            
        except Exception as e:
            logger.error(str(e))
            return json.loads(json.dumps({"message" : str(e)})) , 500