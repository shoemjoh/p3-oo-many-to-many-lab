class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.add_to_all(self)

    @classmethod
    def add_to_all(cls, author):
        cls.all.append(author)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.author]
    
    def books(self):
       return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        total = 0
        contract_list = self.contracts()
        for contract in contract_list:
            total = total + contract.royalties
        return total
       


class Book:
    all = []
    
    def __init__(self, title):
        self.title = title
        Book.add_to_all(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.book]

    def authors(self):
        return [contract.author for contract in Contract.all if self == contract.book]

    @classmethod
    def add_to_all(cls, book):
        cls.all.append(book)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.royalties = royalties
        if not isinstance(royalties, int):
            raise Exception
        self.royalties = royalties

        if not isinstance(date, str):
            raise Exception
        self.date = date

        if (Contract.is_book(book)):
            self.book = book
        else:
            print(f"{book} is not a book.")
        
        if (Contract.is_author(author)):
            self.author = author
        else:
            print(f"{author} is not an author.")
        
        Contract.add_to_all(self)

    @classmethod
    def is_author(cls, author):
        if (isinstance(author, Author)):
            return True
        else:
            raise Exception

    @classmethod
    def is_book(cls, book):
        if (isinstance(book, Book)):
            return True
        else:
            raise Exception

    @classmethod
    def add_to_all(cls, contract):
        cls.all.append(contract)
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in Contract.all if date == contract.date]


