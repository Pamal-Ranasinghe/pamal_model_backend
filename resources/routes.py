from .speechExtraction import SpeechExtraction

def initialize_routes(api):
    api.add_resource(SpeechExtraction, "/api/extraction")