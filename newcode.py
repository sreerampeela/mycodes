# # creating an attendance report for students
#
# std_names = []
# n_students = int(input("Enter number of students: "))
# for i in range(n_students):
#     name = input("Enter student name: ")
#     std_names.append(name)
# max_name = max(name for names in std_names)
# max_char = len(max_name)
# print(max_name)
# std_names.sort()
# print(std_names)
# n_days = int(input("Enter number of working days: "))
# final_attendance = [0] * n_students
# for day in range(n_days):
#     for std in std_names:
#         attendance = input("Is {} present today? (P for present and A for absent): ".format(std))
#         if attendance.lower() == "p":
#             attendance_value = 1
#         elif attendance.lower() == "a":
#             attendance_value = 0
#         else:
#             print("Not a proper entry for {}".format(std))
#         roll_no = std_names.index(std)
#         final_attendance[roll_no] += attendance_value
#
# print(final_attendance)
# attendance_percent = []
# for attend in final_attendance:
#     atd_per = (attend / n_days) * 100
#     attendance_percent.append(atd_per)
#
# print(atd_per)
# for std_out in std_names:
#     roll = std_names.index(std_out) + 1
#     atd_percent = round(attendance_percent[roll - 1], 2)
#     output = str(roll) + " " + std_out + " " * (max_char - len(std_out) + 3) + str(atd_percent)
#     print(output)
# FILE COPYING

# file1 = open("files.txt",'r')
# file3 = open("poppunk_input3.txt",'w',encoding='utf-8',newline='\n')
# ids = file1.readlines()
# print(ids)
# for data in ids:
#     data.rstrip()
#     assembly = data.split("\t")[0].rstrip()+".fasta"
#     sample = data.split("\t")[1].rstrip()
#     poppunk = "{}\t/home/sreeram/Desktop/gpsc_project/kims_2021/ghru_contigs/{}".format(sample,assembly) + "\n"
#     file3.write(poppunk)
# # for id in ids:
# #     id = id.rstrip()
# #     begin = id.split("_")[0]
# #     if begin.lower() == "crl":
# #         kims_id = id.split("_")[2]
# #     elif begin.lower() == "spn":
# #         kims_id = id.split("_")[1]
# #     print(kims_id)
# for i in ids:
#     fastq1 = i.split("\t")[0].rstrip() + "_R1_001.fastq.gz"
#     fastq2 = i.split("\t")[0].rstrip() + "_R1_001.fastq.gz"
#     sample_id = i.split("\t")[1].rstrip()
#     print(sample_id,fastq1,fastq2)
#     # cmd = "cp {} ~/Desktop/gpsc_project/kims_2021/{}_1.fastq.gz".format(fastq1,sample_id) + "\n"
#     # cmd2 = "cp {} ~/Desktop/gpsc_project/kims_2021/{}_2.fastq.gz".format(fastq2,sample_id) + "\n"
#     # file3.write(cmd)
#     # file3.write(cmd2)
#     cmd1 = "shovill --outdir {}_shovill --cpus 8 --trim --depth 150 " \
#           "--R1 {} --R2 {}".format(sample_id,fastq1,fastq2) + "\n"
#     cmd2 = "cp {}_shovill/contigs.fa $PWD/{}_contigs.fasta".format(sample_id,sample_id) + "\n"
#     cmd3 = "cat {}_shovill/00-shovill.log >> shovill_log.txt".format(sample_id) + "\n"
#     file3.write(cmd1)
#     file3.write(cmd2)
#     file3.write(cmd3)
#
#
# file1.close()
# file3.close()
# file1 = open("plasmid_filt.txt", 'r')
# file2 = open("plasmid_filt.csv", 'w', newline='\n')
# data = file1.readlines()
# print(data)
# genes = []
# samples = []
# for i in data[1:]:
#     i.rstrip()
#     gene = i.split("\t")[4]
#     # print(gene)
#     sample = i.split("\t")[0].split("_")[0]
#     # print(sample)
#     genes.append(gene)
#     samples.append(sample)
# genes_all = list(set(genes))
# genes_all.sort()
# samples_all = list(set(samples))
# samples_all.sort()
# print(genes_all, samples_all)
# header = "sample," + ",".join(genes_all) + "\n"
# file2.write(header)
# # summary_data = []
# for sample_name in samples_all[1:]:
#     genes_presence = ["N"]*len(genes_all)
#     for j in data[1:]:
#         sample = j.rstrip().split("\t")[0].split("_")[0]
#         if sample_name == sample:
#             gene_present = j.split("\t")[4]
#             ind = genes_all.index(gene_present)
#             genes_presence[ind] = "P"
#     print(genes_presence)
#     print(sample_name)
#     data_sam = sample_name + "," + ",".join(str(e) for e in genes_presence) + "\n"
#     # new_data = sample_name + "," + ",".join([gene for gene in genes_presence]) + "\n"
#     file2.write(data_sam)
#
# file1.close()
# file2.close()
# file1 = open("pathwatch_filenames.txt",'r')
# file2 = open("pathwatch_copy.txt",'w',newline='\n',encoding='utf-8')
# data = file1.readlines()
# ids = []
# runs = []
# for d in data:
#     ids.append(d.split("\t")[1].rstrip())
#     runs.append(d.split("\t")[0].rstrip())
# for i in range(len(ids)):
#     cmd = "mv {}.gz {}_contigs.fasta".format(runs[i],ids[i]) + "\n"
#     file2.write(cmd)
#
# file1.close()
# file2.close()
#
# file_1 = open("POPPUNK_IND.txt",'r')
# file_2 = open("spn_india_isppd2.newick",'r')
# file_3 = open("core_tree.newick",'w')
# data = file_1.readlines()
# tree_data = file_2.read()
# for i in data:
#     sample_id = i.rstrip().split('\t')[0]
#     acc_id = i.rstrip().split('\t')[1].split("/")[6].split("_")[0] + "_prokka"
#     # print(sample_id,acc_id)
#     tree_data = tree_data.replace(acc_id,sample_id)
# file_3.write(tree_data)
# print(tree_data)
#
# file_1.close()
# file_2.close()
# file_3.close()

# file1 = open("data_for_itol.csv",'r')
# file2 = open("data_in_itol.csv",'r')
# fileout = open("data_annotation2.csv",'w',encoding='utf-8',newline='\n')
# data_itol = file1.readlines()[1:]
# # print(data_itol)
# tree_data = file2.readlines()[1:]
# # print(tree_data)
# for id in tree_data:
#     id_new = id.rstrip().split("_")[0]
#     # print(id_new)
#     id_data = [i.rstrip().split(",")[0] for i in data_itol]
#     print(id_data)
#     if id_new in id_data:
#         ind = id_data.index(id_new)
#         out = data_itol[ind]
#         fileout.write(out)
#         print(out)
#
# fileout.close()
# file1.close()
# file2.close()
# file1 = open("gene_presence_absence_invasive.csv",'r')
# file2 = open("sero_test6.txt",'w',newline='\n',encoding='utf-8')
# # file3 = open("file_copier4.txt",'w',newline='\n')
# ids = file1.readlines()
# for id in ids:
#     id = id.rstrip()
#     oldr1 = id + "_1.fastq.gz"
#     oldr2 = id + "_2.fastq.gz"
#     read1 = id + "_S1_L001_R1_001.fastq.gz"
#     read2 = id + "_S1_L001_R2_001.fastq.gz"
#     # cmd1 = "copy H:\indian_spn_genome_analysis\shovill_assembly\{}\R1.fq.gz D:\{}".format(id,read1) + '\n'+ "copy H:\indian_spn_genome_analysis" \
#     #                                                                                  "\{}\R2.fq.gz D:\{}".format(id,read2) + '\n'
#
#     cmd = "docker run --rm=True -v $PWD:/data quay.io/biocontainers/fastp:0.20.1--h8b12597_0 fastp " \
#           "-i /data/{} -I /data/{} " \
#           "-o /data/{}_fastp_S1_L001_R1_001.fastq.gz " \
#           "-O /data/{}_fastp_S1_L001_R2_001.fastq.gz".format(oldr1,oldr2,id,id) + '\n'
#     cmd2 = "docker run --rm=True -v $PWD:/data staphb/cdc-spn SPN_Serotyper.pl " \
#           "-1 /data/{}_fastp_S1_L001_R1_001.fastq.gz" \
#           " -2 /data/{}_fastp_S1_L001_R2_001.fastq.gz -n {} -o /data/test_cdcpipeline3/{} " \
#           "-r /data/SPN_Reference_DB/SPN_Sero_Gene-DB_Final.fasta".format(id,id,id,id) + '\n'
#     # file3.write(cmd1)
#     # print(cmd1)
#     file2.write(cmd)
#     file2.write(cmd2)
#
#
# file2.close()

# file2 = open("invasive_data.csv",'w',encoding='utf-8',newline='\n')
# data = file1.readlines()[1:]
# # print(data)
# for rowdata in data:
#     all_data = rowdata.split(",")
#     gene = all_data[0]
#     # print(all_data)
#     values = []
#     for i in all_data:
#         if len(i) != 0:
#             value = "1"
#         else:
#             value = "0"
#         values.append(value)
#     values = ','.join(values)
#     # print(values)
#     data_new = gene + "," + values + '\n'
#     file2.write(data_new)
#
#
#
#
# file1.close()
# file2.close()
# file3.close()

# file1 = open("invasive_data_new.csv",'r')
# file2 = open("invasive-core.txt",'w',newline='\n',encoding='utf-8')
# file3 = open("invasive-softcore.txt",'w',newline='\n',encoding='utf-8')
# file4 = open("invasive-shell.txt",'w',newline='\n',encoding='utf-8')
# file5 = open("invasive-cloud.txt",'w',newline='\n',encoding='utf-8')
# data = file1.readlines()[1:]
# for i in data:
#     gene = i.rstrip().split(",")[0] + "\n"
#     print(gene)
#     coreyes = i.rstrip().split(",")[-1]
#     print(coreyes)
#     if coreyes == "1":
#         file2.write(gene)
#     if coreyes == "2":
#         file3.write(gene)
#     if coreyes == "3":
#         file4.write(gene)
#     else:
#         file5.write(gene)

# file1 = open("invasive-core.txt",'r')
# file2 = open("invasive-accessory.txt",'r')
# file3 = open("carriage-core.txt",'r')
# file4 = open("carriage-accessory.txt",'r')
# file5 = open("pan_results.csv",'w',newline='\n',encoding='utf-8')
# inv_core = file1.readlines()
# inv_accessory = file2.readlines()
# car_core = file3.readlines()
# car_accessory = file4.readlines()
# inv_core_genes = []
# inv_accessory_genes = []
# car_core_genes = []
# car_accessory_genes = []
# for data in [inv_core,inv_accessory,car_core,car_accessory]:
#     for j in data:
#         d = j.split("\t")[0].split(":")[0]
#         print(d)
#         if data == inv_core:
#             inv_core_genes.append(d)
#         elif data == inv_accessory:
#             inv_accessory_genes.append(d)
#         elif data == car_core:
#             car_core_genes.append(d)
#         else:
#             car_accessory_genes.append(d)
# inv_core_genes1 = ",".join(inv_core_genes) + '\n'
# inv_accessory_genes1 = ",".join(inv_accessory_genes) + '\n'
# car_core_genes1 = ",".join(car_core_genes) + '\n'
# car_accessory_genes1 = ",".join(car_accessory_genes) + '\n'
# file5.write(inv_core_genes1)
# file5.write(inv_accessory_genes1)
# file5.write(car_core_genes1)
# file5.write(car_accessory_genes1)
# print(inv_core_genes)
#
#
# file1.close()
# file2.close()
# file3.close()
# file4.close()
# file5.close()
# 
# file1 = open("pan_old_results2.csv",'r',newline='\n')
# file2 = open("pan_genome_original.fasta",'r',newline='\n',encoding='utf-8')
# file3 = open("old_pan_genes.txt",'w',newline='\n',encoding='utf-8')
# data = [i.rstrip() for i in file2.readlines()]
# # all_genes = [i.rstrip() for i in file3.readlines()]
# print(data)
# head = []
# gene_ranges = []
# for i in data:
#     if i.startswith(">"):
#
#         gene = i[1:]
#         # if gene in all_genes:
#         print(gene)
#         ind = data.index(i) + 1
#         gene_ranges.append(ind)
#         head.append(gene)
# # print(head)
# # print(gene_ranges)
# for j in range(len(head)-1):
#     # print(head[j])
#     name = ">" + head[j] + '\n'
#     start = gene_ranges[j]
#     end = gene_ranges[j+1] - 1
#     seq = "".join(j.rstrip() for j in data[start:end]) + '\n'
#     file3.write(name)
#     file3.write(seq)
#     print(name,seq)
# # print(''.join(data[end+1:]))
# # print(head[13])
# file1.close()
# #
# file2.close()
# # file3.close()

# genes = "cps4J	cps4B	cps4D	cps4A	cps4A	hysA	cbpD	cbpD	cps4B	cps4B	cps4B	cps4B	cps4B	pce	pce	" \
#         "pce	lytC	lytC	lytC	pfbA	cps4C	rrgC	rrgC	rrgC	pspA	pspA	nanB	pspA	rrgA	" \
#         "rrgA	nanA	srtC-2/srtC	nanA	srtG1	srtC-3/srtD	rrgB	srtC-1/srtB	srtG2	cps4F	cps4C	lytA	" \
#         "lytA	lytA	lytA	lytA	lytA	lytA	zmpC	cps4A	pitA	pitB	cps4E	cps4C	cps4D	cps4F	" \
#         "cps4J	srtC-2/srtC	srtC-3/srtD	cps4B	cps4B	cps4C	cps4I	nanA	cps4G	cps4H	cps4I	cbpG	nanA	" \
#         "cps4E	cps4B	lytA	nanB	pfbA	ply	psaA	pavA	sipA	cps4A	cps4K	cps4L	cps4E	cps4C"
#
# genes_set = list(set(genes.split("\t")))
# print(genes_set)


# file1 = open("old_pan_acc.txt",'r',newline='\n',encoding='utf-8')
# file2 = open("pan_old_results2.csv",'w',newline='\n',encoding='utf-8')
# old_core = file1.readlines()
# # print(old_core)
# old_core_genes = []
# for data in old_core:
#     d = data.rstrip().split("\t")[0].split(":")[0]
#     print(d)
#     old_core_genes.append(d)
#
# old_core_genes2 = ",".join(old_core_genes) + '\n'
# file2.write(old_core_genes2)
#
# file1.close()
# file2.close()
# import fnmatch
# file1 = open("vfdb_abricate.csv",'r')
# file2 = open("gene_presence_absence.csv",'r',newline='\n',encoding='utf-8')
# file3 = open("virulencegenes.csv",'w',encoding='utf-8',newline='\n')
# data = file1.readlines()
# vfs = list(set([i.split(",")[4].rstrip() for i in data]))
# # print(vfs)
# file4 = open("gff_files.txt",'r')
# gffs = file4.readlines()[1:]
# # gffs_car = [i.rstrip().split('\t')[0] for i in gffs]
# # print(gffs)
# data_car = []
# for gff_file in gffs[:1]:
#     for gene in vfs:
#         print(gene)
#         count = 0
#         file = gff_file.rstrip()
#         data = open(file,'r').readlines()
#         for k in data:
#             if k.startswith("gnl"):
#                 data_all = k.split("\t")[8].split(";")
#                 ind = data_all.index()
#                 print(data_all)
#                 print(ind)
#         print(count)
#         data_car.append(gene)
#         data_car.append(count)
#
# print(data_car[1])
#
#
# file1.close()
# file2.close()
# file3.close()
# file4.close()
# script = open("pbptyper_script2.txt",'w',newline='\n',encoding='utf-8')
# ids = ["990666",'2000157','990749','2000164','2000163','2000165','2000182','2000185','2000213','2000188']
# print(len(ids))
# for i in ids:
#     seq_file = i + ".faa"
#     cmd = "echo {} >> results.tab".format(i) + '\n'
#     script.write(cmd)
#     for db in ['spn_pbp1a_db', 'spn_pbp2b_db', 'spn_pbp2x_db']:
#         gene = db.split("_")[1]
#         outfile = i + gene + ".txt"
#         cmd1 = "blastp -db {} -query ../contigs/{} -outfmt 6 | sort -k12,12 -nr -k3,3 -k4,4 | " \
#                "head -n 1 >> results.tab".format(db,seq_file,i) + '\n'
#         # cmd2 = "cat ../{} | ".format(outfile) + '\n'
#         # print(cmd1,cmd2)
#         script.write(cmd1)
#         # script.write(cmd2)
#
# script.close()

# print(type(bin(10).replace("0b",'')))


import os
os.chdir("D:/kims_2021/ghru_contigs/reordered_contigs")
# files = os.listdir()
# print(type(files))
file_names = "ERR2090225,ERR3227834,ERR4784551,ERR4784667,ERR4784547,ERR4784688,ERR4784684,ERR4784692,ERR4784605,ERR3227765," \
            "ERR4784676,ERR4784696,SRR8879299,ERR3227775,ERR3227773,ERR3227779,ERR3227784,ERR3227767,ERR3227746,SRR8879297," \
            "SRR8879296,ERR3227783,ERR3227781,SRR8879298,ERR3227771,CRL_SPN_03_S2_L001,CRL_SPN_07_S4_L001,CRL_SPN_02_S1_L001," \
            "CRL_SPN_06_S3_L001,SPN4_S44_L001,CRL_SPN_08_S5_L001,CRL_SPN_13_S6_L001,CRL_SPN_14_S7_L001,CRL_SPN_20_S13_L001," \
            "CRL_SPN_15_S8_L001,CRL_SPN_16_S9_L001,CRL_SPN_17_S10_L001,CRL_SPN_18_S11_L001,CRL_SPN_35_S21_L001," \
            "CRL_SPN_19_S12_L001,CRL_SPN_23_S14_L001,CRL_SPN_27_S17_L001,CRL_SPN_25_S16_L001,CRL_SPN_29_S18_L001," \
            "Spn_31_S14_L001,CRL_SPN_32_S19_L001,Spn_28_S13_L001,CRL_SPN_33_S20_L001,CRL_SPN_42_S22_L001,CRL_SPN_43_S23_L001," \
            "CRL_SPN_46_S25_L001,Spn_44_S22_L001,CRL_SPN_45_S24_L001,CRL_SPN_59_S31_L001,CRL_SPN_60_S32_L001," \
            "CRL_SPN_61_S33_L001,CRL_SPN_62_S34_L001,CRL_SPN_53_S26_L001,spn_52_S25_L001,CRL_SPN_56_S28_L001," \
            "CRL_SPN_57_S29_L001,spn_55_S26_L001,CRL_SPN_54_S27_L001,CRL_SPN_58_S30_L001,CRL_SPN_66_S35_L001,CRL_SPN_69_S38_L001," \
            "CRL_SPN_68_S37_L001,CRL_SPN_67_S36_L001,Spn_81_S16_L001,Spn_80_S15_L001,Spn_79_S18_L001,Spn_82_S17_L001," \
            "CRL_SPN_77_S40_L001,CRL_SPN_78_S41_L001,CRL_SPN_76_S39_L001".split(",")
sample_names = "SF1916,SF1927,3277,3690,6487,2585,1192,2445,A308,EX3714,P276,6800,1453,927,SF4850,P766,P20011,A2258," \
               "A1645,P924,SF621,A1917,P776,7484,7861,5066,4998,B23927,B21333,B21699,SF5006,126,415,500,664,1801,1862," \
               "2061,2101,2220,EX4584,SF2320,B12510,3069,2285,B14465,2343,3668,EX7831,4267,4075,4249,4167,6178,4800,5118," \
               "5993,5515,5088,5926,6036,B25182,B25147,SF5143,6234,6494,6414,SF5506,7044,7079,B29157,7193,SF6046," \
               "B28457,EX11768".split(",")
script_file = open("prokka_wrapper2.sh",'w',encoding='utf-8',newline='\n')
print(len(sample_names),len(file_names))
for i in range(len(file_names)):
    file_id = file_names[i] + ".fasta"
    sample_id = sample_names[i]
    print(file_id,sample_id)
    cmd = f"sudo docker run -v $PWD:/data staphb/prokka prokka --prefix {sample_id} --addgenes --centre KIMS " \
          f"--genus Streptococcus --species pneumoniae --strain {sample_id} " \
          f"--cpus 8 --rfam /data/{file_id}" + '\n'
    print(cmd)
    script_file.write(cmd)


script_file.close()




