import random

player_hp = 100
computer_hp = 100

while player_hp > 0 and computer_hp > 0:
    if player_hp > 0:
        print("Player choose your move")
        print("1) Hairpull")
        print("2) Round house kick")
        choice = input("Choice: ")
        print()

        if choice == "1":
            print("Player hair pulls the computer")
            computer_hp = computer_hp - random.randint(5,7)
        elif choice == "2":
            print("Player round house kicks the computer")
            computer_hp = computer_hp - random.randint(1,17)
        else:
            print("Player missed their go")

        print("Player HP: " + str(player_hp))
        print("Computer HP: " + str(computer_hp))
        print()

    if computer_hp > 0:
        print("Computer choose your move")
        print("1) Throw a byte")
        print("2) Shutdown")
        choice = random.randint(1,2)
        print()

        if choice == 1:
            print("Computer throws a byte at the player")
            player_hp = player_hp - random.randint(6,8)
        elif choice == 2:
            print("Computer shutdowns the player")
            player_hp = player_hp - random.randint(1,16)
        else:
            print("Computer missed their go")

        print("Player HP: " + str(player_hp))
        print("Computer HP: " + str(computer_hp))
        print()

if player_hp < 0:
    print("Computer wins!")
else:
    print("Player wins!")
