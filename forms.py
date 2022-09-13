from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, NumberRange

class PetForm(FlaskForm):
    '''Form for Handling Pet Addition'''

    pet_name = StringField('Pet Name', validators=[InputRequired(message='Pet Name Required')] )
    species = StringField('Species', validators=[InputRequired(message='Pet Species Required')])
    photo_url = StringField('Add Photo')
    pet_age = IntegerField('Pet`s Age',validators=[NumberRange(min=1, max=30)])
    notes = TextAreaField('Notes')
    

class EditPetForm(FlaskForm):
    '''Form for editing Pet'''

    photo_url = StringField('Add Photo')
    pet_availability = BooleanField('Available for Adoption?')
    notes = TextAreaField('Notes')