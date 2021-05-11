class train:
    def __init__(self,no,from_,to_,departure):
        self.passenger=[]
        self.no=no
        self.from_=from_
        self.to_=to_
        self.departure=departure
        self.lb=1
        self.ub=1
        self.mb=1
        self.latest=0
        
    def book(self):
        self.latest+=1
        