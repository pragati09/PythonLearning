arr = [[]]

arr[0].append(2)
arr[0].append(5)
arr.append([])
arr[1].append(3)
arr[1].append(7)
arr.append([])
arr[2].append(1)
arr[2].append(3)
arr.append([])
arr[3].append(4)
arr[3].append(0)

#for i in range(len(arr)):
    #for j in range(len(arr[i])):
        #print(arr[i][j], end=' ')
    #print()

temp = -1;	
for i in range(len(arr)):
	if(arr[i][0]>arr[i][1] and arr[i][0] > temp):
		temp = arr[i][0];
	elif(arr[i][1] > temp):
		temp = arr[i][1];

print (temp);
    

#print (arr)