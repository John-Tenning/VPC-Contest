import re

def tamilClean(tamil):
    tamil = ''.join(re.findall('[^()]', tamil))

    remove_patterns = ['\d,\d', '\d-\d', '\d', '\n']

    for pattern in remove_patterns:
        tamil = re.sub(pattern, '', tamil)
    
    return tamil


def englishClean(english):
    english = ''.join(english.split('\n')[2:-2])

    remove_patterns = ['p. \d\d', 'viz.,', 'i.e.,', 'paragraph continues', 'Footnotes', '"', "'"]

    for pattern in remove_patterns:
        english = re.sub(pattern, '', english)
    
    return english


for section_num in range(22, 32):
    tamil_file = open(f'Venmurasu\Resources\Mahabharatha-Adiparva-Section{section_num}-ta.txt', 'r', encoding='utf-8')
    english_file = open(f'Venmurasu\Resources\Mahabharatha-Adiparva-Section{section_num}-en.txt', 'r', encoding='utf-8')

    tamil_contents = tamil_file.read()
    english_contents = english_file.read()

    tamil_file.close()
    english_file.close()

    tamil_final = tamilClean(tamil_contents).split('.')
    english_final = englishClean(english_contents).split('.')

    print(len(tamil_final), len(english_final))
    length = min(len(tamil_final), len(english_final))

    combined_file = open(f'Venmurasu\CombinedFiles\Combined-{section_num}.txt', 'w', encoding='utf-8')

    line = 1
    for i in range(length):
        contents = f'Line{line}: {tamil_final[i].strip()}\n{english_final[i].strip()}\n\n'
        combined_file.write(contents)
        line += 1

    combined_file.close()
