# Sentence METEOR

# METEOR mainly works on sentence evaluation rather than corpus evaluation
# Run this file from CMD/Terminal
# Example Command: python3 sentence-meteor.py test_file_name.txt mt_file_name.txt
#https://blog.machinetranslation.io/compute-bleu-score/

import sys
import numpy as np
from nltk.translate.meteor_score import meteor_score


target_pred = "Predictions.txt"
target_test = "References.txt"


# Open the test dataset human translation file
with open(target_test) as test:
    refs = test.readlines()

#print("Reference 1st sentence:", refs[0])

# Open the translation file by the NMT model
with open(target_pred) as pred:
    preds = pred.readlines()

meteor_file = "meteor-test.txt"

# Calculate METEOR for each sentence and save the result to a file
meteor_scores = []
with open(meteor_file, "w+") as output:
    for line in zip(refs, preds):
        test = line[0]
        pred = line[1]
        #print(test, pred)

        #meteor = round(meteor_score([test], pred), 2) # list of references
        meteor = meteor_score([test], pred)
        #print(meteor)
        meteor_scores.append(meteor)
        #print(meteor, "\n")
        output.write(str(meteor) + "\n")

print("Meteor: " + str(sum(meteor_scores)/len(meteor_scores)))
print("Done! Please check the METEOR file '" + meteor_file + "' in the same folder!")