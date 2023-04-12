import re

seq="ATGCAATCGACTACGATCTGAGAGGGCCTAA"

if len(re.findall("ATG",seq))==0:
  print ("coding sequence = 0")
else:
  seq2=re.findall('ATG[TGC][ATGC]*$',seq) #prevent the overlap of start codon and stop codon
  seq=''.join(seq2)
  b=re.findall("T[GA]A",seq)
  num1=len(b)
  c=re.findall("TAG",seq)
  num2=len(c)
  num=num1+num2
  print ("coding sequence =", num)


