
"""
if angered::
    print("I want to rest early!")
"""

temperature = 60
if temperature<40:
    print("The heat is too much!!")
elif temperature>45:
    print("The temperature is moderate")
else:
    print("it is cooler")

grade = 25
if grade >= 90:
    print("I scored an A")
elif grade <= 80:
    print("My score is a B")
elif grade <=70:
    print("The score is a C")
elif grade <= 60:
    print("D it is!")
else:
    print("Worst!!.. an E!")


fruits = ["Mango", "Pineapple", "Cherry", "sWEETBERRY"]
for fruit in fruits:
    print(f"I really like {fruit}")

#some_strides = range(10)
# print(some_strides)

for number in range(45, 78):
    print(f"Number..: {number}")


count = 2 # Sets the starting value
while count <= 16:
    print(f"Count: {count}")
    count+=5 #Increments the counter

#Breaks in loops
#nested loops
for i in range(1, 7): #Outer Loop
    for j in range(1, 7): #Inner loop
        print(f"Outer loop: {i}, Inner loop: {j}")

#Functions in Python
#Defining and calling a function
def greet(name):
    #Greeting a person by name
    return f"Hi you.., {name}!"
#Function call
print(greet("Larry Muia"))