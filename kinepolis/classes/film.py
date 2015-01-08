class Film:
    def __init__(self, ID, title, rating):
        self.ID = ID
        self.title = title
        self.rating = rating
    
    def getID(self, ID):
        return self.ID
    
    def getTitle(self):
        return self.title
    
    def getRating(self):
        return self.rating
        
    def setRating(self, rating):
        self.rating = rating
    
    def setTitle(self, title):
        self.title = title
