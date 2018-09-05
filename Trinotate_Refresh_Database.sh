#!/bin/bash
export LC_ALL=C

Date=$(date +%s)
Date_now=$(date +%Y%m%d)
Database=$(awk '{if(match($0,".*Database=([^; ]*)",a))print a[1]}' software.config)
Trinotate=$(awk '{if(match($0,".*Trinotate=([^; ]*)",a))print a[1]}' software.config)

mkdir -p /tmp/Trinotate_Database_${Date}/
cd /tmp/Trinotate_Database_${Date}/

# 需 sslocal 建立隧道 
# 例 sslocal -s **.***.***.*** -p 8888 -k "password" -l 8989 -t 600 -m rc4-md5 &

proxychains4 ${Trinotate}/admin/Build_Trinotate_Boilerplate_SQLite_db.pl Trinotate${Date_now}

cp /tmp/Trinotate_Database_${Date}/* ${Database}/Trinotate/

cd ${Database}/Trinotate/

gunzip uniprot_sprot.dat.gz
makeblastdb -in uniprot_sprot.pep -dbtype prot
diamond makedb --db uniprot_sprot.pep --in uniprot_sprot.pep

gunzip Pfam-A.hmm.gz
hmmpress Pfam-A.hmm