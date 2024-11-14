from app import db


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'Sample<{self.id}>'
