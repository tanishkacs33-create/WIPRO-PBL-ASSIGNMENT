distance = float(input("How far would you like to travel in miles? "))
if distance < 3:
    transport = "Bicycle"
elif distance < 300:
    transport = "Motor - Cycle"
else:
    transport = "Super - Car"

print(f"I suggest {transport} to your destination")