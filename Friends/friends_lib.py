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

# it will tell if table of friends of this username exists or not
    def is_table_of_friends_exists(self, username):
        
        self.crs.execute('''show tables;''')

        all_tables = []  # will put all tables in database in this list

        for table in self.crs:
            all_tables.append(table[0])
        
        if(("friends_of_" + username) in all_tables):
            return True # user have table of friends
        else:
            return False # user don't have table of friends

# creating table of friends for this username 
    def create_table_of_friends(self, username):
        
        self.crs.execute(f'''create table friends_of_{username}(friends varchar(50));''')
        
# deleting table of friends of this username         
    def delete_table_of_friends(self, username):
        
        self.crs.execute(f'''drop table friends_of_{username};''')
        
# it will tell if table of requests of particular user exists or not
    def is_table_of_requests_exists(self, username):
        
        self.crs.execute('''show tables;''')
        
        all_tables = []
        
        for table in self.crs:
            all_tables.append(table[0])

        if(("requests_of_" + username) in all_tables):
            return True
        else:
            return False

# creating table of requests for this username        
    def create_table_of_requests(self, username):

        self.crs.execute(f'''create table requests_of_{username}(requests varchar(50));''')
        
# deleting table of requests of this username        
    def delete_table_of_requests(self, username):

        self.crs.execute(f'''drop table requests_of_{username}''')   

# will tell if request already exist or
    def if_friend_request_exist(self, sender, username):
        
        self.crs.execute(f'''select requests from requests_of_{sender};''')
        
        friends = []
    
        for friend in self.crs:
            friends.append(friend[0])
        
        if username in friends:
            return True
        else:
            return False
        
# retrieving friends of this username from table of friends
    def retrieve_friends(self, username):
        
        self.crs.execute(f'''select friends from friends_of_{username};''')
        
        friends = []
        
    
        for friend in self.crs:
            friends.append(friend[0])
       
            
        return friends
    
# retrieving friends list of this username
    def retrieve_requests(self, username):
        
        self.crs.execute(f'''select requests from requests_of_{username};''')
        
        requests = []
        
        for request in self.crs:
            requests.append(request[0])

        return requests
    
# checking whether user exists or not
    def if_username_exists(self, username):
        
        self.crs.execute(f'''select username from auth_user where username="{username}"''')

        users = []
        
        for user in self.crs:
            users.append(user[0])
        
        if users:
            return True
        else:
            return False
        
# sending friend-request
    def send_friend_request(self, sender, receiver):
        
        self.crs.execute(f'''insert into requests_of_{receiver} values("{sender}")''')
            
        
# rejecting friend-request
    def reject_friend_request(self, sender, receiver):
        
        self.crs.execute(f'''delete from requests_of_{receiver} where requests = "{sender}";''')

# after accepting friend request
    def friendship(self, sender, receiver):

        self.crs.execute(f'''delete from requests_of_{receiver} where requests = "{sender}";''')
        self.crs.execute(f'''insert into friends_of_{receiver} values("{sender}");''')
        self.crs.execute(f'''insert into friends_of_{sender} values("{receiver}");''')

# after removing friend    
    def end_friendship(self, friend1, friend2):
        
        self.crs.execute(f'''delete from friends_of_{friend1} where friends = "{friend2}";''')
        self.crs.execute(f'''delete from friends_of_{friend2} where friends = "{friend1}";''')

# checking if request already sent or not
    def if_request_already_sent(self, sender, receiver):
        
        self.crs.execute(f'''select * from requests_of_{receiver} where requests = "{sender}";''')

        requests = []
        
        for request in self.crs:
            requests.append(request[0])
            
        if requests:
            return True
        else:
            return False
        
# checking if they are already friend or not
    def if_already_friends(self, sender, receiver):
        
        self.crs.execute(f'''select * from friends_of_{receiver} where friends = "{sender}"''')
    
        friends = []
        
        for friend in self.crs:
            friends.append(friend[0])
            
        if friends:
            return True
        else:
            return False


# to get all users on website
    def all_users(self):
        
        self.crs.execute("select username from auth_user ;")
        all_users = []
        
        for user in self.crs:
            all_users.append(user[0])
        
        return all_users


# closing connection
    def close(self):
        self.hdl.close()
        
def main():

    database = Database()

if(__name__ == "__main__"):
    main()