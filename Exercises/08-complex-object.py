class Address:
    def __init__(self):
        self.buildingAndStreet = ""
        self.townOrCity = ""
        self.postcode = ""
class Scientist:
    def __init__(self, name):
        self.name = name
        self.yearOfBirth = 0
        self.married = False
        self.fields = []
        self.address = Address()
    def printToScreen(self):
        """print all properties of object"""#docstring
        print("Name: " + self.name)
        print("Year of birth: " + str(self.yearOfBirth))
        print("Married: " + str(self.married))
        print("Fields: ")
        for field in self.fields:
            print("- " + field)
        # print("Address: " + 
        #     self.address.buildingAndStreet + ", " +
        #     self.address.townOrCity + ", " + 
        #     self.address.postcode)
        #with python3 placeholders
        print("Address: {}, {}, {}.".format( 
            self.address.buildingAndStreet,
            self.address.townOrCity, 
            self.address.postcode))

curie = Scientist("Marie Curie")
curie.yearOfBirth = 1867
curie.married = True
curie.fields.append("Physics")
curie.fields.append("Chemistry")
curie.fields.append("Radioactivity")
curie.address.buildingAndStreet = "Freta 16"
curie.address.townOrCity = "Warsaw"
curie.address.postcode = "00-227"
curie.printToScreen()

#with placeholders Python3: