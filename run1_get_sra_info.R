library("SRAdb")
library("GEOquery")

#old with bug
#gse=getGEO("GSE57249")
#gsms=gse[[1]]$geo_accession

gse=getGEO("GSE57249",GSEMatrix=F)
gsms=names(GSMList(gse))
#Meta(gsm)
results=""
i=0
for(gsm_id in gsms){
  i=i+1
  gsm=getGEO(gsm_id)
  gse_id=gsm@header$series_id
  sra=gsm@header$relation[2][1]
  sra_id=strsplit(sra,"=")[[1]][2]
  if(i==1){
   results=c(gse_id,gsm_id,sra_id)
  }else{
   results=rbind(results,c(gse_id,gsm_id,sra_id))

 }
write.table(results,file="gse_info.tsv",sep="\t",col.names=F,row.names=F,quote=F)
  
}
