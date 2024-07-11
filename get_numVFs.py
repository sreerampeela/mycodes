file1 = open("vfdb_abricate.csv",'r')
file2 = open("gene_presence_absence.csv",'r',newline='\n',encoding='utf-8')
file3 = open("virulencegenes.csv",'w',encoding='utf-8',newline='\n')
data = file1.readlines()
vfs = list(set([i.split(",")[4].rstrip() for i in data]))
# print(vfs)
file4 = open("gff_files.txt",'r')
gffs = file4.readlines()[1:]
# gffs_car = [i.rstrip().split('\t')[0] for i in gffs]
# print(gffs)
data_car = []
for gff_file in gffs:
    for gene in vfs:
        print(gene)
        count = 0
        file = gff_file.rstrip()
        data = open(file,'r').readlines()
        for k in data:
            if k.startswith("gnl"):
                data_all = k.split("\t")[8].split(";")
                ind = data_all.index()
                print(data_all)
                print(ind)
        print(count)
        data_car.append(gene)
        data_car.append(count)

print(data_car[1])


file1.close()
file2.close()
file3.close()
file4.close()
