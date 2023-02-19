for i in range(1, 10):
    for x in range(1, 10):
        print(i * x, end = "")
    print()

#解答例99.pyの5行目の文を次の文に書き換える．
#print("%2d" % (i * j), end=" ")
#または
#print("{0:>2}".format(i * j), end=" ")

#i = 1
#while i < 10:
 # j = 1
  #while j < 10:
   #j = j + 1
  #print()
  #i = i + 1

#for r in range(1,10):
 # for c in range(1,10):
  #  print(f'{r*c:4d}', end = "")
  #print("\n", end = "")

#for i in range(1, 10):
  #for d in range(1, 10):
    #print(f"{i * d :3d}", end = "")
  #print()
