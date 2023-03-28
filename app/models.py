#1.✅ Build out Model
from sqlalchemy import PrimaryKeyConstraint, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base  

#1.a ✅ Initialize declarative_base and save it to a variable called Base
Base=declarative_base()

#1.b ✅ Create a class Pet that inherits from Base
class Pet(Base):

    def __init__(self,name,species,breed,temperament,owner_id):
        self.id=None
        self.name=name
        self.species=species
        self.breed=breed
        self.temperament=temperament
        self.owner_id=owner_id
    
    # Set the "__tablename__" to 'pets
    __tablename__="pets"
    # Add table args for a primary key constraint based off the id

    #Create the following columns
    # id -> type integer
    id=Column(Integer,primary_key=True)
    # name -> type string
    name=Column(String,nullable=False)
    # species -> type string
    species=Column(String,nullable=False)
    # breed -> type string
    breed=Column(String,nullable=False)
    # temperament -> type string
    temperament=Column(String,nullable=False)
    # owner_id -> integer 
    owner_id=Column(Integer)


    
    #add a __repr__ method that returns a string containing the id, name, species, breed and temperament of our class
    def __repr__(self):
        return f"id={self.id} name={self.name} species={self.species} breed={self.breed} temperament={self.temperament} owner_id={self.owner_id}"

#Note: Nothing further goes in this file.
# The following will generate a number of folders and files

#2.✅ Migrations 
# In the app directory run `alembic init migrations`
# Your directory structure should look like the following 
# └── migrations
#     └── versions
#     ├── env.py
#     ├── README
#     ├── script.py.mako
# ├── alembic.ini
# ├── console.py
# └── models.py

#2.b Configuration
    # In alembic.ini, find `sqlalchemy.url`` and set it to `sqlalchemy.url = sqlite:///pet_app.db`
    # In env.py, find `target_metadata` and add `from models import Base` above it. Next, set target_metadata to `target_metadata = Base.metadata`

#2.c ✅ Generate a migration by running `alembic revision --autogenerate -m "Added Pet model"`
    # pet_app.db should have been added to your file structure

    # Take the time to review the migration and verify the database with SQLite Explorer or DB Browser

# 3✅ Head to debug.py to test out CRUD actions. 
