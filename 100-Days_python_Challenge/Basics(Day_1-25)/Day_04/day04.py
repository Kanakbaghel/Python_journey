#Combining Operators in Expressions
result = (5 + 3) * 2 > 10 and not (3 == 4)
print(result) ##true

#Arithmetic operations
a = 10
b = 5

print(f'Addition: {a} + {b} = {a+b}')
print(f'Division: {a} / {b} = {a/b}')
print(f'Floor Division: {a} // {b} = {a//b}')
print(f'Modulus: {a} % {b} = {a%b}')
print(f'Exponentiation: {a} ** {b} = {a**b}')

#Comparison and logical operators
x = 4
y = 7

print(f'x > y: {x>y}')
print(f'x == y: {x==y}')
print(f'(x > y) and (y > 0): {(x>y) and (y>0)}')
print(f'not (x == y): {not (x == y)}')

#Assignment operators
count = 10
print(f'inital count: {count}')

count += 10
print(f'after += 10: {count}')

count *= 10
print(f'after *= 10: {count}')

count //= 10
print(f'After //= 10: {count}')

#Complex expression combining operators
a = 3
b = 7
c = 8

result = (a+b) * c > 20 or not (b == 2)
print(f'Result of expression: {result}')