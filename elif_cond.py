#To find entered year is leap year or not
year = int(input("Enter a year to find it's leap year or not:- "))

if year%400==0:
    print("it's a leap year")
elif year%100==0:
    print("it's a leap year")
elif year%4==0:
    print("it's a leap year")
else:
    print("It's not a leap year")