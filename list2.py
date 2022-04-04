from tokenize import String


heros=['spider man', 'thor', 'hulk' ,'iron man', 'captain america']
print(heros)
print("Length of list:",len(heros))

heros.append('black panther')
print("Update list: ",heros)

heros.remove('black panther')
heros.insert(3,'black panther')
print("Update list: ",heros)

heros.remove('thor')
heros.remove('hulk')
heros.insert(1,'doctor strange')
print("Update list: ",heros)

# romove thor and hulk in single line code
#heros[1:3]='doctor stange'
#print("Update list: ",heros)


heros.sort()
print("Sorted list: ",heros)

# Basically dir() returns all pre-difined functions of dataTye like list, Strings and ect..
print(dir(list))
print(dir(String))


