from flask_restful import Resource
from loguru import logger
# from .wordsProcessModel import WordModel
# from .awsOperation import AwsOperation
from database.models import NormalVideo
from flask import request, session
from flask import jsonify

import speech_recognition as sr
import moviepy.editor as mp
import json
import os

class LectureVideo(Resource):

    def get(self):
        try:
            trans_vid = []
            for user in NormalVideo.objects:
                trans_vid.append(user.to_json())

            return trans_vid, 200
        except Exception as e:
            logger.error(str(e))
            return json.loads(json.dumps({"message" : str(e)})), 500
