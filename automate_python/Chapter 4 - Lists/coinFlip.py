import random

numberOfStreaks = 0
coinSigns = []
tailsCounter = 0
headsCounter = 0

def CoinFlipLogic():
    pass

for experimentNumber in range(10000):
    ranNum = random.randint(0, 1)
    if ranNum == 0:
        coinSigns.append("T")
        tailsCounter += 1
    elif ranNum == 1:
        coinSigns.append("H")
        headsCounter += 1


print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print(coinSigns)
print("There are: ", tailsCounter, "tails")
print("There are: ", headsCounter, "heads")

