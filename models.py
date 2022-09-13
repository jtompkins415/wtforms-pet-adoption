from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    '''Connects to DB'''
    db.app = app
    db.init_app(app)

stock_photo = 'https://christopherscottedwards.com/wp-content/uploads/2018/07/Generic-Profile.jpg'

class Pet(db.Model):
    '''Pet Model'''

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=stock_photo)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        p = self
        return f'<Pet id={p.id} name={p.name} species={p.species}>'
    




