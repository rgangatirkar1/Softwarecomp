print("Enter a positive integer:")
x = input()
y = int(x)
abs(y)
if y%7 == 0 and y%3 == 0:
    print("TechOlympics")
elif y%7 == 0:
    print("Olympics")
elif y%3 == 0:
    print("Tech")
else:
    print("Have a good day")
