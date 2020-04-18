a = 5
b = 0

try:
    print("Resource Open")
    print(a/b)

except Exception as e:
    print("Something Went Wrong: ",e)

finally:
    print("Resource Closed")