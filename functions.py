def hello():
    print("This is my first function")
hello()

def calculate():
    x=5
    y=3
    print(x*y)
calculate()

def majina(fname,lname):
    print(fname+" "+lname)
majina("Eric","Were")
majina("Manvin","Chager")
majina("Victor","Muthombi")
majina("Ashley","Nelima")

def greetings(name,greeting="Hello"):
    print(greeting+ " "+name)
greetings("Eric")
greetings("Niaje","Joan")

#MY OWN
def orders(name,order="would you like a Vanilla latte?"):
    print(name+","+order)
orders("Manvin")
orders("Paul")

def ages(name,age="how old are you"):
    print(name+","+age)
ages("Manvin")


def maxvalu(a, b, c, d, e, f):
    return max(a, b, c, d, e, f)
result=maxvalu(7, 9, 1, 8, 17, 45)
print(result)

def minvalu(a, b, c, d, e, f):
    return min(a, b, c, d, e, f)
result=minvalu(2, -5, 34, 100, 30,1)
print(result)

def sort_list(lst):
    return sorted(lst)
answer=sort_list([3,6,9,12,15,11])
print(answer)

def sort_list(lst):
    return sorted(lst)
answer=sort_list([10045,6089,35657,79880])
print(answer)

def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(5)

def print_number(n):
    for m in range(n):
        print(m)
print_numbers(10)


