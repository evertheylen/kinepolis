#Auteur: Anthony Hermans

class Theater():
    def __init__(self, ID, places):
        self.ID = ID
        self.places = places

    def getID(self, ID):
        return self.ID

    def getPlaces(self):
        return self.places
    
    def __str__(self):
        return "Theater: [{}] places: {}".format(self.ID, self.places)
    
    def __repr__(self):
        return self.__str__()