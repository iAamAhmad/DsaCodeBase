prev = 0
prevtwo =1
print(prev)
print(prevtwo)
for febo in range(18):
   nextFebo = prev + prevtwo
   print(nextFebo)
   prevtwo = prev
   prev = nextFebo
   