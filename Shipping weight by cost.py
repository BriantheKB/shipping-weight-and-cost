#ground shipping based on excel values
weight = 41.5

if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
elif weight >= 10:
  cost_ground = weight * 4.75 + 20
else:
  print("No cost associated with the weight")

print(cost_ground)

#ground shipping premium
cost_ground_shipping = 125.00

print(cost_ground_shipping)

#drone shipping
if weight <= 2:
  cost_drone = weight * 4.50 + 0
elif weight <= 6:
  cost_drone = weight * 9.00 + 0
elif weight <= 10:
  cost_drone = weight * 12.00 + 0
elif weight >= 10:
  cost_drone = weight * 14.25 + 0
else:
  print("No cost associated with the weight")

print(cost_drone)
