




class calisan:
    def __init__(self,name,surname,age):


        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):
         print(f"Ad:{self.name}  Soyad: {self.surname}   Yaş: {self.age}")


calisan1 = calisan("Ali","a",20)
print(calisan1.name,calisan1.surname,calisan1.age)

calisan2 = calisan("Ahmet","b",23)
print(calisan2.name,calisan2.surname,calisan2.age)

calisan1.show_info()
calisan2.show_info()