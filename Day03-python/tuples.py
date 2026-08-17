tup=("apple","bat","car")# tuples are unchangable we cant add or delete the values and ordered,allows duplicates
print(tup[1])

#counting the no.of duplicates a specific value in the tuple
print(tup.count("car"))

#unpacking the tuples
(x,y,z)=tup #unpacking done like this we assign a variable for each value to access by the variable
print(z)
#if we want to give the multiple values to the single variable we use the asterisk*
(x,*y)=tup #after the x stored the first value then the remaining are stored in the y
print(y)