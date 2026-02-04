input()
dna = list(input().strip())

rule = {
    'AA':'A','AC':'A','AG':'C','AT':'G',
    'CA':'A','CC':'C','CG':'T','CT':'G',
    'GA':'C','GC':'T','GG':'G','GT':'A',
    'TA':'G','TC':'G','TG':'A','TT':'T'
}

while len(dna) > 1:
    a = dna.pop()
    b = dna.pop()
    dna.append(rule[b + a])

print(dna[0])