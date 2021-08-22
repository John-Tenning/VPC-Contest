# Venmurasu-Contest-August-2021

## Overview

This repository is a solution for the [**Aug 2021 - Venmurasu Programming Contest**](https://github.com/venmurasu-programming-team/Aug2021-contest) .  
The objective of the solution is to translate Tamil contents to English using NLP models like **Indictrans** and **Mbart50_m2m** to get a basic understanding of NLP models.  

___
## Gearing-Up
Install all the dependencies required for this solution via requirements.txt
```

git clone https://github.com/John-Tenning/VPC-Contest.git
cd ./VPC-Contest
pip install sacrebleu

```
[Main.py](https://github.com/John-Tenning/VPC-Contest/blob/main/main.py) is the driver file for the solution.
___

## Strategy

### 1. Analysing the Resources

* There were 10 sections of English and Tamil version of Mahabharatham in the repository [**resource**](https://github.com/John-Tenning/VPC-Contest/tree/main/resources)(numbered 22-31).

* The characters: parentheses, brackets and quotations, were considered unwanted.

* Tamil and English share the period/fullstop as the common sentence delimiter. But analysing the text in the files, it was found that it did not produce equal number of tamil sentences with respective translated english sentences.


### 2. Data Preprocessing

*  An approach of processing the data was taken by using self-produced Python programs. As the stratergy failed, the files were first cleaned (removal of "",[],(),'') and sentences were split automatically using [**clean.py**](https://github.com/John-Tenning/VPC-Contest/blob/main/clean.py) module and those files were saved in the repo [**clean**](https://github.com/John-Tenning/VPC-Contest/tree/main/Clean)
* Once files were split, manual checking was done to merge and split sentences to make equal number of sentences in both English and Tamil files.  
* This manual checking is done so that each sentence of Tamil file corresponds to respective sentence of reference English file so that bleu score can be calculated, meaningfully. 
* The cleaned files were saved in local folder [**Data**](https://github.com/John-Tenning/VPC-Contest/tree/main/Data) as two different folders named TamilCleanfiles and EnglishCleanfiles.  
* They were saved in different folders because it makes file parsing for translation and calculating Bleu score easy.  

### 3. Translating Files

#### Requirements-for-translation

```
git clone https://github.com/AI4Bharat/indicTrans.git
%cd indicTrans
git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git
git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git
git clone https://github.com/rsennrich/subword-nmt.git
%cd ..

pip install sacremoses pandas mock sacrebleu tensorboardX pyarrow indic-nlp-library
pip install mosestokenizer subword-nmt

git clone https://github.com/pytorch/fairseq.git
%cd fairseq

pip install --editable ./
%cd ..
```

Restart the runtime after running prev cell (to update) if you are using Colab. See this [**Stackoverflow Source**](https://stackoverflow.com/questions/57838013/modulenotfounderror-after-successful-pip-install-in-google-colaboratory).
This import will not work without restarting runtime abstract.

```
wget https://storage.googleapis.com/samanantar-public/V0.2/models/indic-en.zip
unzip indic-en.zip

%cd indicTrans
```

We'll be using specific modules for library *fairseq*.

```
from fairseq import checkpoint_utils, distributed_utils, options, tasks, utils
```

You can find the sample Collab Notebook, [**here**](https://colab.research.google.com/drive/1UByeetC68GibBxZq_wxVu4JxqVmdWvzY?usp=sharing).

### 4. Calculating Bleu score

* BLEU is one of the standard measures to calculate the accuracy and quality of the Machine Translation system. 
* BLEU calculations are independent of the translation model/framework used.
* Quotations tend to increase the BLEU score, according to our solution. But since both these languages hold meaning for quotations in their grammar, we couldn't ignore it.
* The file [**bleu.py**](https://github.com/John-Tenning/VPC-Contest/blob/main/bleu.py) is used to calculate BLEU score

Reference: [**Computing BLEU Score for Machine Translation**](https://blog.machinetranslation.io/compute-bleu-score/)

The Average BLEU score for the file is given below :
```
File 22 : 10.926209425092425
File 23 : 9.389193875582405
File 24 : 8.554833408247244
File 25 : 8.400111401819778
File 26 : 8.765172826342521
File 27 : 7.580158606214755
File 28 : 6.894618163743909
File 29 : 10.812070278960649
File 30 : 8.962625883376859
File 31 : 6.090987459345413

Average Score : 8.637598132872595
```
*As this round doesn't focus of BLEU score , no imporvement in datasets and model is done to improve BLEU score*

### 5. BONUS

For the bonus part of the solution, we have approached the [**MBart-50**](https://huggingface.co/transformers/v3.5.1/model_doc/mbart.html) and [**Google Translate**](https://py-googletrans.readthedocs.io/en/latest/).

The following code is used to translate using Mbart50_m2m model.

```
pip install easynmt
from easynmt import EasyNMT
model = EasyNMT('mbart50_m2m')
#create a folder tamil_files
for ind in range(22,32):
  tamil_open = open(f"/content/tamil_files/{ind} - tam.txt",'r')

  t_read = tamil_open.readlines()
  ta_sent=[]
  for i in range(len(t_read)):
    if t_read[i]!='\n':
      ta_sent.append(t_read[i].rstrip("\n"))
      
  max_len_split=[]
  translate=[]
  for i in range(len(ta_sent)):
    k=ta_sent[i]
    if len(k)<723:
      translate.append(model.translate(k,target_lang='en'))
    if len(k)>=723:
      k=k.split()
      max_len_split.append(''.join(k[:len(k)//2]))
      max_len_split.append(''.join(k[len(k)//2:len(k)]))
      ttemp=((model.translate(k,target_lang='en')))
      stemp=' '.join(ttemp)
      translate.append([stemp])

#create a folder called translate

  write_file = open(f"/content/translate/{ind} - translate.txt",'w')

  for i in translate:
    write_file.writelines(i)
    write_file.write('\n\n')

  write_file.close()
  tamil_open.close()
  ```
  **The average BLEU score for Mbart-50 is :** 8.66 (file wise score [here](https://github.com/John-Tenning/VPC-Contest/blob/main/bonus_mbart50_m2m/mbart_bleu.txt))  
  
  The second approach is done using Google translate.
  
  ```
  pip install deep_translator
  from deep_translator import GoogleTranslator
  for ind in range(22,32):
  tamil_open = open(f"/content/tamil_files/{ind} - tam.txt",'r')

  t_read = tamil_open.readlines()
  ta_sent=[]
  for i in range(len(t_read)):
    if t_read[i]!='\n':
      ta_sent.append(t_read[i].rstrip("\n"))
      
  max_len_split=[]
  translate=[]
  if (len(ta_sent)<=5000):
    for i in range(len(ta_sent)):
      k=ta_sent[i]
      translate.append(GoogleTranslator(source='tamil', target='en').translate(k))
  else:
    for i in range(5000):
      k=ta_sent[i]
      translate.append(GoogleTranslator(source='tamil', target='en').translate(k))
    for j in range(5000,len(ta_sent)):
       k=ta_sent[j]
       translate.append(GoogleTranslator(source='tamil', target='en').translate(k))

  write_file = open(f"/content/translate/{ind} - translate.txt",'w')

  for i in translate:
    write_file.writelines(i)
    write_file.write('\n\n')
```
 **The average BLEU score for GoogleAPI is :** 9.51 (file wise score [here](https://github.com/John-Tenning/VPC-Contest/blob/main/bonus_googleapi/googleapi_bleu.txt))  

* The translated files using MBart Model can be found in the folder [**bonus_mbart50_m2m**](https://github.com/John-Tenning/VPC-Contest/tree/main/bonus_mbart50_m2m)
* The translated files uding Google translate can be found in the folder [**bonus_googleapi**](https://github.com/John-Tenning/VPC-Contest/tree/main/bonus_googleapi)
___
## Members

* TG Ashwin Kumar       [@tgashwinkumar](https://github.com/tgashwinkumar)
* Jeyam Palaniappan D   [@jeyam03](https://github.com/jeyam03)
* Samyuktha M S         [@samyuktha-12](https://github.com/samyuktha-12)
* Sashti Amar R A       [@John-Tenning](https://github.com/John-Tenning)
* Suvan Sathyendira B    [@suvanbalu](https://github.com/suvanbalu)

___
