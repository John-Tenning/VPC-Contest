from googletrans import Translator

def gtranslate(src_file, dest_file, dest_lang='en') -> None:
    translator = Translator()
    with open(src_file, 'r', encoding='utf-8') as src:
        for line in src:
            translator.translate(line, dest=dest_lang).text.encode('utf-8')
            with open(dest_file, 'a', encoding='utf-8') as dest:
                dest.write(translator.translate(line, dest=dest_lang).text.encode('utf-8'))
    return