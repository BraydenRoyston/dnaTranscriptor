DNA = input("Enter your sequence of DNA here:")
mRNA = ""
for i in range(len(DNA)):
    if DNA[i] == 'A':
        mRNA = mRNA+'U'
    if DNA[i] == 'G':
        mRNA = mRNA+'C'
    if DNA[i] == 'C':
        mRNA = mRNA + 'G'
    if DNA[i] == 'T':
        mRNA = mRNA + 'A'

print(DNA)
print(mRNA)
