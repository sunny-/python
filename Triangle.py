# Identify types of triangles
# isosceles, equilateral, scalene or right angled triangle
a=10
b=6
c=10
if a==b==c:
    print('Equilateral')

elif a==b or b==c or a==c:
    print('Isosceles')

elif (a**2+b**2)==c**2 or (a**2+c**2)==b**2 or (b**2+c**2)==a**2:
    print('Right angled')

else:
    print('Scalene')
