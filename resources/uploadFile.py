from loguru import logger
from flask_restful import Resource
from flask import request, session
from werkzeug.utils import secure_filename
from .awsOperation import AwsOperation
from database.models import NormalVideo
from .subtitleGeneration import GenerateSubtitle
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
            # subtitle = GenerateSubtitle(object_name)
            # subend = subtitle.generate_subtitle_aws()
            
            file_url = s3_session.meta.client.generate_presigned_url('get_object', Params = {'Bucket': 'lecvideos', 'Key': object_name}, ExpiresIn = 86400)
            # subtitle_url = s3_session.meta.client.generate_presigned_url('get_object', Params = {'Bucket': 'pamalcodex', 'Key': "my-output-files/"+ object_name+"-job.srt"}, ExpiresIn = 86400)
            
            
            video = NormalVideo(normal_vid_name=object_name, link = file_url, subtitle_link = "sample_link" ).save()

            session['uploaded_video_file'] = object_name

            return {"message": "File uploaded successfully"}, 200

        except Exception as e:
            logger.error(str(e))
            return json.loads(json.dumps({"message" : str(e)})), 500