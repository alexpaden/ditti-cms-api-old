from ditti_web.database import alchemy_db as db

class TrackerManager(db.Model):
    __tablename__ = 'tracker_managers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), default=db.func.now())
    trackee_fid = db.Column(db.Integer)
    tracker_fid = db.Column(db.Integer)


