from clean import tamilClean , englishClean
from translate import eng_translate
from bleu import get_sentence_bleu_score_from_file
# from gtranslate import gtranslate_sentence

# print(gtranslate_sentence("""ஒருமுறை கத்ரு, வினதையை அழைத்தாள்.வினதை அவளை விழுந்து வணங்கி எழுந்ததும், கத்ரு அவளது மகனின் முன்னிலையிலேயே, ஓ மென்மையான வினதையே, கடலுக்கு நடுவிலே, யாரும் அணுகமுடியாத ஓர் இடத்திலே, அழகானதும், இன்பம் தருவதுமான பாம்புகளின் வசிப்பிடம் ஒன்று இருகிறது."""))


if __name__ == "__main__":
    #Step 1 => To clean english and tamil files , removing brackets etc
    for section_num in range(22, 32):
        tamil_file = open(f'Align_Files/TamilCleanfiles/{section_num} - tamil.txt', 'r', encoding='utf-8')

        tamil_contents = tamil_file.read()

        tamil_file.close()

        tamil_final = tamilClean(tamil_contents).split('.')

        cleaned_file = open(f'Data/FinalTamilFiles/Tamil-{section_num}.txt', 'w', encoding='utf-8')

        for i in range(len(tamil_final)):
            contents = f'{tamil_final[i].strip()}\n\n'
            cleaned_file.write(contents)

        cleaned_file.close()


    #cleaning english files
    for section_num in range(22, 32):
        english_file = open(f'Align_Files/EnglishCleanfiles/{section_num} - eng.txt', 'r', encoding='utf-8')

        english_contents = english_file.read()

        english_file.close()

        english_final = englishClean(english_contents).split('.')

        cleaned_file = open(f'Data/FinalEnglishFiles/English-{section_num}.txt', 'w', encoding='utf-8')

        for i in range(len(english_final)):
            contents = f'{english_final[i].strip()}\n\n'
            cleaned_file.write(contents)

        cleaned_file.close()
    
    
    #Step2 => To translate the Tamil files

    for section_num in range(22,32):
        eng_translate(f'Data/FinalTamilFiles/Tamil-{section_num}.txt',f'Translate/Translate-{section_num}.txt')


    #finding bleu_scores
    #Step 3 => To find the bleu score

    for section_num in range(22,32) :
        get_sentence_bleu_score_from_file(f'Data/FinalEnglishFiles/Eng-{section_num}.txt' ,f'Translate/Translate-{section_num}.txt' ,f"/content/Results/res-{section_num}.txt")


