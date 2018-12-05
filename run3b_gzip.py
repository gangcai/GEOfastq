import glob,os
for filename in glob.glob("SRX*.fq"):
	sample=filename
	os.system("nohup gzip {0} > {0}.log &".format(sample))

