from models import db, Pet
from app import app

db.drop_all()
db.create_all()

pet1 = Pet(name='Dougie', species='dog', age=4, photo_url='https://townofbeekmantown.com/wp-content/uploads/2019/06/2-dog.jpg', notes='Happy go lucky dog!')
pet2 = Pet(name='Sandy', species='cat', age=5, photo_url='https://www.humanesociety.org/sites/default/files/styles/1240x698/public/2018/06/cat-217679.jpg?h=c4ed616d&itok=3qHaqQ56', notes='Chill and relaxed at all times.')
pet3 = Pet(name='Mitchell', species='dog', age=9, photo_url='https://images.unsplash.com/photo-1587518102280-8d5fdcb68d13?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8b2xkJTIwZG9nfGVufDB8fDB8fA%3D%3D&w=1000&q=80', notes='Older and ready for a low-key lifestyle')
pet4 = Pet(name='Roxie', species='horse', age=1, photo_url='https://cdn.pixabay.com/photo/2016/02/15/13/26/horse-1201143__340.jpg', notes='Ready for a long day of riding!')
pet5 = Pet(name='Juniper', species='cat', age=3, photo_url='https://vetmed.tamu.edu/news/wp-content/uploads/sites/9/2019/10/CatGrassPetTalk.png', notes='Rambouncious explorer of a cat!')

db.session.add_all([pet1, pet2, pet3, pet4, pet5])
db.session.commit()