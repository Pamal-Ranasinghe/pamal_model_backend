from .db import db

class Video(db.Document):
    name = db.StringField()
    link = db.StringField()

    def to_json(self):
        return {"name": self.name,
                "link": self.link}


class NormalVideo(db.Document):
    normal_vid_name = db.StringField()
    link = db.StringField()
    subtitle_link = db.StringField()

    def to_json(self):
        return {"name": self.normal_vid_name, 
                "link": self.link,
                "subtitle_link": self.subtitle_link}    

# class Video(db.Document):
#     name = db.StringField()
#     link = db.FileField()

#     def to_json(self):
#         return {"name": self.name,
#                 "link": self.video}