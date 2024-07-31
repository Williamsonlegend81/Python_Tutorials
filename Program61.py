class Names:
    def __init__(self,name,city):
        self._name = name
        self._city = city
    @property
    def Name_details(self):
        print(f"{self._name} lives in {self._city}")
        l  = [self._name,self._city]
        return l
    @Name_details.setter
    def Name_details(self,l):
        print(f"Your name is changed from {self._name} to {l[0]}")
        self._name = l[0]
        print(f"Your city name is changed from {self._city} to {l[1]}")
        self._city = l[1]

details = Names("Genos","City Z")
print(details.Name_details)
details.Name_details = ["Saitama","City A"]