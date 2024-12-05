i = 3
m = 666
while m != 0:
    m = (m * 10 + 6) % 2023
    i += 1
print(i)
