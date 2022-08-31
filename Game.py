import random

player_hp = 100
computer_hp = 100

print ("What is your name")
player_name = input("Name: ")

print ("Hello " + player_name + " would you like to play a game")
print ("1) Yes")
print ("2) No I don't play games")
choice = input("Choice: ")
if choice == "1":
    print ("Excellent, let's find you an opponent")
elif choice == "2":
    print ("You disappoint me, we are going to play anyway")
print()

#Picking an opponent
print ("Selecting Opponent")
choice = random.randint(1,2)
if choice == 1:
    computer_name = "Lazarus"
    computer_hp = 25
elif choice == 2:
    computer_name = "Cozy Bear"
    computer_hp = 50
print()

while player_hp > 0 and computer_hp > 0:
    if player_hp > 0:
        print(player_name + " choose your move")
        print("1) Punch")
        print("2) Round house kick")
        choice = input("Choice: ")
        print()

        if choice == "1":
            print(player_name + " punches the "+ computer_name)
            computer_hp = computer_hp - random.randint(5,7)
        elif choice == "2":
            print(player_name + " round house kicks "+ computer_name)
            computer_hp = computer_hp - random.randint(1,17)
        else:
            print(player_name + "was lazy and missed their go")

        print(player_name + " Health: " + str(player_hp))
        print(computer_name + "Health: " + str(computer_hp))
        print()

    if computer_hp > 0:
        print(computer_name + " choose your move")
        print("1) Throw a byte")
        print("2) Shutdown")
        choice = random.randint(1,2)
        print()

        if choice == 1:
            print(computer_name + " throws a byte at " + player_name)
            player_hp = player_hp - random.randint(6,8)
        elif choice == 2:
            print(computer_name + " shutdowns "+ player_name)
            player_hp = player_hp - random.randint(1,16)
        else:
            print(computer_name + " missed their go")

        print(player_name + " HP: " + str(player_hp))
        print(computer_name + " HP: " + str(computer_hp))
        print()

if player_hp < 0:
    print(computer_name + " wins!")
else:
    print( player_name + " proves that " + computer_name " was not worthy")
