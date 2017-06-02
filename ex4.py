cars=100
space_in_a_car=4
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
avg_passengers_per_car=passengers/cars_driven

print ("There are",cars,"cars available.")
print ("There are only",drivers,"drivers available")
print ("There will be",cars_not_driven,"cars not driven today")
print ("We can transport", carpool_capacity,"people today")
print ("We have",passengers,"to carpool today",end=" ") """Here i am using end thing just to get the 
output of last 2 lines of code in a single line."""
print ("We have to accomodate",avg_passengers_per_car,"people in a car")