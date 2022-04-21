from database import Database

if __name__ == "__main__":
    db = Database()
    db.connect()
    db.createTable()
    db.createNewClient('Samuel', 'loremipsumdolor', '0001010110', 'samuel@email.com')
    db.createNewClient('Foo', 'foobar12345', '100010101', 'foo@bar.com') 
    #db.showClient('100010101')
    #db.deleteClient('100010101')
    #db.showClientByEmail('samuel@email.com')
    login = db.login('samuel@email.com', 'asdas')
    print(login)
    db.disconnect()