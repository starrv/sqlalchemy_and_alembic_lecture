
# 3.✅ CRUD practice
# To run the file run `python3 console.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)


if __name__ == '__main__':
    print("hello world!!")
    #3.1 ✅ Uncomment bellow to create the engine
    engine = create_engine('sqlite:///pet_app.db')
    #Base.metadata.create_all(engine)
    #3.2 ✅ Uncomment bellow to create sessions and bind o the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    #3.3 ✅  -- Creating records
        # Create a pet and save it to the data base with session.add and session.commit
    pet=Pet("Snoopy","dog","beagle","playful",1)
    session.add(pet)
    session.commit()

    all=session.query(Pet).all()
    print(all)
    print("\n\n")
        # Create multiple pets and bulk save them with  session.bulk_save_objects and session.commit
    pet_2=Pet("Rose","dog","German Shepard","loving",1)
    pet_3=Pet("Garfield","cat","regular cat","couch potato",2)

    session.bulk_save_objects([pet_2,pet_3])
    session.commit()

    all=session.query(Pet).all()
    for pet in all:
        print(pet)
    print("\n\n")

        #session.add(rose)
        #Note: bulk save will not contain the id

        #verify by checking the db 
    #3.4 ✅ Read
        # Get all with session.query
        # Print the pets 

        #Get all of the pet names and print them with session.query
    names=session.query(Pet.name).all()
    for name in names:
        print(name[0],end=",")
    print("\n\n\n")
        #Get all the pet names and print them in order with session.query and order_by
    ordered_names=session.query(Pet.name).order_by(Pet.name).all()
    for name in ordered_names:
        print(name[0],end=",")
    print("\n\n\n")
        #Get the first pet with session.query and first
    first_pet=session.query(Pet).first()
    print(first_pet)
    print("\n\n\n")

        #Filter pet by temperament with session.query and filter 
    temperament=session.query(Pet).filter(Pet.temperament=="playful")
    for pet in temperament:
        print(pet)
    print("\n\n\n")

    #3.5 ✅ Update 
        # Update the pets name and print the updated pet info
    first_pet=session.query(Pet).first()
    print(f" init pet: {first_pet}")
    first_pet.name="Daphne"
    session.commit()
    print(f" updated pet: {first_pet}")
    print("\n\n\n")
    
        # Update all the pets temperament to 'cool' and print the pets 
    all=session.query(Pet).filter(Pet.name=="Garfield").update({
        Pet.temperament:"cool"
    })
    session.commit()
    print("update pets' tempermant to cool ")
    print(all)
    print("\n\n\n")

    all=session.query(Pet).all()
    for pet in all:
        print(pet)
    print("\n\n\n")

    #3.6 ✅  Delete
        # Delete one item by querying the first pet, deleting it and committing it
    first_pet=session.query(Pet).first()
    print(f"first pet: {first_pet}")
    session.delete(first_pet)
    session.commit()

    first_pet=session.query(Pet).first()
    print(f"deleted pet: {first_pet}")
    print("\n\n\n")
        #delete all the pets with session.query and .delete
    session.query(Pet).delete()
    session.commit()

    all=session.query(Pet).all()
    for pet in all:
        print(pet)
    print("\n\n\n")

    # optional Break point for debugging and testing
    import ipdb; ipdb.set_trace()