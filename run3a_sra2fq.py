import os
for line in open("GSM_info.tsv"):
	line=line.rstrip()
	sr=line.split("\t")[-1]
	sra_file=sr+"/"+sr+".sra"
	fq=sr+".fq.gz"
	if os.path.isfile(fq):
		print(sr+" skipped")
		continue
	os.system("fasterq-dump {0} -S -b 1000MB -m 20000MB -e 10 -o {1}.fq".format(sra_file,sr))
