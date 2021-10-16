class get_sides:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
class Area(get_sides):
    def area(self):
        s = (self.a + self.b + self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
obj=Area(a,b,c)
ans=obj.area()
print("Area of triangle: {:.2f} sq.units".format(ans))
