from ditti_api.database import alchemy_db as db
from sqlalchemy.dialects.postgresql import JSONB

class ApiKeys(db.Model):
    __tablename__ = 'api_keys'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=db.func.now())
    expires_at = db.Column(db.DateTime(timezone=True))
    