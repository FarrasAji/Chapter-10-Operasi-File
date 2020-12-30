file = open('Data5.txt', 'r')
result = []
for i in file.readlines() :
    if('\n' in i) :
        replaced = i.replace('\n','')
        splitted = replaced.split('|')
        valueList = int(splitted[0]) + int(splitted[1])
        result.append(valueList) 
    else :    
        splitted = i.split('|')
        valueList = int(splitted[0]) + int(splitted[1])
        result.append(valueList)

file.close()
output = open('Hasil5.txt', 'w')
for i in range(len(result)) :
    output.write(str(result[i]) + '\n')
output.close()
print('Hasil penjumlahan berada pada file hasil5.txt')
