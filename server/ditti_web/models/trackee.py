from ditti_web.database import alchemy_db as db

class Trackee(db.Model):
    __tablename__ = 'trackees'
    fid = db.Column(db.Integer, primary_key=True, unique=True)