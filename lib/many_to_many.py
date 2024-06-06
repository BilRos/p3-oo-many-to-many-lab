class Author:
    def __init__(self,name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self,book, date, royalties):
        contract =Contract(self,book,date,royalties)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    def __init__(self,title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all = []
    def __init__(self, author,book,date,royalties=0):
        if not isinstance(author, Author):
            raise Exception
        self.author = author
        if not isinstance(book, Book):
            raise Exception
        self.book = book
        if not isinstance(royalties, int):
            raise Exception
        self.royalties = royalties
        if not isinstance(date, str):
            raise Exception
        self.date = date
        Contract.all.append(self)
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    