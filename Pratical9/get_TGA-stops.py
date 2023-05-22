F = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
list1 = [] # for names of all the genes
list2 = [] # for names of TGA_genes
seq1 = {} # for combine the name and sequence
for line in F:
    if line.startswith('>'):
        name = line.replace('_mRNA', '').split()[0]
        seq1[name] = ''
        list1.append(line.replace('_mRNA', '').split()[0])
    else:
        seq1[name] += line.replace('\n', '').strip()

for i in range(len(list1)):
    if seq1[list1[i]][-3:] == 'TGA':
        list2.append(list1[i])

new = open('TGA_genes.fa', 'w')
for i in range(len(list2)):
    line1 = list2[i]
    n = 0
    line2 = ''
    while n <= len(seq1[list2[i]]):
        line2 += '\n' + seq1[list2[i]][n:n+60]
        n = n + 60
    new.write('\n'+line1)
    new.write(line2)

F.close()
