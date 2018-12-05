import glob,os
for filename in glob.glob("SRX*"):
	sample=filename
	os.system("mv {0} {0}.fq".format(sample))
	os.system("nohup gzip {0}.fq > {0}.log &".format(sample))

