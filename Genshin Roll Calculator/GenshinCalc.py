import csv

charBanner = ["Albedo",
              "Ganyu",
              "Hu Tao",
              "Klee",
              "Tartaglia",
              "Venti",
              "Xiao",
              "Zhongli"
              "Eula"
]

stdBanner = ["Diluc",
             "Jean",
             "Keqing",
             "Mona",
             "Qiqi"
]

weaponsBanner = ["Elegy for the End",
                 "Memory of Dust",
                 "Primordial Jade Cutter",
                 "Song of Broken Pines",
                 "Staff of Homa",
                 "Summit Shaper",
                 "The Unforged",
                 "Vortex Vanquisher",             
]

stdweaponsBanner = ["Amos' Bow",
                    "Aquila Favonia",
                    "Lost Prayer to the Sacred Winds",
                    "Primordial Jade Winged-Spear",
                    "Skyward Atlas",
                    "Skyward Blade",
                    "Skyward Harp",
                    "Skyward Pride",
                    "Skyward Spine",
                    "Wolf's Gravestone",
]

inputList=[]
constDict=dict()
totalPulls = 20
avgRolls = 0
count = 0

ec = 0
sc = 0
ew = 0
sw = 0

with open('Test.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        count += 1
        inputList.append(row[0][-2:])
        totalPulls += int(row[0][-2:])
        if not(row[0][:-3] in constDict.keys()):
            constDict.__setitem__(row[0][:-3], 0)
        else:
            constDict[row[0][:-3]] += 1

avg = round(totalPulls/count, 2)
offsetAvg = round(abs(avg - 63), 2)

print("Steven's Genshin Luck Calculator\n")
print("List of your 5-star pulls:")
print("5-star Count: "+ str(count) + "\n")

print("  Event Characters")
for item in constDict:
    if item in charBanner:
        print("  -" + str(item) + " C" + str(constDict[item]))
        ec +=1

print("\n  Standard Characters")
for item in constDict:
    if item in stdBanner:
        print("  -" + str(item) + " C" + str(constDict[item]))
        sc +=1

print("\n  Exclusive Weapons")
for item in constDict:
    if item in weaponsBanner:
        print("  -" + str(item) + " R" + str(constDict[item]))
        ew +=1

print("\n  Standard Weapons")
for item in constDict:
    if item in stdweaponsBanner:
        print("  -" + str(item) + " R" + str(constDict[item]))
        sw +=1

print("\nTotal rolls:", totalPulls)
print("\nAverage rolls per 5-star:", avg, "\n")

if ((offsetAvg < 0.5) and (offsetAvg > -0.5)):
    print("You have about average luck. Not bad.")
    if (offsetAvg > 0):
        print("That's", abs(offsetAvg), "roll(s) more than the average of 63.")
    elif (offsetAvg < 0):
        print("That's", abs(offsetAvg), "roll(s) less than the average of 63.") 
    print("Not bad.")

elif (offsetAvg > 0.5):
    print("You have pretty bad luck. RIP :(")
    print("That's", abs(offsetAvg), "roll(s) more than the average of 63.")
    print("I feel that. :( -Steven")

elif (offsetAvg < 0.5):
    print("You have pretty good luck.")
    print("That's", abs(offsetAvg), "roll(s) less than the average of 63.")
    print("I hate you. -Steven")



