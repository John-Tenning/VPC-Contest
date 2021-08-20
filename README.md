# VPC-Contest-August-2021

```
python -m venv virtualenv
virtualenv/Scripts/activate
pip install -r requirements.txt
python Parser.py

```

## Repository requirements for translation

```
# clone the repo for running evaluation
git clone https://github.com/AI4Bharat/indicTrans.git
%cd indicTrans
# clone requirements repositories
git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git
git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git
git clone https://github.com/rsennrich/subword-nmt.git
%cd ..

# Install the necessary libraries
pip install sacremoses pandas mock sacrebleu tensorboardX pyarrow indic-nlp-library
pip install mosestokenizer subword-nmt
# Install fairseq from source
git clone https://github.com/pytorch/fairseq.git
%cd fairseq
# !git checkout da9eaba12d82b9bfc1442f0e2c6fc1b895f4d35d
pip install --editable ./
%cd ..

# this step is only required if you are running the code on colab
# restart the runtime after running prev cell (to update). See this -> https://stackoverflow.com/questions/57838013/modulenotfounderror-after-successful-pip-install-in-google-colaboratory

# this import will not work without restarting runtime
from fairseq import checkpoint_utils, distributed_utils, options, tasks, utils

# download the indictrans model

# downloading the indic-en model
wget https://storage.googleapis.com/samanantar-public/V0.2/models/indic-en.zip
unzip indic-en.zip

# downloading the en-indic model
# !wget https://storage.googleapis.com/samanantar-public/V0.2/models/en-indic.zip
# !unzip en-indic.zip

# # downloading the indic-indic model
# !wget https://storage.googleapis.com/samanantar-public/V0.3/models/m2m.zip
# !unzip m2m.zip

%cd indicTrans
```
Sample Colab Notebook [here](https://colab.research.google.com/drive/1UByeetC68GibBxZq_wxVu4JxqVmdWvzY?usp=sharing)

