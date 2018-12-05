import os
for line in open("../SRA/GSM_info.2.tsv"):
	line=line.rstrip()
	sr=line.split("\t")[-2]
	sra_file="../SRA/"+sr+"/"+sr+".sra"
	fq=sr+".fq.gz"
	if os.path.isfile(fq):
		print(sr+" skipped")
		continue
	os.system("fasterq-dump {0} -S -b 1000MB -m 20000MB -e 10 -o {1}".format(sra_file,sr))
