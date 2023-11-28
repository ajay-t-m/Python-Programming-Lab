class publisher:
    def __init__(self,name1):
        self.name=name1
    # def show(self):
    #     pass

class book(publisher):
    def __init__(self,title1,author1,name1):
        self.title=title1
        self.author=author1
        publisher.__init__(self,name1)
    # def show(self):
    #     pass

class python(publisher):
    def __init__(self,prices,page,title1,author1,name1):
        self.price=prices
        self.pages=page
        book.__init__(self,title1,author1,name1)
    def show(self):
        print("Book Title:",self.title)
        print("Author:",self.author)
        print("Publisher:",self.name)
        print("Price: Rs",self.price)
        print("No of pages:",self.pages)

p1=python(700,300,'Python Programming','G V Rossum','ABC Books')
p1.show()