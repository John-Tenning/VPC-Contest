from indicnlp.tokenize import sentence_tokenize

def get_sentences_tokenized(src_file: str, lang: str) -> list:
    file = open(src_file, "r", encoding="utf-8")
    indic_string = file.read()
    sentences = sentence_tokenize.sentence_split(indic_string, lang)
    return sentences

for t in get_sentences_tokenized("./resources/Mahabharatha-Adiparva-Section23-en.txt", "en"):
    print('\n')
    print(t)

print("\n\n\n\n")

for t in get_sentences_tokenized("./resources/Mahabharatha-Adiparva-Section23-ta.txt", "ta"):
    print('\n')
    print(t)

