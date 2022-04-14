from flask_restful import Resource
from loguru import logger

import speech_recognition as sr
import moviepy.editor as mp
import json

class SpeechExtraction(Resource):

    # This function uses for extract the speech from a video
    # params: self
    # return: json
    # author: Pamal Ranasinghe
    def get(self):
        try:
            # Check the endpoint execution
            logger.info("Speech Extraction - GET - hits")

            clip = mp.VideoFileClip(r"assets/sample_video.mov")
            clip.audio.write_audiofile(r"assets/converted_wav/converted.wav")
            r = sr.Recognizer()
            audio = sr.AudioFile("assets/converted_wav/converted.wav")

            with audio as source:
                audio_file = r.record(source)

            result = r.recognize_google(audio_file)

            # Create a dict object which includes the result
            value = {"text" : result}

            #return the json object which is having converted speech
            return json.loads(json.dumps(value)), 200
            
        except Exception as e:
            logger.error(str(e))
            return json.loads(json.dumps({"message" : "Something went wrong"})) , 500