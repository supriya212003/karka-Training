

# print(s)
# from math import sqrt
def heron():
    side_a=int(input("Enter the side a value:"))
    side_b=int(input("Enter the side b value:"))
    side_c=int(input("Enter the side c value:"))
    s=int((side_a+side_b+side_c)/2)
    n=(s*(s-side_a)*(s-side_b)*(s-side_c))
    return sqrt(n)




# #triangle area
 
def area():
    side_a=int(input("Enter the side a value:"))

    return side_a*side_a
  



# #square area

def rect():
    length=int(input("Enter the length:"))
    breadth=int(input("Enter the breadth"))
    return length*breadth
# rect_area=rect(length,breadth)
# print(rect_area)



# #rectangle area
# radius=int(input("Enter the radius:"))
def circle():
    radius=int(input("Enter the radius:"))
    return 3.14*radius*radius
# circle_area=circle(radius)
# print(circle_area)



# #circle area
#  base_a=int(input("Enter the base a:"))
#  base_b=int(input("Enter the base b:"))
#  height=int(input("Enter the height:"))
def trapezium():
    base_a=int(input("Enter the base a:"))
    base_b=int(input("Enter the base b:"))
    height=int(input("Enter the height:"))
    return ((base_a+base_b)/2)*height
# area=trapezium(base_a,base_b,height)
# print(area)



n=input("Enter the input number")
if n=='1':
    print(heron())
if n=='2':
    print(area())
if n=='3':
    print(rect())
if n=='4':
    print(circle())
if n=='5':
    print(trapezium())