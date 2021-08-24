val = input('Enter num: ')
val = int(val)
running = True
count = 0
highval = 0

while running:
    if (val % 2) == 0:
        val = val/2
        print (val)
        count += 1
        if val > highval:
            highval = val
    else:
        val = (val*3) + 1
        print (val)
        count += 1
        if val > highval:
            highval = val

    if val == 1:
        running = False
        print('---------------')
        print('Total ops taken: ',count)
        print('Highest val: ',highval)

