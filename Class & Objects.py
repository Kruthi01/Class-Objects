'''
1. Class called circle with constructor which will take a list as an argument
'''
class circle:
#constructor     
    def __init__(self):
        self.n1=[10,501,22,37,100,999,87,351]
    def dis(self):
        print("1. The list is:", self.n1)
if __name__=="__main__":
#assigning class to an variable
    onj=circle()
#calling method via class
    onj.dis()

'''
2. Create a member variable PI and use it whereever necessary
'''
class circle:
#Initializing private member variable for class circle 
    __pi=3.14
    def __init__(self,radius):
        self.radius=radius
#calc circle and returning a value
    def a_circle(self):
        a=self.__pi*self.radius*self.radius
        return a
#calc perimeter and returning a value    
    def disp(self):
        b=self.__pi
        return b

if __name__=="__main__":
    circle=circle(4)
#printing them respectively
    print("2. Calc of circle:",circle.a_circle())
    print("The Pi value is:",circle.disp())

'''
3. From the given list, create 2 class methods circle and perimeter and calc the same
'''
class circle:
    __pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area_of_circle(self):
        area=self.__pi*self.radius*self.radius
        return area
    def area_of_Perimeter(self):
        peri=2*self.__pi*self.radius
        return peri
if __name__=="__main__":
    circle=circle(4)
    print("3. Area of Circle:",circle.area_of_circle())
    print("Area of Perimeter:",circle.area_of_Perimeter())


