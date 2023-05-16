stop_codons = input('input the stop codons of your sequence:')
if stop_codons == 'TAA':
    file = open('TAA_stop_genes.fa', 'w')
elif stop_codons == 'TAG':
    file = open('TAG_stop_genes.fa', 'w')
elif stop_codons == 'TGA':
    file = open('TGA_stop_genes.fa', 'w')

F = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
list1 = [] #for all names
list2 = [] #for stop codon names
seq1 = {}
for line in F:
    if line.startswith('>'):
        name = line.replace('_mRNA', '').split()[0]
        seq1[name] = ''
        list1.append(line.replace('_mRNA', '').split()[0])
    else:
        seq1[name] += line.replace('\n', '').strip()

for i in range(len(list1)):
    if seq1[list1[i]][-3:] == stop_codons:
        list2.append(list1[i])
for i in range(len(list2)):
    num = 0
    lenth = len(seq1[list2[i]])
    for a in range(3, lenth - 2):
        if seq1[list2[i]][a:a + 3] == stop_codons:
            num = num + 1
    line1 = list2[i] + "___"+"num:"+str(num)
    line2 = seq1[list2[i]]
    file.write('\n'+line1+'\n'+line2)

if stop_codons == 'TAA':
    x = open('TAA_stop_genes.fa')
elif stop_codons == 'TAG':
    x = open('TAG_stop_genes.fa')
elif stop_codons == 'TGA':
    x = open('TGA_stop_genes.fa')

F.close()
