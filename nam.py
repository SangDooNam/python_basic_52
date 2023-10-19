"""Task 1"""

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]


def user_validation(p_username, p_password, subject_lst = []):
    for user in users:
        if (p_username, p_password) == (user['name'], user['password']) and 'modules' in user:
            for subject in user['modules']:
                subject_lst.append(subject['title'])
            return subject_lst
            
        elif (p_username, p_password) == (user['name'], user['password']) and user['type'] == 'Teacher':
            return user['type']
    
    return False


def show_registration(p_username, p_password, p_modulename):
    
    authentication = user_validation(p_username, p_password)
    
    if authentication == 'Teacher':
        print('You are a teacher')
    elif not authentication:
        print(f'You did not register to the module {p_modulename}.')
    elif authentication and any(i == p_modulename for i in authentication):
        print(f'You are registered to the module {p_modulename}.')
    elif authentication and not any(i == p_modulename for i in authentication):
        print(f'You did not register to the module {p_modulename}.')
    

    
# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# modulename = input("What module do you want to check? ")
# show_registration(username, password, modulename)



"""Task 2"""

def student_teacher_anounymous(p_username, p_password, p_modulename):
    for user in users:
        if (p_username, p_password) == (user['name'], user['password']) and user['type'] == 'Student':
            for subject in user['modules']:
                if subject['title'] == p_modulename:
                    return subject['completed']
        elif (p_username, p_password) == (user['name'], user['password']) and user['type'] == 'Teacher':
            return user['type']
    
    return False


def has_completed_module(p_username, p_password, p_modulename):
    
    authentication = student_teacher_anounymous(p_username, p_password, p_modulename)
    
    if authentication == 'Teacher':
        return 
    elif authentication:
        print(f'You have completed the module {p_modulename}.')
    else:
        print(f'You did not complete the module {p_modulename}.')


# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# modulename = input("What module do you want to check? ")
# show_registration(username, password, modulename)
# has_completed_module(username, password, modulename)



"""Taks 3"""


modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
    }
]


def type_users(p_username, p_password, module_processes={} ):
    
    for user in users:
        if (p_username, p_password) == (user['name'], user['password']) and user['type'] == 'Student':
            for module_process in user['modules']:
                key = module_process['title']
                if not key in module_processes:
                    module_processes[key] = {}
                module_processes[key] = module_process['completed']
            return module_processes
        elif (p_username, p_password) == (user['name'], user['password']) and user['type'] == 'Teacher':
            return user['type']
        
    return 'Anonymous'


def requirement(p_modulename):
    
    for module in modules:
        if p_modulename == module['name'] and module['name'] == 'Computer basics':
            return 'no requirement'
        elif p_modulename == module['name'] and module['name'] == "Python basics":
            return module["requirement"]
        elif p_modulename == module['name'] and module['name'] == "Django":
            return module["requirement"]
    return 'no offer'


def no_requirement(p_username, p_password, p_modulename):
    
    if type_users(p_username, p_password) == 'Anonymous' and requirement(p_modulename) == 'no requirement':
        return True
    else:
        return False


def may_enroll(p_username, p_password, p_modulename):
    
    if no_requirement(p_username, p_password, p_modulename):
        return True
    elif not no_requirement(p_username, p_password, p_modulename):
        if type_users(p_username, p_password) == 'Teacher':
            return False
        elif isinstance(type_users(p_username, p_password), (dict)):
            for module, process in type_users(p_username, p_password).items():
                if module == requirement(p_modulename) and process == True and not p_modulename in type_users(p_username, p_password):
                    return True
                else:
                    return False


# def may_enroll(p_username, p_password, p_modulename):
    
#     if no_requirement(p_username, p_password, p_modulename):
#         return True
#     elif not no_requirement(p_username, p_password, p_modulename):
#         if type_users(p_username, p_password) == 'Teacher':
#             return False
#         elif isinstance(type_users(p_username, p_password), (dict)):
#             if 'Computer basics' in type_users(p_username, p_password) and requirement(p_modulename) == 'no requirement':
#                 return False
#             else:
#                 for module, process in type_users(p_username, p_password).items():
#                     if module == requirement(p_modulename) and process == True and not p_modulename in type_users(p_username, p_password):
#                         return True
#                     elif module == requirement(p_modulename) and process == False:
#                         return False


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)
if may_enroll(username, password, modulename):
    print(f"You may register to the module {modulename}.")
else:
    print(f"You may not register to the module {modulename}.")



