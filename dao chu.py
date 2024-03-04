import array as arr
print('Nhap hai chu:')
a = str(input())
b = str(input())
arr1= []
arr2= []
count=0
for i in range (26):
    arr1.append(0)
    arr2.append(0)
for i in range(len(a)):
    arr1[ord(a[i])-ord('a')]+=1
for i in range(len(b)):
    arr2[ord(b[i])-ord('a')]+=1
for i in range(26):
    if(arr1[i]!=arr2[i]):
        print('Hai chu khong la dao chu cua nhau')
        break
    else: count+=1
if(count==26):
    print('Hai chu la dao chu cua nhau')


