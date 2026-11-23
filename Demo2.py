
values = [ 1, 2, "rahul", 4, 5 ]

# List is data type that allows multiple values and can be different data types

print(values[0]) # 1

print(values[3]) # 4

print(values[-1]) # 5

print(values[1:3]) # 2 rahul 4


# Insert
values.insert(3, "DJ")

print((values)) # [1, 2, 'rahul', 'DJ', 4, 5]


# Append
values.append(7)

print(values) #[1, 2, 'rahul', 'DJ', 4, 5, 7]


#Update

values[2] = "RAHUL"

print(values) # [1, 2, 'RAHUL', 'DJ', 4, 5, 7]


#Delete

del values[0]

print(values) #[2, 'RAHUL', 'DJ', 4, 5, 7]




# Tuple - same as list only difference is that tuple in immutable

val1 = (1,3,"rahul",5.6)

print(val1[2]) # rahul

#val1[2] = "RAHUL"  # TypeError: 'tuple' object does not support item assignment -- Immutable




# Dictionary

dic1 = { 1:"abc" , "c": 2, 4:53}

print(dic1[1])  #abc -- accessing it via key not index

print(dic1["c"]) #2

dic1[5] ="hello world"

print(dic1)


# Adding new values in  empty dict
dict2 = {}

dict2 ["firstName"] ="abc"
dict2 ["lastName"] ="xyz"
dict2 ["gender"] ="Male"

print(dict2)