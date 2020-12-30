file = open('Data1.txt', 'r')
Data1 = file.readlines()

dataganjil= []
datagenap = []

for i in range(len(Data1)):
    data = Data1[i] 
    if (int(data)%2) == 0 :
        datagenap.append(Data1[i])
    else :
        dataganjil.append(Data1[i])
        
print('Banyaknya bilangan genap : ', len(datagenap))
print('Banyaknya bilangan ganjil: ', len(dataganjil))
