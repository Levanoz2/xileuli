fruits = ["pineapple","strawberry","watermelon"]

if "pineapple" in fruits:
    print("Do you really like pineapple?")
if "watermelon"in fruits:
    print("Do you really like watermelon?")
if "orange" in fruits: 
    print("Do you really like orange?")

#forloops

requested_toppings = ["extra peperoni","green peppers","extra marpejan"]

for requested_topping in requested_toppings:
    print("Adding "   +  requested_topping + ".")

print("\nFinished making your pizza")


for requested_topping in requested_toppings:
    if requested_topping == "extra peperoni":
        print("Sorry we are out of green peppers right now")
    else:
        print("adding ".title() + requested_topping+".")
print("\nFinished making your pizza")
requested_toppings = ["Pizza"]
if requested_toppings:
    print("Storage is not empty")
else:
    print("Storage is empty")

available_toppings = ["olives","green peppers","pepperoni","pineapple","extra peperoni"]
requested_toppings = ["extra peperoni","green peppers"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding ".title() + requested_topping+".")
    else:
        print("Sorry we dont have requested toppings")
print("\nFinished making your pizza")
