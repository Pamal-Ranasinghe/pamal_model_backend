from pdb import post_mortem
from .speechExtraction import SpeechExtraction
from .uploadFile import UploadFile
from .translatedVideo import TranslatedVideos
from .noramalVideo import LectureVideo
def initialize_routes(api):
    api.add_resource(SpeechExtraction, "/api/extraction")
    api.add_resource(UploadFile, "/api/upload_video")
    api.add_resource(TranslatedVideos, "/api/translate_video")
    api.add_resource(LectureVideo, "/api/normal_video")