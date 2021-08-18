from googletrans import Translator

# langs = googletrans.LANGUAGES

translator = Translator()

# f = open('test.txt', 'r', encoding='utf-8')
# g = open('gtr.txt', 'w')
s = "ஓ பாவங்களற்றவரே"

print(translator.translate(s, dest='en').text)

# g.close()
# f.close()

