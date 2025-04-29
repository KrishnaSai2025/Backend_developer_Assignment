from . import db
from datetime import datetime

class Video(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(255), index=True)
    description = db.Column(db.Text, index=True)
    published_at = db.Column(db.DateTime, index=True)
    thumbnail_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
