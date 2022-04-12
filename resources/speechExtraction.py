from flask_restful import Resource
import speech_recognition as sr
import moviepy.editor as mp

class SpeechExtraction(Resource):
    #Test function
    def get(self):
        return 'API is working'