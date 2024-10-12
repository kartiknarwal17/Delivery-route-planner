import turtle
n=int(input("Enter the size of matrix:"))
j=0
turtle.pensize(2)
for k in range (n):
    for j in range (n):
        for i in range (4):
            turtle.forward(50)
            turtle.left(90)
        turtle.forward(50)
    turtle.backward(50+50*j)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
x=int(input("Enter x component of destination:"))
y=int(input("Enter y component of destination:"))
if y==n:
    turtle.forward(x*50)
else:
    turtle.right(90)
    turtle.forward((n-y)*50)
    turtle.left(90)
    turtle.forward(x*50)

x1=int(input("Enter x component of source:"))
y1=int(input("Enter y component of source:"))
if y1==y:
    turtle.backward((x-x1)*50)

else:
    turtle.backward((x-x1)*50)
    turtle.right(90)
    turtle.forward((y-y1)*50)
    turtle.left(90)

#if y1==n:
 #   turtle.forward((x-x1)*50)
#
#else:
 #   turtle.right(90)
  #  if x1!=0:
   #     turtle.forward((y-y1)*50)
    #turtle.left(90)
    #turtle.forward(x1*50)


# FIND SHORTEST PATH FROM SOURCE TO DESTINATION:

turtle.color('red')
turtle.pensize(4)
SD=input("To find the shortest distance, press 1: ")
print(" The red coloured path is the shortest route from source to destination")
if x<=x1 and y<=y1:
    if x1-x==0 and y1-y==0:
        turtle.dot(8)
        print("Source and destination are the same")
    else:
        turtle.dot(8)
        turtle.backward((x1-x)*50)
        if (y1-y)!=0:
            turtle.right(90)
        turtle.forward((y1-y)*50)
elif x==x1 and y>y1:
    turtle.dot(8)
    turtle.left(90)
    turtle.forward((y-y1)*50)
elif x>x1 and y==y1:
    turtle.dot(8)
    turtle.forward((x-x1)*50)
elif x>x1 and y>y1:
    turtle.dot(8)
    turtle.forward((x-x1)*50)
    turtle.left(90)
    turtle.forward((y-y1)*50)

elif x<x1 and y>y1 :
    turtle.dot(8)
    turtle.left(90)
    turtle.forward((y-y1)*50)
    turtle.left(90)
    turtle.forward((x1-x)*50)

elif x>x1 and y<y1:
    turtle.dot(8)
    turtle.forward((x-x1)*50)
    turtle.right(90)
    turtle.forward((y1-y)*50)

else:
    print("Invalid")

print("end")
