import re

def tamilClean(tamil : str) -> str:
    tamil = tamil.split('\n')
    tamil = "\n".join(tamil)
    # Removing the patterns
    remove_patterns = ['\d,\d', '\d-\d', '\d', r'\([^)]*\)', '”', '"', "'"]

    for pattern in remove_patterns:
        tamil = re.sub(pattern, '', tamil)

    # Removing the brackets
    for i in range(tamil.count('{')):
        start = tamil.index('{')
        end = tamil.index('}')
    
        tamil = tamil[:start] + tamil[end + 2:]
    
    tamil = tamil.replace('[]', '')

    return tamil

def quotes_clean(english : str) -> str :
    remove_patterns = ['p. \d\d', 'viz.,', 'i.e.,', 'paragraph continues', 'Footnotes', '"', "'", r'\([^)]*\)']

    for pattern in remove_patterns:
        english = re.sub(pattern, '', english)
    
    return english

def englishClean(english : str) -> str:
    # Removing the section name
    # print(english)
    english_lines = english.split('\n')
    if english_lines[0].startswith("SECTION"):
        english_lines = english_lines[2:]

    english = '.'.join(english_lines)

    # Removing the patterns
    remove_patterns = ['p. \d\d', 'viz.,', 'i.e.,', 'paragraph continues', 'Footnotes', '"', "'", r'\([^)]*\)']

    for pattern in remove_patterns:
        english = re.sub(pattern, '', english)
    
    # Removing the footnotes
    english_sents = english.split('.')
    english = '\n'.join(english_sents[:-2])

    # english = english.replace('\n\n' , '\n')
    
    return english