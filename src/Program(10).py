from math import sqrt

#Calucate curved surface area, total area, volume AND slant height of cone

PI = 22 / 7

isLgiven =  input("Is the slant height given y/n? ")
r = int(input("Enter the radius of the cone(r): "))
if input == 'n':
    h = int(input("Enter the height of the cone(h): "))
    l = sqrt(h**2 + r**2)
else:
    l = int(input("Enter the slant height(l): "))
    h = sqrt(l**2 - r**2)

CSA = PI * r * l
TSA = PI * r * (r + l)
V = 1/3 * PI * r**2 * h
print (f"""Curved surface area: {CSA}
Total surface area: {TSA}
Volume: {V}""")

print(r**2)
print(h)