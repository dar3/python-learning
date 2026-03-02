import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    coinSigns = []

    # Generate 100 coin flips
    for i in range(100):
        if random.randint(0, 1) == 0:
            coinSigns.append('H')
        else:
            coinSigns.append('T')

    # Check for streak of 6
    streakCount = 1

    for i in range(1, len(coinSigns)):
        if coinSigns[i] == coinSigns[i - 1]:
            streakCount += 1
            if streakCount == 6:
                numberOfStreaks += 1
                break
        else:
            streakCount = 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))