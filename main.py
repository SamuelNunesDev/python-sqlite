from database import Database

if __name__ == "__main__":
    db = Database()
    db.connect()
    db.createTable()
    #db.createNewClient('Samuel', '0001010110', 'samuel@email.com')
    #db.createNewClient('Foo', '100010101', 'foo@bar.com') 
    #db.showClient('100010101')
    db.deleteClient('100010101')
    db.disconnect()