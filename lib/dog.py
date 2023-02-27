import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    def __init__(self, name, breed, id = None):
        self.id = id
        self.name = name
        self.breed = breed
        
    @classmethod                #class method not instance method. Want class creating table so all methods would be able to too
    def create_table(cls):          #lab specifically asks to create instance dogs
        sql = """
            CREATE TABLE IF NOT EXISTS dogs       
                (id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT)
        """
        CURSOR.execute(sql)     #allows to read string as SQL commands

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS dogs
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO dogs (name, breed)
            VALUES (?, ?)
        """
        CURSOR.execute(sql)

    # def create(self,name, breed):
    #     self = Dog(name, breed)
    #     self.save()
    #     return self

    #     CURSOR.execute(sql)

    # def new_from_db(cls, row):
    #     song = cls(row[1], row[2])
    #     song.id = row[0]
    #     return song
    
    # def get_all(self):
    #     sql = """
    #         SELECT *
    #         FROM self
    #     """
   


    # def find_by_name(self):
    #     sql = """
    #         SELECT name
    #         FROM self
    #     """

      

    # def find_by_id(self):
    #     sql = """
    #         SELECT id
    #         FROM self
    #     """

    # def update(self):
    #     sql="""
    #         UPDATE self SET name = "" 
    #         WHERE name = ""
    #     """
      
