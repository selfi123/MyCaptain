fre={}
s=input("Please enter a string :")
for i in s:
   c=0
   for k in s:
       if i==k:
          c=c+1
   fre[i]=c
for w in sorted(fre, key = fre.get, \
                reverse = True):
    print(w+"="+"0"+str(fre[w]),end=" ")

