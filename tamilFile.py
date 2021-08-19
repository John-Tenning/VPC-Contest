import re

def tamilClean(tamil):

    # Removing the patterns
    remove_patterns = ['\d,\d', '\d-\d', '\d', r'\([^)]*\)', '\n', '”', '"', "'"]

    for pattern in remove_patterns:
        tamil = re.sub(pattern, '', tamil)

    # Removing the brackets
    for i in range(tamil.count('{')):
        start = tamil.index('{')
        end = tamil.index('}')
    
        tamil = tamil[:start] + tamil[end + 2:]
    
    tamil = tamil.replace('[]', '')

    return tamil


for section_num in range(22, 32):
    tamil_file = open(f'VPC-Contest\Resources\Mahabharatha-Adiparva-Section{section_num}-ta.txt', 'r', encoding='utf-8')

    tamil_contents = tamil_file.read()

    tamil_file.close()

    tamil_final = tamilClean(tamil_contents).split('.')

    combined_file = open(f'VPC-Contest\TamilFiles\Tamil-{section_num}.txt', 'w', encoding='utf-8')

    for i in range(len(tamil_final)):
        contents = f'{tamil_final[i].strip()}\n\n'
        combined_file.write(contents)

    combined_file.close()
