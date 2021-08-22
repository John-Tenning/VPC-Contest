"""@package bleu
Documentation for this module.

More details.
"""

import sacrebleu
from sacremoses import MosesDetokenizer

def get_bleu_score_from_file(predict_text_file: str, test_text_file: str) -> float:
    """
    This function takes a whole text file as input and returns the BLEU score. 
    For reference, see https://blog.machinetranslation.io/compute-bleu-score/ 
    @param  predict_text_file   The predicted text file.
    @param  test_text_file  The test text file.
    @return The BLEU score in float.
    """
    detokenizer = MosesDetokenizer(lang='en')
    refs = []
    with open(test_text_file, 'r') as test:
        for line in test:
            refs.append(detokenizer.detokenize(line.strip().split()))
    print("\nTest file - first sentence: ", refs[0])
    refs = [refs]
    preds = []
    with open(predict_text_file, 'r') as pred:
        for line in pred:
            preds.append(detokenizer.detokenize(line.strip().split()))
    print("\nPredicted file - first sentence: ", preds[0])    
    bleu = sacrebleu.corpus_bleu(preds, refs)
    return bleu.score

def get_sentence_bleu_score_from_file(predict_text_file: str, test_text_file: str, bleu_evaluate_file: str , index: int) -> None:

    """
    This function takes a whole text file as input ,splits them into list of sentences and finds the blue score for individual snetences and return the file that contains average of all BLEU scores. 
    For reference, see https://blog.machinetranslation.io/compute-bleu-score/ 
    @param  predict_text_file   The predicted text file.
    @param  test_text_file  The test text file.
    @param  bleu_evaluate_file_file  The file to store average.
    @param  index  indexof the reference_file.
    @return None.
    """

    score=count=0
    detokenizer = MosesDetokenizer(lang='en')

    refs = []
    with open(test_text_file, 'r') as test:
        for line in test:
            refs.append(detokenizer.detokenize(line.strip().split()))
    print("\nTest file - first sentence: ", refs[0])

    preds = []
    with open(predict_text_file, 'r') as pred:
        for line in pred:
            preds.append(detokenizer.detokenize(line.strip().split()))
    print("\nPredicted file - first sentence: ", preds[0])    

    with open(bleu_evaluate_file, 'a+') as bleu_file:
        for line in zip(refs, preds):
            if len(line[0])>1:
                test = line[0]
                pred = line[1]
                #print(test, '\t----->\t', pred)
                bleu = sacrebleu.sentence_bleu(pred, [test], smooth_method='exp')
                score+=bleu.score
                count+=1
                #print(bleu.score, "\n")
        avg=score/count
        print("\nAverage Bleu Score : ",avg)
        content = f"File {index} : {avg}"
        bleu_file.write(content+'\n')

    return 

for i in range(22,32) :
    get_sentence_bleu_score_from_file(f"./Translate/{i} - translate.txt" ,f"./Data/EnglishCleanfiles/{i} - eng.txt",f"./BLEU_Result.txt",i)

