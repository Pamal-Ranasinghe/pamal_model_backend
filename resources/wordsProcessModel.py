from nltk.tokenize import word_tokenize
from loguru import logger
from .awsOperation import AwsOperation
from .wordsMappingModel import WordMapping
from moviepy.editor import *

import os
import json
import cv2
import numpy as np
import glob

class WordModel:

    def __init__(self,para):
        self.para = para

    # This function uses for pre-processing on words 
    # params: self
    # return: json
    # author: Pamal Ranasinghe

    def word_pre_processor(self):
        try:
            logger.info('word_pre_process - hits')

            clip_arr = []

            # Identify all the takens
            para_tokenize = word_tokenize(self.para)
            logger.info('Tokenized Words : ' ,para_tokenize)

            # Remove the stop words from the text
            from nltk.corpus import stopwords
            stop_words = set(stopwords.words(os.getenv('NORMAL_LANGUAGE')))
            filtered_sentence = [w for w in para_tokenize if not w.lower() in stop_words]
            filtered_sentence = []
 
            #Append the rest of words after removing the stop words
            for w in para_tokenize:
                if w not in stop_words:
                    filtered_sentence.append(w)

            word_mapper = WordMapping(filtered_sentence)
            word_mapper.words_map_with_gestures()

            return json.loads(json.dumps({
                "filtered_words" : filtered_sentence,
                "tokens" : para_tokenize,                   
                }))

        except Exception as e:
            logger.error(str(e))
            return json.loads(json.dumps({"message" : str(e)})), 500

