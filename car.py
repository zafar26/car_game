car_capacity = 30
travel = 100
petrol_pums = [10, 20,40, 60, 80]
refil = 20
shortcuts = [8, 17, 33, 56, 91]
traveled = 0
moved  = 0
i = 1

print("Game started \nPetrol pumps generated at 10, 20, 40, 60, 80 \nPits generated at 7, 22, 67 \nShortcuts generated at 8 (6 Steps forward), 17 (5 steps forward), 33 (7 steps backwards), 56 (6 steps forward), 91 (8 steps backward)")

while traveled < 100:
    print("MOVE",i)
    move = int(input("Car at: ")) 
    if move == 0 or move <= 6: 
        traveled = move + moved
        moved = traveled
        car_capacity = car_capacity - move
        if traveled in petrol_pums:
            car_capacity = car_capacity + refil
        if traveled in shortcuts:
            if traveled == 8:
                num = 6
            if traveled == 17:
                num = 5
            if traveled == 33:
                num = -7
            if traveled == 56:
                num = 6
            if traveled == 91:
                num = -8
            traveled = traveled + num
            moved = traveled
            print ("shortcut:",num)
            if traveled in petrol_pums:
                car_capacity = car_capacity + refil
        if traveled == 7 or traveled == 22 or traveled == 67:
            print("met with pitch, Game Over")
            break
        if traveled >= 100:
            print("Win")
            break
        if car_capacity <= 0:
            print("Fuel Over")
            break
        print("distance traveled:",traveled, end = '')
        print(", petrol remaining:",car_capacity)
    else:
        print("enter CORRECT steps")
    i = i+1