from googletrans import Translator

# langs = googletrans.LANGUAGES

translator = Translator()

f = open('VPC-Contest\Resources\Mahabharatha-Adiparva-Section22-ta.txt', 'r', encoding='utf-8')
g = open('gtr.txt', 'w')
s = f.read()

g.write(translator.translate(s, dest='en').text)

g.close()
f.close()
