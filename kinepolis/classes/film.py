class Film:
    def __init__(self, ID, title, rating):
        self.ID = ID
        self.title = title
        self.rating = rating
    
    def __str__(self):
        return "Film: [{}] {} ({})".format(self.ID, self.title, self.rating)
    
    def __repr__(self):
        return self.__str__()