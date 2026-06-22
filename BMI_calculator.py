print("BMI Calculator")
a=int(input("Enter you Height:"))
a=a/100
b=int(input("Enter you Weight:"))
c=b/(a*a)
if c<18.5:
    print("Under Weight")
elif (c==18.5 or c>18.5) and (c==24.9 or c<24.9):
    print("Healthy Weight")  
elif (c==25 or c>25) and (c==29.9 or c<29.9):
    print("Over Weight")  
elif (c>30 or c==30) and (c<34.5 or c==34.5):
    print("Obesity(class 1)")
elif (c>35.0 or c==35.0) and (c<39.9 or c==39.9):
    print("Obesity(class 2)")
elif c==40 or c>40:
    print("Extreme Obesity")