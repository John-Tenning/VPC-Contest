import re

def englishClean(english):

    # Removing the section name
    english_lines = english.split('\n')
    if english_lines[0][0] == 'S':
        english_lines = english_lines[2:]

    english = ''.join(english_lines)

    # Removing the patterns
    remove_patterns = ['p. \d\d', 'viz.,', 'i.e.,', 'paragraph continues', 'Footnotes', '"', "'", r'\([^)]*\)']

    for pattern in remove_patterns:
        english = re.sub(pattern, '', english)
    
    # Removing the footnotes
    english_sents = english.split('.')
    english = '.'.join(english_sents[:-2])
    
    return english


for section_num in range(22, 32):
    english_file = open(f'VPC-Contest\Resources\Mahabharatha-Adiparva-Section{section_num}-en.txt', 'r', encoding='utf-8')

    english_contents = english_file.read()

    english_file.close()

    english_final = englishClean(english_contents).split('.')

    combined_file = open(f'VPC-Contest\EnglishFiles\English-{section_num}.txt', 'w', encoding='utf-8')

    for i in range(len(english_final)):
        contents = f'{english_final[i].strip()}\n\n'
        combined_file.write(contents)

    combined_file.close()
