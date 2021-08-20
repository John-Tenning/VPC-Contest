from clean import tamilClean , englishClean
from bleu import get_sentence_bleu_score_from_file
# from gtranslate import gtranslate_sentence

# print(gtranslate_sentence("""ஒருமுறை கத்ரு, வினதையை அழைத்தாள்.வினதை அவளை விழுந்து வணங்கி எழுந்ததும், கத்ரு அவளது மகனின் முன்னிலையிலேயே, ஓ மென்மையான வினதையே, கடலுக்கு நடுவிலே, யாரும் அணுகமுடியாத ஓர் இடத்திலே, அழகானதும், இன்பம் தருவதுமான பாம்புகளின் வசிப்பிடம் ஒன்று இருகிறது."""))

#cleaning tamil files
def clean_tamil_files() -> None:
    for section_num in range(22, 32):
        tamil_file = open(f'Clean_Files/EnglishCleanfiles/{section_num} - eng.txt', 'r', encoding='utf-8')

        tamil_contents = tamil_file.read()

        tamil_file.close()

        tamil_final = tamilClean(tamil_contents).split('.')

        cleaned_file = open(f'VPC-Contest\TamilFiles\Tamil-{section_num}.txt', 'w', encoding='utf-8')

        for i in range(len(tamil_final)):
            contents = f'{tamil_final[i].strip()}\n\n'
            cleaned_file.write(contents)

        cleaned_file.close()
        return


#cleaning english files
def clean_english_files() -> None:
    for section_num in range(22, 32):
        english_file = open(f'Clean_Files/EnglishCleanfiles/{section_num} - eng.txt', 'r', encoding='utf-8')

        english_contents = english_file.read()

        english_file.close()

        english_final = englishClean(english_contents).split('.')

        cleaned_file = open(f'VPC-Contest\EnglishFiles\English-{section_num}.txt', 'w', encoding='utf-8')

        for i in range(len(english_final)):
            contents = f'{english_final[i].strip()}\n\n'
            cleaned_file.write(contents)

        cleaned_file.close()
        return

#finding bleu_scores
def find_bleu_score() -> None:
    for i in range(22,32) :
        get_sentence_bleu_score_from_file(f"/content/English-{i}.txt" ,f"/content/translate-{i}.txt" ,f"/content/Results/res-{i}.txt")

    return


#Step 1 => To clean english and tamil files , removing brackets etc

clean_english_files()
clean_tamil_files()

#Step2 => To translate the Tamil files

#translate()

#Step 3 => To find the bleu score
find_bleu_score()
