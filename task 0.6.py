def maximum_number(t,g,s):
    if (t>=g) and (t>=s):
        largest = t
    elif (g>=t) and (g>=s):
        largest = g
    else:
        largest = s
    return largest

print(maximum_number(2,78,45))