import cmath  
a = int(input("a = "))  
b = int(input("b = "))  
c = int(input("c = "))  
d = b**2 - 4*a*c  
sol1 = (-b - cmath.sqrt(d)) / (2*a)  
sol2 = (-b + cmath.sqrt(d)) / (2*a)  
print("Solutions:" ,sol1,sol2)



# import cmath  
# # input a,b,c as int
# d =b**2-4*a*c  
# sol1=(-b-cmath.sqrt(d))/(2*a)  
# sol2=(-b+cmath.sqrt(d))/(2*a)  
# print("Ans:" ,sol1,sol2)