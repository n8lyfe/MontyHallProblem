import random

anzahlGewinne = 0
rolls = 1000000

#Spieler wechselt nicht:
for i in range (1, rolls):
    gewinn = random.randint(1,3)
    wahlPlayer = random.randint(1,3)
    wahlMod = random.randint(1,3)

    while wahlMod == wahlPlayer or wahlMod == gewinn:
        wahlMod = random.randint(1,3)

    if (wahlPlayer == gewinn):
        anzahlGewinne = anzahlGewinne +1

print ("Spieler wechselt nicht - Gewinn-Chance: " + str(anzahlGewinne/rolls))

#Spieler wechselt:
anzahlGewinne = 0
for i in range (1, rolls):
    gewinn = random.randint(1,3)
    wahlPlayer = random.randint(1,3)
    wahlMod = random.randint(1,3)

    while wahlMod == wahlPlayer or wahlMod == gewinn:
        wahlMod = random.randint(1,3)

    wahlPlayerNew = random.randint(1,3)

    while wahlPlayerNew == wahlPlayer or wahlPlayerNew==wahlMod:
        wahlPlayerNew = random.randint(1,3)
    if (wahlPlayerNew == gewinn):
        anzahlGewinne = anzahlGewinne +1

print ("Spieler wechselt - Gewinn-Chance: " + str(anzahlGewinne/rolls))
