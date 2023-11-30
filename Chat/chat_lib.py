import mysql.connector as mc

class Database:

    def __init__(self, host = "localhost", user = "root", password = "root", database = "credentials", autocommit = True):
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.autocommit = autocommit
        self.hdl = mc.connect(host = self.host, user = self.user, password = self.password, database = self.database, autocommit = self.autocommit)
        self.crs = self.hdl.cursor()

    def push(self, message):
         
        self.crs.execute(f'''insert into messages values("{message}");''')
        
    def push_dm(self, message,message_table):
         
        self.crs.execute(f'''insert into {message_table} values("{message}");''')

    def pull(self):
        
        self.crs.execute(f'''select * from messages;''')
        record_list = []
        
        for data in self.crs:
            record_list.append(list(data))

        return record_list
    
    def pull_dm(self, message_table):
        
        self.crs.execute(f'''select * from {message_table};''')
        record_list = []
        
        for data in self.crs:
            record_list.append(list(data))

        return record_list
    
    def reset_chat(self):
        
        self.crs.execute(f'''delete from messages;''')
        
    def reset_chat_dm(self, message_table):
        
        self.crs.execute(f'''delete from {message_table};''')
    
# creating table for every 2 person to chat directly
    def create_table(self,message_table):
        
        self.crs.execute(f'''create table {message_table}(messages varchar(500));''')
    
    
    
    
# closing connection 
    def close(self):
        self.hdl.close()
    
def main():
    
    database = Database()

    record_list = database.pull()
    print(record_list)

if(__name__ == "__main__"):
    main()