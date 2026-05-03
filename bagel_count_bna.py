import math

people=9
needed=people*2
bags=math.ceil(needed/12)
tubs = bags*2
leftovers = (bags *12)-needed

print(f"Bags needed:{bags}")
print(f"Tubs needed:{tubs}")
print(f"Leftovers: {leftovers}")

print("---Extra credit: 13 per bag---")
extra_bags=math.ceil(needed/13)
extra_tubs=extra_bags*2
extra_left=(extra_bags*13)-needed
print(f"I'd need {extra_bags}bags(13 per bag).")
print(f"I'll need {extra_tubs} tubs of cream cheese.")
print(f"I'd have {extra_left} bagels left over.")
