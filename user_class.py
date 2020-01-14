# importing the data fine
from data import user_data, ROLES


# function to check the privilages of each function
def privilage(funct, obj):  # takes 2 arguments function name and the object
    if (obj.role == 'admin'):  # checking for admin role
        return True
    elif funct in ROLES['role_priviledges'][obj.role]['allowed']:  # checking for moderator role
        return True
    else:
        return False


# creating the parent userclass
class UserClass:

    def __init__(self, id, name, password, role, desc):
        
        self.id = id
        self.name = name
        self.password = password
        self.role = role
        self.desc = desc

   # function to get info about individual object
    def get_user_info(self, obj):
        if privilage('get_user_info', self):
            for user in user_data:
                if user['id'] == obj.id:
                    print(obj.id, obj.name, obj.password, obj.role, obj.desc)
                    break
            else:
                print('user does not exist')
        else:
            print('operation not allowed')

    # function to get no. of users
    def user_count(self):
        if privilage('user_count', self):
           print(len(user_data))
        else:
            print('operation not allowed')

    # function for no of users with a particular role
    def role_based_user_count(self, role):
        if privilage('role_based_user_count', self):
            count = 0
            for user in user_data:
                if user['role'] == role:
                    count += 1
            print(count)
        else:
            print('operation not allowed')

    # function to retrieve a user's role
    def get_user_role(self, obj):
        if privilage('get_user_role', self):
            print(obj.role)
        else:
            print('operation not allowed')


# creating a child class
class UserActionClass(UserClass):

    # function to add a new user
    def add_user(self, obj):
        if privilage('add_user', self):
            newuser = obj.__dict__
            user_data.append(newuser)
        else:
            print('operation not allowed')

    # function to edit user's data
    def edit_user(self, obj, key, value):
        if privilage('edit_user', self):
            for user in user_data:
                if user['id'] == obj.id:
                    user[key] = value
                    break
            else:
                print('user does not exist')
        else:
            print('operation not allowed')

    # function to change existing user's role
    def set_user_role(self, obj, role):
        if privilage('set_user_role', self):
            print('valid')
            for i in user_data:
                if i['id'] == obj.i_d:
                    i['role'] = role
        else:
            print('not valid')

    # function to delete an existing user
    def delete_user(self, obj):
        if privilage('delete_user', self):
            for user in user_data:
                if user['id'] == obj.id:
                    user.clear()
        else:
            print('not valid')

#creating a list of objects
ob = []

for user in user_data:
    ob.append(UserActionClass(user['id'], user['name'], user['pass'], user['role'], user['desc']))


#clent

user_input = int(input('enter 1 for user info \n'
                       'enter 2 for user count \n'
                       'enter 3 for role based count\n'
                       'enter 4 for get user role \n'
                       'enter 5 for add user\n'
                       'enter 6 for edit user\n'
                       'enter 7 for set role\n'
                       'enter 8 for delete role\n'))
if user_input == 1:
    ob[3].get_user_info(ob[6])
elif user_input == 2:
    ob[3].user_count()
elif user_input == 3:
    ob[3].role_based_user_count('admin')
elif user_input == 4:
    ob[3].get_user_role(ob[1])
elif user_input == 5:
    print(user_data)
    ob[3].add_user(ob[1])
    print(user_data)
elif user_input == 6:
    print(user_data)
    ob[3].edit_user(ob[0], 'name', 'zinnov')
    print(user_data)
elif user_input == 7:
    print(user_data)
    ob[3].set_user_role(ob[2], 'moderator')
    print(user_data)
elif user_input == 8:
    print(user_data)
    ob[3].delete_user(ob[1])
    print(user_data)
else:
    print('enter valid input')
