from .awsOperation import AwsOperation
from moviepy.editor import *
from loguru import logger

import os
import json
import cv2
import numpy as np
import glob


# pamalcodex

class WordMapping:

    def __init__(self, filtered_sentence):
        self.filtered_sentence = filtered_sentence

    def words_map_with_gestures(self):
            
            try:
                clip_arr = []

                aws = AwsOperation()
                s3_session = aws.s3_connector()
                bucket = s3_session.Bucket('rpserverone')

                extension = ".mp4"

                for i in range(0, len(self.filtered_sentence)):
                    print(type(i))
                    print(str(self.filtered_sentence[i]) + extension)
                    bucket.download_file(str(self.filtered_sentence[i])+extension, 'D:/s3_tute/'+str(self.filtered_sentence[i])+extension)

                for i in range(0, len(self.filtered_sentence)):
                    with open('D:/s3_tute/' + str(self.filtered_sentence[i])+extension) as f:
                        clip = VideoFileClip(f.name)
                        clip_arr.append(clip)

                final = concatenate_videoclips(clip_arr)
                final.write_videofile("assets/final_video/final_out.mp4")

                s3_session.meta.client.upload_file("assets/final_video/final_out.mp4","pamalcodex", "final_out.mp4")
                os.remove(os.path.join("D:/rp_server_one/assets/final_video", "final_out.mp4"))
            
            except Exception as e:
                logger.error(str(e))
                return json.loads(json.dumps({"message" : str(e)})), 500