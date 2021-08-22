# Venmurasu-Contest-August-2021

## Overview

This repository is a solution for the [**Aug 2021 - Venmurasu Programming Contest**](https://github.com/venmurasu-programming-team/Aug2021-contest) .  
The objective of the solution is to translate Tamil contents to English using NLP models like **Indictrans** and **Mbart50_m2m** to get a basic understanding of NLP models.  

## Gearing-Up
Run this command in a terminal to setup virtual environment for our repository
```
python -m venv virtualenv
virtualenv/Scripts/activate

git clone https://github.com/John-Tenning/VPC-Contest.git
pip install -r requirements.txt

```
## Strategy

### 1. Analysing the Resources

There are 10 sections of English and Tamil version of Mahabharatham in the repo [resource](https://github.com/John-Tenning/VPC-Contest/tree/main/resources).   
There are unwanted characters like brackets and quotes.  
Both the files doesn't give equal number of sentences when spliting it when using fullstop as delimiter.  

### 2. Cleaning and Spliting of Datasets

As programatic spliting of files doesn't give proper result , the files are first cleaned (removal of "",[],(),'') and sentences are split using [clean.py](https://github.com/John-Tenning/VPC-Contest/blob/main/clean.py) module.  
Once files are splitted,manual checking is done to merge and split sentences to make equal number of sentences in both English and Tamil file.  
This manual checking is done so that each sentence of Tamil file corresponds to sentence of English file so that bleu score can be calculated. 
The cleaned files are saved in repo [Align_files] as two different folders named Tamilfiles and Englishfiles.  
They are saved in different folders because it makes file parsing to translation and calculating Bleu score easy.  

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

# this step is only required if you are running the code on colab
# restart the runtime after running prev cell (to update). See this -> https://stackoverflow.com/questions/57838013/modulenotfounderror-after-successful-pip-install-in-google-colaboratory
# this import will not work without restarting runtime

from fairseq import checkpoint_utils, distributed_utils, options, tasks, utils

wget https://storage.googleapis.com/samanantar-public/V0.2/models/indic-en.zip
unzip indic-en.zip

%cd indicTrans
```
Sample Colab Notebook [here](https://colab.research.google.com/drive/1UByeetC68GibBxZq_wxVu4JxqVmdWvzY?usp=sharing)

### 4. Calculating Bleu score


### 5. BONUS

#### Translation
#### Bleu Score
