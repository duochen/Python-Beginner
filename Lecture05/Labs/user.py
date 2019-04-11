class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):        
        print(self.first_name, self.last_name)

    def greet_user(self):
        print("Hello " + self.first_name + "," + self.last_name)        

user1 = User("Duo", "Chen")    
user2 = User("Jie", "Lin")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super(Admin, self).__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        self.privileges.show_privileges()

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

privileges = Privileges(["can add post", "can delete post"])
admin = Admin("Lillian", "Chen", privileges )        
admin.show_privileges()