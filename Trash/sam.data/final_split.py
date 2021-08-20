for num in range(22, 30, 2):
    old = open(f"VPC-Contest\sam.data\Mahabharatha-Adiparva-Section{num}-ta.txt", 'r', encoding='utf-8')
    tam = open(f"VPC-Contest\sam.data\TamilSplits\TamSplit-{num}.txt", 'w', encoding='utf-8')
    eng = open(f"VPC-Contest\sam.data\EnglishSplits\EngSplit-{num}.txt", 'w', encoding='utf-8')

    lines = old.read().split('\n')
    for i in range(lines.count('')):
        lines.remove('')
    
    for i in lines[::2]:
        tam.write(i)
        tam.write('\n')

    for i in lines[1::2]:
        eng.write(i)
        eng.write('\n')

    old.close()
    tam.close()
    eng.close()