from flask import Flask, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import EditPetForm, PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet-adoption-db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secRetAdopTion123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/', methods=['GET'])
def home_page():
    '''Redirect to Pets Avaliable Page'''

    return redirect('/pets')

@app.route('/pets', methods=['GET'])
def list_pets():
    '''Lists All Pets'''

    pets = Pet.query.all()

    return render_template('pets_list.html', pets=pets)

@app.route('/pets/add', methods=['GET', 'POST'])
def add_pet():
    '''Handle Form Submission for Adding Pet'''

    form = PetForm()

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.pet_age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/pets')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/pets/<int:pet_id>/details', methods=['GET', 'POST'])
def show_edit_pet_details(pet_id):
    '''Show Pet details and form to edit details'''

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.availability = form.pet_availability.data

        db.session.add(pet)
        db.session.commit()

        return redirect('/pets')
    else:
        return render_template('pet_details.html', form=form, pet=pet)


    

