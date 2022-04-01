weight = 41.5
ground_cost = ''
drone_cost = ''
# ground shipping
if weight <= 2:
  ground_cost= (weight * 1.50) + 20.00
elif (weight > 2) and (weight <= 6):
  ground_cost = (weight * 3.00) + 20.00
elif (weight > 6) and (weight <= 10):
  ground_cost = (weight * 4.00) + 20.00
elif weight > 10:
  ground_cost = (weight * 4.75) + 20.00
  #ground shipping premium has a flat fee
cost_ground_shipping_premium = 125.00
print('Your ground shipping cost is $' + str(ground_cost))
print('Ground shipping premium is a flat fee of $' + str(cost_ground_shipping_premium))
# Drone Shipping 
if weight <= 2:
  drone_cost = weight * 4.50
elif (weight > 2) and (weight <= 6):
  drone_cost = weight * 9.00
elif (weight > 6) and (weight <= 10):
  drone_cost = weight * 12.00
elif weight > 10:
  drone_cost = weight * 14.25
print('Your cost for drone shipping is $' + str(drone_cost))
