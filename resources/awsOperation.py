import boto3
import glob
import numpy as np

class AwsOperation:
        
    def __init__(self):
        pass

    def s3_connector(self):
    
        session = boto3.Session(
            aws_access_key_id="AKIAWAP4EPNHCC6BXFXV",
            aws_secret_access_key="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",
        )
        return session.resource('s3')
        # return s3.Bucket(self.bucket_name)