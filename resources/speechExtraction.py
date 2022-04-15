from flask_restful import Resource
from loguru import logger
from .wordsProcessModel import WordModel

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


            # Calling word pre processor model
            wm = WordModel(result)
            processed_words = json.dumps(wm.word_pre_processor())

            value = {
                "text" : result,
                "tokens" : json.loads(processed_words)["tokens"],
                "functional_words": json.loads(processed_words)["filtered_words"],
                }

            #remove the coverted.wav for get more space in the server
            os.remove(os.path.join(os.getenv('CONVERTED_AUDIO_PATH'), os.getenv('CONVERTED_AUDIO_FILE_NAME')))

            #return the json object which is having converted speech
            return json.loads(json.dumps(value)), 200
            
        except Exception as e:
            logger.error(str(e))
            return json.loads(json.dumps({"message" : str(e)})) , 500