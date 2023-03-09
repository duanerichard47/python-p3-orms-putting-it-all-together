import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    def __init__(self, name, breed, id = None):    #instance with created without name and bread
        self.id = id
        self.name = name
        self.breed = breed

    all_dogs = []  
                                # table if first thing(second thing overall) after instance that is created. Can't add data before table created
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
        
        CURSOR.execute(sql,(self.name,self.breed))  #allows to read string as SQL commands and passes values into sql statement

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM dogs").fetchone()[0]  # after instance saved( we can't create an id database does when saved) grabbing the id created by database and adding it to the python created instance

    
    @classmethod
    def create(cls ,name, breed):           #3rd and 4th step. 1st row created. values created
        new_dog = Dog(name, breed)
        new_dog.save()                      #automatically called and values are added to table
        return new_dog

        
    @classmethod
    def new_from_db(cls, row):
        song = cls(row[1], row[2])
        song.id = row[0]
        return song
    
    @classmethod
    def get_all(cls):                # retrieving all data from table. All multiple rows
        sql = """
            SELECT *
            FROM dogs
        """
        all_dogs = CURSOR.execute(sql).fetchall()

        cls.all_dogs = [cls.new_from_db(row) for row in all_dogs]  #retrieves data row by row into list of dictionaries
        return cls.all_dogs


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
      
