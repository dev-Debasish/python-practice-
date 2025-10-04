# def require_role(role):
#     def decorator(func):
#         def wrapper(self, *args, **kwargs):
#             if self.role != role:
#                 raise PermissionError(f"User with role '{self.role}' not allowed to call {func.__name__}. requires '{role}' ")
#             return func(self, *args, **kwargs)
#         return wrapper
#     return decorator

# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
        
#     @require_role('admin')
#     def delete_data(self):
#         return f"{self.name} delete the data"
    
#     @require_role('guest')
#     def view_data(self):
#         return f"{self.name} viewed the data"
    
# # test it
# admin = User("Bittu", "admin")
# guest = User("Deb", "guest")

# print(admin.delete_data())
# print(guest.view_data())

# # fail occur
# try:
#     print(guest.delete_data())
# except PermissionError as e:
#     print(e)
# try:
#     print(admin.view_data())
# except PermissionError as e:
#     print(e)
    
    
    
#! LET'S EXTENDS IT WITH ARGUMENTS 

def require_role(role):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if self.role != role:
                raise PermissionError(f"User with role '{self.role}' not allowed to call {func.__name__}")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    @require_role('admin')
    def delete_data(self, item):
        return f"{self.name} delete {item}"
    
# test it
admin = User("Bittu", "admin")
guest = User("Deb", "guest")

print(admin.delete_data("files"))  # works

try:
    print(guest.delete_data("files"))    # fails
except PermissionError as e:
    print(e)