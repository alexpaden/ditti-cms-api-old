from ditti_api.database import alchemy_db as db

class Trackee(db.Model):
    __tablename__ = 'trackees'
    fid = db.Column(db.Integer, primary_key=True, unique=True)