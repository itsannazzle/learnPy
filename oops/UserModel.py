
class UserModel:
    #unecessary

    def __init__(self,FirstName,MiddleName,LastName,Age):
        self.FirstName = FirstName
        self.MiddleName = MiddleName
        self.LastName = LastName
        self.Age = Age
    def validateUser(self):
        print(len(self.FirstName))
        return (len(self.FirstName) <0)
    def validateMiddleName(self):
        print(len(self.MiddleName))
        return (len(self.MiddleName) <0)
    