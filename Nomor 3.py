file = open('Data2.txt', 'r')
perbaris = file.readlines()
dic = {}
listDict = []

for i in range(len(perbaris)) :
    a = perbaris[i].split('|')
    a[2] = a[2].replace('\n', '')
    
    dic = {'nim' : a[0], 'nama' : a[1], 'alamat' : a[2]}
    listDict.append(dic)

print(listDict)
file.close()
