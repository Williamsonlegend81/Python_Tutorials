class Library:
    def __init__(self,bookname):
        list1 = [bookname]
        self.name = list1   
        self.no_of_book = len(self.name)
    def add(self,newbook):
        # length = len(self.name)
        list2 = self.name
        list2.append(newbook)
        self.name = list2
        # length2 = len(self.name)
        print(f"Total books in library is updated from {int(len(list2)-1)} to {int(len(list2))}")
    def Showall(self):
        for index,i in enumerate(self.name,start=1):
            print(index,i)
        print(f"Library has {len(self.name)} books")

book = Library("Harry Potter")
book.add("Lord of Rings")
book.add("Dark Matter")
book.add("Sherlock Holmes")
book.add("Ikigai")
book.Showall()
b = Library("Vachnamrut")
b.add("Bhaktchintamani")
b.Showall()
