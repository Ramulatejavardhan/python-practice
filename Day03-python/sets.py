#sets are unordered,doesn't allow the duplicates and unchangeable but{we can add and remove the values}
sets={"hi","hello","hi","bye"}#hi counts 1
print(len(sets))

#add the new items
sets.add("hlo")
print(sets)
set2={"bat","bag"}
sets.update(set2)
print(sets)

#to remove the items from the sets we can use the discard() or remove()
sets.remove("bat")#we cant remove it by indexing because it is unordered
sets.discard("bag")
print(sets)

#join in the 2 0r more sets
myset=sets.union(set2)
