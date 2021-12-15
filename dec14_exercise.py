ages = [
29,
19,
17,
26,
32,
16,
21,

]
#4
print(ages)
#6
print(ages[4])
#7
print(ages[-2])
#8
print(ages[2:6])
#9
print(ages[:3])
#10
print(True) if 17 in ages else print(False)
    
#11
print(True) if 42 in ages else print(False)


#13
ages[2]=18
print(ages)

#14
temp=ages[4]
ages[4]=ages[3]
ages[3]=temp
print(ages)

#17
ages.append(45)
print(ages)

#18
ages.insert(0,32)
print(ages)

#19
ages.insert(5,37)
print(ages)

#22
ages.pop()

#23
ages.pop(2)

print(ages)