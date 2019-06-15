# call in the import module/library
from sys import argv

# list arguments that need to be given when invoking the script: in this case, the script name and user name.
script, user_name, college = argv

# This shows what character will be on the screen when introducing the prompt entry field.
prompt = '*'

# print statements and give prompt for user to enter/answer
print(f"Hi {user_name} from {college}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# Display final text with given prompt answers
# you can insert variables within blocks by just adding the (f"""
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is. 
And you have a {computer} computer. Nice. 
""")
