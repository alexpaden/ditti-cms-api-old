from ditti_web.database import alchemy_db as db
from sqlalchemy.dialects.postgresql import JSONB

class FollowTracker(db.Model):
    __tablename__ = 'follow_trackers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    fid = db.Column(db.Integer)
    following_fids = db.Column(JSONB)
    following_changes = db.Column(JSONB)
    follower_fids = db.Column(JSONB)
    follower_changes = db.Column(JSONB)
