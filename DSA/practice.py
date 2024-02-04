prev = 0
prevtwo =1
print(prev)
print(prevtwo)
for febo in range(18):
   nextFebo = prev + prevtwo
   print(nextFebo)
   prevtwo = prev
   prev = nextFebo


var1 = 0
var2 = 2
count = 2
def findingFebn(var1, var2):
   global count
   print(var1)
   print(var2)
   if count <= 19:
      varnew = var1 + var2 
      print(varnew)
      var2 = var1
      var1 = varnew
      count +=1
      findingFebn(var1, var2)
   else:
      return
findingFebn(0,1)
findingFebn(0,1)
   