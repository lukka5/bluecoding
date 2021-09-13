from datetime import datetime

from app import db


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    full_url = db.Column(db.String)
    short_url = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<URL #{self.id} {self.full_url}>"
