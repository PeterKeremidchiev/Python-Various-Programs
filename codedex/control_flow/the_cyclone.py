
height = int(input("Whats your height in cm? "))
credits = int(input("How much credits you have? "))

# if height >= 137 and credits >= 10:
#   print("Enjoy the ride!")
# elif credits >= 10 and height < 137:
#   print("You are not tall enough to ride.")
# elif height >= 137 and credits < 10:
#   print("You don't have enough credits.")
# else:
#   print("You are not tall enough and dont have credits!")

#bonus


is_rolercoaster_open = True
is_tall_enough = height >= 137
have_credits = credits >= 10

if is_rolercoaster_open and is_tall_enough and have_credits:
  print("Enjoy you ride!")
elif not is_tall_enough or not have_credits:
  print("You dont meet the requirements!")
else:
  print("The rolercoaster is closed!")
