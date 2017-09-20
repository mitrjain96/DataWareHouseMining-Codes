filename=input('Enter the file containing the dataset: ')
file = open(filename,'r') 
raw_dataset=file.read().split('\n')
meta_data=raw_dataset[0].split(",")
# print(raw_dataset[0])
no_of_items=int(meta_data[0])
# print('No. of items = ',no_of_items)
print('Raw Dataset:')
print(raw_dataset)
dataset=[]

for trans in raw_dataset:
	items=trans.split(",")
	entry =0 #bitmasked representation of items
	for val in items:
		entry = entry | (1 << int(val))
	dataset.append(entry)

# print('Actual Dataset Representation:')
for item in dataset:
	print(bin(item))

#Running iterations
sup_val=int(input('Enter the support value')) #Threshold value
for item in dataset:
	

