class Animal:
    def __init__(self, name, complextion, sound):
        self._name = name
        self._complextion = complextion
        self._sound = sound

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if value > 0:
            self._name = value
        else:
            print("Name must be positive")

    @property
    def complextion(self):
        return f"{self._complextion}"

    @property
    def sound(self):
        return self._sound
animal = Animal("Dog","Brown","Gboo")
print(animal.name)
print(animal.complextion)
print(animal.sound)

