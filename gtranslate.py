#!/usr/bin/python
# -*- coding: utf-8 -*-
from googletrans import Translator

def gtranslate(src_file: str, dest_file: str, dest_lang:str='en') -> None:
    translator = Translator()
    with open(src_file, 'r', encoding='utf-8') as src:
        for line in src:
            translator.translate(line, dest=dest_lang).text.encode('utf-8')
            with open(dest_file, 'a', encoding='utf-8') as dest:
                dest.write(translator.translate(line, dest=dest_lang).text.encode('utf-8'))
    return

def gtranslate_sentence(src_text:str, dest_lang:str='en') -> str:
    translator = Translator()
    return translator.translate(src_text, dest=dest_lang).text.encode('utf-8')