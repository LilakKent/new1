#This is first part of HW
cities = input("Enter the cities where you have been the last 10 years: ").title().split()
wish = input("Where do you want to go in the next 10 years? ").title().split()
repeats = set(cities).intersection(set(wish))
if repeats:
    print(f'maybe you really liked these cities: {", ".join(repeats)}')
else:
    print(f'maybe you are open to something new?')
-------------------------------------------------------------------------------------------------------------
#This is second part of HW
vehicle_description = {
    "model": "Camry Elegance+",
    "type": "sedan",
    "color": ["white", "black", "silver", "brown", "blue", "red"],
    "hp": 175,
    "length": 4885,
    "width": 1840,
    "height": 1445,
    "wheelbase": 2825,
    "front track width": 1590,
    "rear track width": 1610,
    "overhang ahead": 975,
    "overhang behind": 1085,
    "front electric motor(max_power)": 88
}