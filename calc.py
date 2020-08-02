def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
print('''
Choose The Option:
1. Addition
2. Subtract
3. Multiply
4. Divide
''')
print("Enrter the Option for Operation :\n")
option = int(input())
n1=int(input("Enter the First Number :\n"))
n2=int(input("Enter the Second Number :\n"))
print("The Value is :)")
if(option == 1):
    print(add(n1,n2))
elif(option ==2):
    print(sub(n1,n2))
elif(option ==3):
    print(mul(n1,n2))
elif(option ==4):
    print(div(n1,n2))
else:
    print("OUT OF OPTION :(")
