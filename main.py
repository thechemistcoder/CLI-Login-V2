import bcrypt
import sqlite3

class Databasemanager:
    def __init__(self):
        super().__init__
        self.con = sqlite3.connect('users.db')
        self.cursor = self.con.cursor()

    def verify(self, username, password):
        self.cursor.execute('SELECT Password FROM Users WHERE Username = ?', (username,))
        result = self.cursor.fetchone()
        if result:
            hashed_password = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                print('Login successful')
            else:
                print('Password incorrect')
        else:
            print('User not found')
    def register(self,Username,Password):
        hashed_password = bcrypt.hashpw(Password.encode('utf-8'), bcrypt.gensalt())
        self.cursor.execute('INSERT INTO Users VALUES(?,?)', (Username, hashed_password))
        self.con.commit()

while True:
    print('Welcome to Login System\n')

    print('Choose one of the following options\n')
    choice = input('1.Login\n2.Register\n3.Exit\n')
    match choice:
        case '1':
            Username = input('Username\n')
            Password = input('Password\n')
            hashedpassword = bcrypt.hashpw(Password, bcrypt.gensalt())
            db = Databasemanager()
            Databasemanager.verify(Username,Password)
            # if hashedpassword ==
        case '2':
            Username = input('Username\n')
            Password = input('Password\n')
            db = Databasemanager()
            db.register(Username,Password)
            print('Success User Registered')
        case '3':
            break




