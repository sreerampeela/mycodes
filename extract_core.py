file1 = open("invasive_data_new.csv",'r')
file2 = open("invasive-core.txt",'w',newline='\n',encoding='utf-8')
file3 = open("invasive-softcore.txt",'w',newline='\n',encoding='utf-8')
file4 = open("invasive-shell.txt",'w',newline='\n',encoding='utf-8')
file5 = open("invasive-cloud.txt",'w',newline='\n',encoding='utf-8')
data = file1.readlines()[1:]
for i in data:
    gene = i.rstrip().split(",")[0] + "\n"
    print(gene)
    coreyes = i.rstrip().split(",")[-1]
    print(coreyes)
    if coreyes == "1":
        file2.write(gene)
    if coreyes == "2":
        file3.write(gene)
    if coreyes == "3":
        file4.write(gene)
    else:
        file5.write(gene)

file1 = open("invasive-core.txt",'r')
file2 = open("invasive-accessory.txt",'r')
file3 = open("carriage-core.txt",'r')
file4 = open("carriage-accessory.txt",'r')
file5 = open("pan_results.csv",'w',newline='\n',encoding='utf-8')
inv_core = file1.readlines()
inv_accessory = file2.readlines()
car_core = file3.readlines()
car_accessory = file4.readlines()
inv_core_genes = []
inv_accessory_genes = []
car_core_genes = []
car_accessory_genes = []
for data in [inv_core,inv_accessory,car_core,car_accessory]:
    for j in data:
        d = j.split("\t")[0].split(":")[0]
        print(d)
        if data == inv_core:
            inv_core_genes.append(d)
        elif data == inv_accessory:
            inv_accessory_genes.append(d)
        elif data == car_core:
            car_core_genes.append(d)
        else:
            car_accessory_genes.append(d)
inv_core_genes1 = ",".join(inv_core_genes) + '\n'
inv_accessory_genes1 = ",".join(inv_accessory_genes) + '\n'
car_core_genes1 = ",".join(car_core_genes) + '\n'
car_accessory_genes1 = ",".join(car_accessory_genes) + '\n'
file5.write(inv_core_genes1)
file5.write(inv_accessory_genes1)
file5.write(car_core_genes1)
file5.write(car_accessory_genes1)
print(inv_core_genes)


file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
