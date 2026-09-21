# A program stores the activities that occur monthly at a gym. Here is an extract from the program.
# Construct an algorithm to count how many Pilates classes there are during the month. 
# Construct an algorithm that counts how many evening classes (classes happening at 18 or 19 there are.
# Construct an algorithm that returns a list of Boxfit classes including the week and day they occur on. Assume [0][0] is Monday week 1. 

activities = ([ [8, "Pilates"], [18, "Boxfit"], [13, "Attack"], [9, "Pilates"], [14, "Attack"], [8, "Pilates"], [8, "Pilates"] ],

# Week 2
[ [10, "Boxfit"], [9, "Pilates", 17, "Attack"], [19, "Boxfit"], [9, "Pilates"], [9, "Baby Yoga"], [8, "Pilates"], [8, "Pilates"] ],

# Week 3
[ [8, "Pilates"], [11, "Boxfit", 17, "Yoga"], [18, "Pilates"], [12, "Boxfit"], [18, "Pilates"], [8, "Pilates", 10, "Boxfit"], [8, "Pilates"] ],

# Week 4
[ [18, "Pilates"], [19, "Boxfit"], [19, "Pilates"], [19, "Boxfit"], [19, "Pilates"], [8, "Pilates"], [8, "Pilates"] ])

pilates_counter = 0
for i in range(len(activities)):
    for x in range(len(activities[i])):
        for j in range(len(activities[i][x])):
            try:
                if activities[i][x][j] == "Pilates":
                    pilates_counter+=1
            except:
                continue

print(f"\nThe amount of pilates classes is {pilates_counter}.")

evening_counter=0
for i in range(len(activities)):
    for x in range(len(activities[i])):
        for j in range(len(activities[i][x])):
            try:
                if activities[i][x][j] == 18 or activities[i][x][j] == 19:
                    evening_counter+=1
            except:
                continue

print(f"\nThere are {evening_counter} evening classes")

boxfit=[]
for i in range(len(activities)):
    for x in range(len(activities[i])):
        for j in range(len(activities[i][x])):
            try:
                if activities[i][x][j] == "Boxfit":
                    boxfit.append([i, x])
            except:
                continue

print(f"\nWeek and day of boxfit classes: {boxfit}")