import glob,os
for sra_file in glob.glob("./*/*.sra"):
	print(sra_file)
	os.system("fastq-dump --gzip --split-files {0}".format(sra_file))
