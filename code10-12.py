def visitSeoul():
    global total, countSeoul
    countSeoul += 1
    total += 1

def visitJeju():
    global total, countJeju
    countJeju += 1
    total += 1

total = 0
countSeoul = countJeju = 0
while True:
    choice = input("선택['s', 'j' or 'any key']:")
    if choice == 's':
        visitSeoul()
    elif choice == 'j':
        visitJeju()
    else:
        break
print(countSeoul, countJeju, total)