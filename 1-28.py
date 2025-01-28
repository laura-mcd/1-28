#list
list = [1,2,3,4,5,6,7,8,9,10]

#add 11 to list
list.append(11)
print(list)

#remove 5 from list
list.remove(5)
print(list)

#list numbers in reverse
list.reverse() 
print(list)

#find maximum and minimum
maximum = max(list)
minimum = min(list)
print("maximum number:" , maximum)
print("minimum number:" , minimum)

#find average
average = sum(list)/len(list)
print("average number:" , average)