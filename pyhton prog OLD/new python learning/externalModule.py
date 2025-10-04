# import pyttsx3
# engine = pyttsx3.init()
# engine.say("hello debasish! how are you")
# engine.runAndWait()

import os

# Select the directory whose content you want to list
directory_path = "/Users/asus/Videos/English Movies"

# use the os module to list the directory contents
content = os.listdir(directory_path)

# print the contents of the directory
for item in content:
    print(item)

# import os

# def list_directory_contents(path):
#     for item in os.listdir(path):
#         print(item)

# # Example usage
# directory_path = '/'  # Replace with your desired directory path
# list_directory_contents(directory_path)
