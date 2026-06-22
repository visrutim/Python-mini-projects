print("Temperatur Converter")
print("1.Celsius <-> Kelvin")
print("2.Fahrenheit <-> Celcius")
print("3.Fahrenheit <-> Kelvin")
a=int(input("Enter Your choice:"))
match a:
    case 1:
        print("1.Celsius to Kelvin")
        print("2.Kelvin to Celsius")
        b=int(input("Enter:"))
        if b==1:
            c=float(input("Enter Celsius:"))
            k=c+273
            print("Celsius:",k)
        if b==2:
            k=float(input("Enter Kelvin:"))
            c=k-273
            print("Celsius",c)
    case 2:
        print("1.Fahrenheit to Celsius")
        print("2.Celsius to Fahrenheit")
        b=int(input("Enter:"))
        if b==1:
            f=float(input("Enter Fahrenheit:"))
            c=(f-32)*5/9
            print("Celsius:",c)
        if b==2:
            c=float(input("Enter Celsius:"))
            f=(c*9/5)+32
            print("Fahrenheit:",f)
    case 3:
        print("1.Fahrenheit to Kelvin")
        print("2.Kelvin to Fahrenheit")
        b=int(input("Enter:"))
        if b==1:
            f=float(input("Enter Fahrenheit:"))
            k=(f+459.67)*5/9
            print("Kelvin:",k)
        if b==2:
            k=float(input("Enter Kelvin:"))
            f=(9/5*k)-459.67
            print("Fahrenheit:",f)
                                


        
