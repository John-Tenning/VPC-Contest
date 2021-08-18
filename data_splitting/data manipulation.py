
import re
for i in range(23,32):
    f = open(f'..\\resources\\Mahabharatha-Adiparva-Section{i}-ta.txt', 'r', encoding='utf-8')
    g = open(f'..\\resources\\Mahabharatha-Adiparva-Section{i}-en.txt', 'r', encoding='utf-8')
    tamil = f.read()
    english = g.read()

    tamil = ''.join(re.findall('[^()]', tamil))
    tamil = re.sub('\d,\d', '', tamil)
    tamil = re.sub('\d-\d', '', tamil)
    tamil = re.sub('\d', '', tamil)

    english = ''.join(re.findall("[^()]",english))
    english = ''.join(english.split('\n')[2:-2])
    english = re.sub('p. \d\d', ' ', english)
    english = re.sub('viz., ', '', english)
    english = re.sub('i.e., ', '', english)
    english = re.sub('paragraph continues', '', english)
    english = re.sub('"', '', english)
    english = re.sub("'", "", english)

    h = open(f'clean_{i}.txt', 'w', encoding='utf-8')

    english = english.split('.')
    tamil = tamil.split('.')

    print(f"English sentences : {len(english)}  Tamil sentences :{len(tamil)}")
    m = min(len(english), len(tamil))

    for i in range(m):
        h.write(tamil[i])
        h.write('\n')
        h.write(english[i])
        h.write('\n\n')

    f.close()
    g.close()
    h.close()

