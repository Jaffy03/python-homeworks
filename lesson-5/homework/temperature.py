def convert_cel_to_far(cel):
    return cel*9/5 +32

def convert_far_to_cel(far):
    return (far-32)*5/9

try:
    far=float(input("Enter a temperature in degrees F: "))
    print(f"{far} degrees F= {convert_far_to_cel(far):.2f} degrees C")
    
    cel=float(input("Enter a temperature in degrees C: "))
    print(f"{cel} degrees C= {convert_cel_to_far(cel):.2f} degrees F")

except:
    print("Not a valid data type is entered")    