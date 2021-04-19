x=0
y=1 
print(x)
print(y)
x = x + 3
y = y + x 

if x+3==0 and y+x==1:
    print(x)
else:
    print(y)


x = 1 + 1 *2
print(x)

y = (1+1)*2
print(y)

z = (1+(1*2))
print(z)

a = 1+1*2/2
print(a)

b = (1+1*2)/2
print(b)



def hello(name):
    print(f" hello {name}")

hello("Thapelo!")


def even_or_odd(i):
        if i%2==0:
            print("even")
        else:
            print("odd")

even_or_odd(27)


def triangle(b,h,a):
    a = (1/2) * (b*h)
    return a
print(triangle(4,6,1))


def maximum(t,g,s):
    if (t>=g) and (t>=s):
        largest = t
    elif (g>=t) and (g>=s):
        largest = g
    else:
        largest = s
    return largest

print(maximum(2,78,45))


def celcius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f
print(celcius_to_fahrenheit(41))



def fahrenheit_to_celcius(f):
    c = (f- 32) * 5/9
    return c
print(fahrenheit_to_celcius(108))


def time_conv(num):
    hours = num//60
    minutes = num%60
    print(hours,minutes)

time_conv(84)



def vowels(word):
    for letter in word:
        if (letter in "AaEeIiOoUu"):
            print(letter)

vowels("I like tomatoes")

#color1 = "red" 
#color2 = "green"
#color3 = "color1" + "color2"
#Char = "abcdefghijklmnopqrstuvwyz"

def common_letters(color1,color2):
    for r in color1:
        if r in color2:
            print(r, end=",")

common_letters("red","green")


