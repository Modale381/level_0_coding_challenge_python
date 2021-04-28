def common_letters(color1,color2):
    for r in color1:
            if r in color2:
                print(r, end=",")

common_letters("red","green")
