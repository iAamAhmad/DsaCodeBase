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


def F(n):
   if n <= 1:
      return n
   else:
      return F(n-1) + F(n-2)
print(F(19))


my_array = [0,1,3,5,7,8]
min_val = my_array[0]
for i in my_array:
   if i < min_val:
      min_val = i
print(min_val)

x =[3,5,6,7,8,9]
min = x[0]
for i in x:
   if i< min:
      min = i
print(min)



y =[3,5,6,7,8,9]
max = x[0]
for i in x:
   if i> max:
      max = i
print(max)

#bubule sort

b = [8,4,6,7,2,3]
n = len(b)
for i in range(n-1):
   for j in range(n-i-1):
      if b[j] > b[j+1]:
         b[j+1], b[j] = b[j], b[j+1]
print(b)

#selection sorting

selection_sort = [3,4,5,6,2,8]
n = len(selection_sort)
for i in range(n-1):
   min_index = i
   for j in range(i+1,n):
      if selection_sort[j] < selection_sort[min_index]:
         min_index = j
   min_val = selection_sort.pop( min_index)
   selection_sort.insert(i,min_val)
print(selection_sort)
      
      
selection_sort = [3,4,5,6,2,8]
n = len(selection_sort)
for i in range(n-1):
   min_index = i
   for j in range(i+1,n):
      if selection_sort[j] < selection_sort[min_index]:
         min_index = j
   min_val = selection_sort.pop( min_index)
   selection_sort.insert(i,min_val)
print(selection_sort)
      
      

selection_sort = [3,4,5,6,2,8]
n = len(selection_sort)
for i in range(n-1):
   min_index = i
   for j in range(i+1,n):
      if selection_sort[j] < selection_sort[min_index]:
         min_index = j
   min_val = selection_sort.pop( min_index)
   selection_sort.insert(i,min_val)
print(selection_sort)