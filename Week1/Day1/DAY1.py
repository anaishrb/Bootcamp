# Exercice 1
print("Hello world\n" * 4, end="")

# Exercice 2
result = (99 ** 3) * 8
print(result)

# Exercice 4

computer_brand = "apple"
print(f"I have a {computer_brand} computer.")

# Exerice 5
my_name = "Anaïs"
my_age = 23
shoe_size = 38
info = f"My name is {my_name}, I am {my_age}, and my shoe size is {shoe_size}."
print(info)

# Exercice 6 
a = 5
b = 3
if a > b: 
    print("Hello World")

# Exerice 7

given_number = int(input("give me a number"))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
    
# Exercice 8

my_name = "Anaïs"
user_name = input("give me your name")
if user_name == my_name:
    print("We have the same name!")
else: 
    print("What a fun name")


# Exercice 9 

user_height = int(input('give me your height: '))
if user_height >= 145:
    print("You are tall enough, you can ride! ")
elif user_height < 145:
    print("You need to grow some more to ride...")


# Daily Challenge 

user_string = input("Please enter a string with exactly 10 characters: ")

if len(user_string) < 10:
    print("String not long enough")
elif len(user_string) > 10:
    print("String too long")
else:
    print("Perfect string")

print(f"First character: {user_string[0]}")
print(f"Last character: {user_string[-1]}")
for char in user_string:
    print(char)