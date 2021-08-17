from indicnlp.tokenize import sentence_tokenize

class SentParser:
    def __init__(self):
        pass

file = open("test.txt", "r", encoding="utf-8")
indic_string = file.read()
# print(indic_string)
sentences = sentence_tokenize.sentence_split(indic_string, lang='ta')
for t in sentences:
    print('\n')
    print(t)

