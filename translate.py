from indicTrans.inference.engine import Model

indic2en_model = Model(expdir='../indic-en')

def translate(tamil_file : str,translate_source : str) -> None :
    '''
    Takes cleaned Tamil files as input and translate it to English using AI4bharath NLP model 
    For setup of the required packages check readme of "https://github.com/John-Tenning/VPC-Contest"
    '''
    tamil_open = open(tamil_file,'r')

    tamil_read = tamil_open.readlines()
    tamil_sentence=[]
    for i in range(len(tamil_read)):
        if tamil_read[i]!='\n':
            tamil_sentence.append(tamil_read[i].rstrip("\n"))

    max_len_split=[]
    translate=[]
    for i in range(len(tamil_sentence)):
        k=tamil_sentence[i]
        if len(k)<723:
            translate.append(indic2en_model.batch_translate([k], 'ta', 'en'))

        if len(k)>=723:   #code for manual splitting of sentences more than 723 words. check "https://github.com/AI4Bharat/indicTrans/issues/21"
            k=k.split()
            max_len_split.append(''.join(k[:len(k)//2]))
            max_len_split.append(''.join(k[len(k)//2:len(k)]))
            trans_temp=(indic2en_model.batch_translate(max_len_split, 'ta', 'en'))
            string_temp=' '.join(trans_temp)
            translate.append([string_temp])

    write_file = open(translate_source,'w')

    for i in translate:
        write_file.writelines(i)
        write_file.write('\n')

    write_file.close()
    tamil_open.close()