# GEOfastq
Download Fastq format files from GEO.

# Requirement
R packages:
SRAdb
GEOquery

Python

sratoolkit

# Usage
$Rscript run1_extract_GEOinfo.R #get GSM, SRA information
$python run2_download_sra.py #download SRA
$python run3a_sra2fq.py #convert to fq
$python run3b_gzip.py #gzip
