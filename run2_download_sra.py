import os
for line in open("GSM_info.tsv"):
	line=line.rstrip()
	sr=line.split("\t")[-1]
	os.system("prefetch -O {0} {0}".format(sr))

