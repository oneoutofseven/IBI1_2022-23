import re

def calculate(DNA):
  dna_arrange=DNA.upper() #make the DNA all upper case
  seq1 = re.findall('ATG([ATCG]*)TGA',dna_arrange)
  seq=''.join(seq1)
  percentage= len(seq)/len(DNA)
  if percentage > 0.5:
    print("it is protein-coding")
  elif percentage < 0.1:
    print("it is non-coding")
  else:
    print("it is unclear")
  return percentage

DNA="atgtcaTatcAttgcatgtcagtcagttga"
calculate(DNA)


