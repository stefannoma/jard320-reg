import random
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
selcalCode = ""
pointer = 0
pointer2 = 0

regNr = input("What is the registration of your aircraft?\n")
regNr = regNr.upper()

while pointer < 5:
    pointer2 = random.randint(0, len(alphabet) - 1)
    pointer2 = alphabet[pointer2]
    if pointer == 2:
        selcalCode += "-"
    else:
        selcalCode += pointer2
    pointer = pointer + 1

f = open("regSelcal.txt", "r")
index = 0
found = False
if regNr in f.read():
    print("Reg found, inputting into version.txt")
    f.close()
    f = open("regSelcal.txt", "r")
    array = f.readlines()
    while found == False:
        if regNr in array[index]:
            selcalIndex = array[index]
            selcalCode = selcalIndex[len(selcalIndex) - 6 : len(selcalIndex) - 1]
            found = True
        index += 1
    print(selcalCode)
            
else:
    f = open("regSelcal.txt", "a")
    f.write(f"{regNr}, {selcalCode}\n")
    f.close()

f = open("version.txt", "w")
f.write(f"{regNr} | {selcalCode}")
f.close()
