fil = open("C:\\Users\\Ander\\ING301\\ing301public\\examples\\02_gpsdata\\gpslogs\\long.csv")
liste = fil.readlines()
foerste = liste[0]
liste2 = foerste.split(',')
for x in liste2:
    print(x)