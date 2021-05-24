def calculate_square(mylist):
    squares=[n**2 for n in mylist]
    return squares

def calculate_cube(mylist):
    cube=[n**3 for n in mylist]
    return cube

def calculate_4(mylist):
    fourth=[n**4 for n in mylist]
    return fourth

def calculate_5(mylist):
    five=[n**5 for n in mylist]
    return five

print(calculate_square([2,4,8,16]))
print(calculate_cube([2,4,8,16]))