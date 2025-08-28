file = open("b5.jpg", "r")
try:
    with open("b5.jpg", "r") as file:
        data =  file.read()
except FileNotFoundError:
    print("File not found!. Please check the file well")