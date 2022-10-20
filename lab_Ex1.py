# A
print("Variables and their Data Type")
a = 3
b = 4.0
d = True
c = "Hello Python"
e = [4, 3.0, "Python mania", "Harry"]
f = {4, 3.0, "Python mania", "Harry"}
g = (4, 3.0, "Python mania", "Harry")
h = {"a":45,"Python":"language"}


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

#EXCHANGING VARIABLES

a, b = b, a
print(a,b)


#B
print("Arithmetic Operations")

a=10
b=5
sum=a+b
diff=a-b
mul=a*b
div=a/b
rem=a%b
pow=a**b
flr=a//b
expr=27 + 47 * 15 / 5 - 13 % 10
print("sum =", sum)
print("Difference =", diff)
print("Product =", mul)
print("Quotient =", div)
print("Remainder = ", rem)
print("Exponent = ", pow)
print("Floor Division = ", flr)
print("Expression Value = ", expr)