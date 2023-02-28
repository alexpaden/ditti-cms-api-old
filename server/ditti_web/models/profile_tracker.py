from ditti_web.database import alchemy_db as db

class ProfileTracker(db.Model):
    __tablename__ = 'profile_trackers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), default=db.func.now())
    fid = db.Column(db.Integer)
    username = db.Column(db.String(75))
    display_name = db.Column(db.String(64))
    bio = db.Column(db.String(160))
    pfp_url = db.Column(db.String(255))
    following_count = db.Column(db.Integer)
    follower_count = db.Column(db.Integer)
