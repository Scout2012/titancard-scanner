import sqlite3

# begin class MyDatabase()
class MyDatabase():
    def __init__(self):
        self.mConnection = sqlite3.connect("csuf.db")

        # for now, creates the table for the club 'acmw'
        # more will be added
        self.mConnection.cursor().execute("CREATE TABLE IF NOT EXISTS acmw(Name,TCID,CWID)")
        
    # the following three methods()
    # - adds a person to the database (club specific OR all)
    # - removes a person from a particular club OR all
    # - checks if the person is in the database (at least in one club) using the supplied name or id

    # def subscribePersonWithClub(self, person, club):
    def subscribePerson(self, person):
        cursor = self.mConnection.cursor()
        if type(person) is list:
            cursor.executemany("INSERT INTO acmw VALUES (?,?,?)", person)
        if type(person) is tuple:
            cursor.execute("INSERT INTO acmw VALUES (?,?,?)", person)
    
    # def unsubscribePersonFromClub:
    def unsubscribePerson(self, name):
        cursor = self.mConnection.cursor()
        cursor.execute("DELETE FROM acmw WHERE Name=(?)", (name,))

    def isPersonSignedUp(self, name):
        cursor = self.mConnection.cursor()
        cursor.execute("SELECT * FROM acmw WHERE Name=(?)", (name,))
        data = cursor.fetchone()
        if not data:
            return False
        else:
            return True
    


    # the following three methods()
    # - places a 'marker' next the person to indicate the person is signed in to a particular club
    # - removes a 'marker' next the person to indicate the person is singed out from the particular club
    # - checks if a 'marker' is next to the person in a particular club
    # def signPersonIn(self):
    #     pass
    # def signPersonOut(self):
    #     pass
    # def isPersonSignedIn(self):
    #     pass
    
    def status(self):
        cursor = self.mConnection.cursor()
        for row in cursor.execute("SELECT * FROM acmw"):
            print(row)
# end class MyDatabase()

def version():
    return 1.0

