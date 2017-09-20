item_count={'test':0}

#A function to count the occurances of all possible pairings of items
def freqCount(val,items):
	global item_count
	if (len(items)==0):
		return
	counter =len(items)
	key=str(items[counter-1])+","+str(val)
	if key in item_count:
		item_count[key]+=1
	else:
		item_count[key]=1
	counter-=1
	temp=items[:counter]
	freqCount(val,temp)
	if(len(items)==1):
		return
	key=""
	for value in items:
		key+=str(value)+","
	key+=str(val)
	if key in item_count:
		item_count[key]+=1
	else:
		item_count[key]=1
	return

filename=raw_input('Enter the file containing the dataset: ')
file = open(filename,'r')
raw_dataset=file.read().split('\n')
meta_data=raw_dataset[0].split(",")
# print(raw_dataset[0])
no_of_items=int(meta_data[0])
print('No. of items = ',no_of_items)
raw_dataset=raw_dataset[1:no_of_items+1]
# print('Raw Dataset:')
# print(raw_dataset)

dataset=[]
freqItemSet=[]						 #To kep track of all frequent Item Sets after every iteration.
for trans in raw_dataset:
	items=trans.split(",")
	prevItems=[]
	for val in items:
		if val in item_count:
			item_count[val]+=1
		else:
			item_count[val]=1
		if(len(prevItems)!=0):
			freqCount(int(val),prevItems)
		prevItems.append(int(val))
candidSet=[str(i+1) for i in range(no_of_items)]

#Printing item_count
# for key in item_count:
# 	print(key,":",item_count[key])

#Running iterations
sup_val=int(input('Enter the support value: ')) #Threshold value
iteration=0

while(True):
	iteration+=1
	freqSetObj=[]
	print "iteration: ",iteration
	for key in candidSet:
		if(item_count[key]>=sup_val):
			freqSetObj.append(key)
	freqItemSet.append(freqSetObj)

	#Forming Candidate Set from Previous Frequen Item Set
	temp=[]
	for item in candidSet:
		
