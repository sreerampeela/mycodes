file1 = open("gene_presence_absence_invasive.csv",'r')
file2 = open("sero_test6.txt",'w',newline='\n',encoding='utf-8')
# file3 = open("file_copier4.txt",'w',newline='\n')
ids = file1.readlines()
for id in ids:
    id = id.rstrip()
    oldr1 = id + "_1.fastq.gz"
    oldr2 = id + "_2.fastq.gz"
    read1 = id + "_S1_L001_R1_001.fastq.gz"
    read2 = id + "_S1_L001_R2_001.fastq.gz"
    
    cmd = "docker run --rm=True -v $PWD:/data quay.io/biocontainers/fastp:0.20.1--h8b12597_0 fastp " \
          "-i /data/{} -I /data/{} " \
          "-o /data/{}_fastp_S1_L001_R1_001.fastq.gz " \
          "-O /data/{}_fastp_S1_L001_R2_001.fastq.gz".format(oldr1,oldr2,id,id) + '\n'
    cmd2 = "docker run --rm=True -v $PWD:/data staphb/cdc-spn SPN_Serotyper.pl " \
          "-1 /data/{}_fastp_S1_L001_R1_001.fastq.gz" \
          " -2 /data/{}_fastp_S1_L001_R2_001.fastq.gz -n {} -o /data/test_cdcpipeline3/{} " \
          "-r /data/SPN_Reference_DB/SPN_Sero_Gene-DB_Final.fasta".format(id,id,id,id) + '\n'
    # file3.write(cmd1)
    # print(cmd1)
    file2.write(cmd)
    file2.write(cmd2)


file2.close()
