from loguru import logger
from flask_restful import Resource
from flask import request, session
from werkzeug.utils import secure_filename
from .awsOperation import AwsOperation
from database.models import NormalVideo

import os
import json

class UploadFile(Resource):
        
    def post(self):
        try:
            aws = AwsOperation()
            s3_session = aws.s3_connector()
            # bucket = s3_session.Bucket('rpserverone')

            object_name = secure_filename(request.files['file'].filename)

            # s3_session.meta.client.upload_fileobj(str(request.files['file']), bucket, object_name)
            s3_session.meta.client.upload_fileobj(request.files['file'], "lecvideos", object_name)
            video = NormalVideo(normal_vid_name=object_name).save()

            return {"message": "File uploaded successfully"}, 200

        except Exception as e:
            logger.error(str(e))
            return json.loads(json.dumps({"message" : str(e)})), 500