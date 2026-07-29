class cricket:
    def __init__ (self, score, sport):
        self.score = score
        self.__sport = sport
    def ball(self):
        print("Hey, this is a cricket ball!")

    def access(self):
        print (f"This sport is {self.__sport}")


class football:
    def __init__(self,score):
        self.score = score
    def ball(self):
        print("Hey, this is a football!")


cric1 = cricket(4,"cricket")
foot1 = football(5)
cric1.ball()
cric1.access()