import blosum as bl
f1 = open('ACE2_human.fa')
f2 = open('ACE2_mouse.fa')
f3 = open('ACE2_cat.fa')

for line in f1:
  if not line.startswith('>'):
    h=line.strip()
for line in f2:
  if not line.startswith('>'):
    m=line.strip()
for line in f3:
  if not line.startswith('>'):
    c=line.strip()

matrix=bl.BLOSUM(62)
def COMPARE(seq1,seq2):
  val=0
  for n in range(len(seq1)):
    i = seq1[n]
    j = seq2[n]
    val = val + matrix[i][j]
  return val

print("human with mouse is %d" %COMPARE(h,m))
print("human with cat is %d" %COMPARE(h,c))
print("cat with mouse is %d" %COMPARE(c,m))


def compare(seq1,seq2):
  percentage = 0
  edit_distance = 0 #set initial distance as zero
  for i in range(len(seq1)): #compare each amino acid
    if seq1[i]==seq2[i]:
      edit_distance += 1 #add a score 1 if amino acids are different
      percentage=edit_distance/(len(seq1))
  return percentage


print("human with mouse is %f%%" %(compare(h,m)*100))
print("human with cat is %f%%" %(compare(h,c)*100))
print("cat with mouse is %f%%" %(compare(c,m)*100))
