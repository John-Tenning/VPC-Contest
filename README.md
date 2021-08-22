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
pip install -r requirements.txt

```

___

## Strategy

### 1. Analysing the Resources

* There were 10 sections of English and Tamil version of Mahabharatham in the repository [**resource**](https://github.com/John-Tenning/VPC-Contest/tree/main/resources)(numbered 22-31).

* The characters: parentheses, brackets and quotations, were considered unwanted.

* Tamil and English share the period/fullstop as the common sentence delimiter. But analysing the text in the files, it was found that it did not produce equal number of tamil sentences with respective translated english sentences.


### 2. Data Preprocessing

*  An approach of processing the data was taken by using self-produced Python programs. As the stratergy failed, the files were first cleaned (removal of "",[],(),'') and sentences were split using [**clean.py**](https://github.com/John-Tenning/VPC-Contest/blob/main/clean.py) module.  
* Once files were split, manual checking was done to merge and split sentences to make equal number of sentences in both English and Tamil files.  
* This manual checking is done so that each sentence of Tamil file corresponds to respective sentence of reference English file so that bleu score can be calculated, meaningfully. 
* The cleaned files were saved in local folder [**Data**](https://github.com/John-Tenning/VPC-Contest/tree/main/Data) as two different folders named Tamilfiles and Englishfiles.  
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

This step is only required if you are running the code on colab. Restart the runtime after running prev cell (to update). See this [**Stackoverflow Source**](https://stackoverflow.com/questions/57838013/modulenotfounderror-after-successful-pip-install-in-google-colaboratory).
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
```

### 5. BONUS

For the bonus part of the solution, we have approached the [**MBart-50**](https://huggingface.co/transformers/v3.5.1/model_doc/mbart.html) and [**Google Translate**](https://py-googletrans.readthedocs.io/en/latest/).

___
## Members

* TG Ashwin Kumar       [@tgashwinkumar](https://github.com/tgashwinkumar)
* Jeyam Palaniappan D   [@jeyam03](https://github.com/jeyam03)
* Samyuktha M S         [@samyuktha-12](https://github.com/samyuktha-12)
* Sashti Amar R A       [@John-Tenning](https://github.com/John-Tenning)
* Suvan Satyendira B    [@suvanbalu](https://github.com/suvanbalu)

___
