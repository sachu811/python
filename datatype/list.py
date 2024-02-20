# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements
# A list is a versatile data structure in python that may hold a collection of object of various data types
# it is a mutable data type in python which means that its elements can be changed after they are created
# lists are represented by square brackets and their elements by commas

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone'] #define python
#print(sea_creatures)
#print(sea_creatures[0])

#update
sea_creatures[0]='dolphine'
#print(sea_creatures)

#remove
sea_creatures.pop(0)
#print(sea_creatures)

#reverse
sea_creatures.reverse()
#print(sea_creatures)

#length
#print(len(sea_creatures))

print(['Hi']*4)

print([1,2,3,4]+[6,7,8,9])

if(3 in [1,2,3]):
    print("true")

for x in [1,2,3,4,5]:
    print(x)


