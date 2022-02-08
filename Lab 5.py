# Kunal Shah
# Date 02/08/2022

# Problem 1
# Initial value
i = 0
print("Hello World!")

# while loop run till i is less than or equal to 100
while(i <= 100):
    print("Hello World!")
    # Increment i = i + 1
    i += 1

# Problem 2

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
print("Part 1")

# (a) : numbers
# i will iterate through each element of list

for i in numbers:
    print(i)

print("Part 2")

# (b) : numbers and squares
# i will iterate through each element of list

for i in numbers:
    # i * i will give square of i
    print(i, " : ", i * i)

# Problem 3

# imports Turtle
import turtle

# sets background screen
wn = turtle.Screen()  
alex = turtle.Turtle()
 
# input for side number, length, line color, and fill color
sides = input ("Number of sides in polygon?"  )
length = input ("Length of the sides in polygon?" )
colorname = input ("Color of polygon?" )
fcolor = input ("Fill color of polygon?")
 
alex.color = (colorname)
alex.fillcolor = (fcolor)

# creates a shape drawing loop with user-defined parameters 
for i in range(int(sides)):
   alex.forward (int(length))
   alex.left (int(360)/int(sides))



# Problem 4

# variable q
q = 1
#while loop
while q <= 50:
    #checking if q is divisible by 3 and 5
    #when q is divisible by 3 and 5
    if q % 3 == 0 and q % 5 == 0:
        print("Divisible by both")

    #checking if q is divisible by 3
    #when q is divisible by 3
    elif q % 3 == 0:
        print("Divisible by three")

    #checking if q is divisible by 5
    #when q is divisible by 5
    elif q % 5 == 0:
        print("Divisible by five")
    #when number is not divisible by 3 or 5
    else:
        print(q) 
    q=q+1#increment q


# Problem 5

# Importing Turtle
import turtle as t

g = 100

#Creates shape with the following parameter using for loop
for i in range(8):
    t.forward(g)
    t.right(135)


    
