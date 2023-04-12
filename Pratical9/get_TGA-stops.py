f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
# ls1 is to record names of all the genes.
# ls2 is to record names of TGA_genes.
# seq1 is to combine the name and sequence
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
    if seq1[ls1[i]][-3:] == 'TGA':
        ls2.append(ls1[i])

new = open('TGA_genes.fa', 'w')
for i in range(len(ls2)):
    line1 = ls2[i]
    n = 0
    line2 = ''
    while n <= len(seq1[ls2[i]]):
        line2 += '\n' + seq1[ls2[i]][n:n+60]
        n = n + 60
    new.write('\n'+line1)
    new.write(line2)

f.close()
