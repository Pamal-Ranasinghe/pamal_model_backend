from .db import db

class Video(db.Document):
    name = db.StringField()
    link = db.StringField()

    def to_json(self):
        return {"name": self.name,
                "link": self.link}


class NormalVideo(db.Document):
    normal_vid_name = db.StringField()
    # link = db.StringField()

    def to_json(self):
        return {"name": self.normal_vid_name}

# class Video(db.Document):
#     name = db.StringField()
#     link = db.FileField()

#     def to_json(self):
#         return {"name": self.name,
#                 "link": self.video}