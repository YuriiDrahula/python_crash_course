# Aline color exercises
alien_color = "green"
if alien_color == "green":
    print("You've just earned 5 points!")

if alien_color != "green":
    print("Failed")

alien_color = "red"
if alien_color == "green":
    print("You've just earned 5 points!")
elif alien_color == "yellow":
    print("You've just earned 10 points!")
elif alien_color == "red":
    print("You've just earned 15 points!")
else:
    print("You've just earned 2 points!")


