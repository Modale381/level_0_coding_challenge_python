def time_conv(num):
    hours = num // 60
    minutes = num % 60
    return (hours,minutes)

print(time_conv(84))
