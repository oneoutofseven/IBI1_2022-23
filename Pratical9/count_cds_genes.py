stop_codons = input('input the stop codons of your sequence:')
if stop_codons == 'TAA':
    file = open('TAA_stop_genes.fa', 'w')
elif stop_codons == 'TAG':
    file = open('TAG_stop_genes.fa', 'w')
elif stop_codons == 'TGA':
    file = open('TAG_stop_genes.fa', 'w')
f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
ls1 = []
ls2 = []
seq1 = {}
for line in f:
    if line.startswith('>'):
        name = line.replace('_mRNA', '').split()[0]
        seq1[name] = ''
        ls1.append(line.replace('_mRNA', '').split()[0])
    else:
        seq1[name] += line.replace('\n', '').strip()

for i in range(len(ls1)):
    if seq1[ls1[i]][-3:] == stop_codons:
        ls2.append(ls1[i])
for i in range(len(ls2)):
    num = 0
    lenth = len(seq1[ls2[i]])
    for e in range(3, lenth - 2, 1):
        if seq1[ls2[i]][e:e + 3] == stop_codons:
            num = num + 1
    line1 = ls2[i] + "___"+"num:"+str(num)
    line2 = seq1[ls2[i]]
    file.write('\n'+line1+'\n'+line2)

if stop_codons == 'TAA':
    x = open('TAA_stop_genes.fa')
elif stop_codons == 'TAG':
    x = open('TAG_stop_genes.fa')
elif stop_codons == 'TGA':
    x = open('TAG_stop_genes.fa')

f.close()
