class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.owner_pets = []

    def pets(self):
        owner_pets = [pet for pet in Pet.all if pet.owner == self]
        return owner_pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        pet.owner = self
        self.owner_pets.append(pet)

    def get_sorted_pets(self):
        owner_pets = self.pets()
        owner_pets.sort(key=lambda x: x.name)
        return owner_pets
