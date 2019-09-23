
print("Enter the number of players")
noOfPlayers = int(input())

mals = []

for i in range(noOfPlayers):
    
    print("Enter mal of player-" + str(i+1))
    mal = int(input())
    mals.append(mal)

print("Who won the game? (Enter position of the player)")
winPos = int(input())

# making negative mals zero    
countNoMal = 0
for i in range(len(mals)):
    if mals[i] < 0:
        countNoMal = countNoMal + 1
        mals[i] = 0

# calculating total mal
totalMal = sum(mals)
# print(totalMal)

finalArray = [None] * len(mals);    
# calculating mal for no showing players
for i in range(len(mals)):
    finalArray[i] = mals[i]
    
for i in range(len(mals)):
    if mals[i] == 0:
        finalArray[i] = -(totalMal+10)
        
# calculating mal for showing players
for i in range(len(mals)):
    if mals[i] != 0:
        finalArray[i] = (mals[i] * noOfPlayers) - (totalMal + 3)
        
b = finalArray[winPos-1] - sum(finalArray)
finalArray[winPos-1] = b

print(finalArray)