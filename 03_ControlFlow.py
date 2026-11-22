## IF ELSE

temparature = 30

if temparature > 25:
    print("It's hot")
else:
    print("It's cold")


# elif conditions
if temparature >= 30:
    print("It's very hot")
elif temparature >= 25:
    print("It's hot")
else:
    print("It's cold")

#multiple conditions

age = 20
has_license = True
if age >= 18 and has_license:
    print("You can drive")
elif age >= 18 and not has_license:
    print("You need a license to drive")
else:
    print("You are not old enough to drive")

## LOOPS

for i in range(5):
    print(f"Iteration {i}")

for i in range(1, 6):
    print(i)

#count with steps of 2
for i in range(1,10,2):
    print(i)