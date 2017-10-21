import textract
import re
import json
import gc
gc.enable()
class wordsearch():
    def __init__(self, file):
        self.file = file
        text = textract.process(file)
        str = text.decode('utf8').encode('ascii', errors='ignore')
        str = str.decode("utf-8")
        self.tmp = re.sub(r'[^a-zA-Z0-9-/. ]', '', str)
    def searchBWB(self):
        BMI = re.findall(r'((?i)BMI*\s\d+(?:[.,]\d+)|(?i)BMI*\d+|(?i)BMI\D+\s\d+(?:[-/]\d+)+(?:[-/]\d+)|(?i)BMI\D+\d+(?:[.])\d+|(?i)BMI\D+\d+)', self.tmp, re.M)
        BMI = BMI[0].strip().split()
        BMI= BMI[-1]

        BP = re.findall(r'((?i)blood pressure*\s\d+(?:[.,/]\d+)|blood pressure*\d+|(?i)blood pressure\D+\d+(?:[/.]\d+)|(?i)blood  pressure\D+\d+(?:[/]\d+)|(?i)bloodpressure\D+\d+(?:[/]\d+)|(?i)blood pressure\D+\d+\/\d+)', self.tmp)
        BP = BP[0].strip().split()
        BP = BP[-1]

        Weight = re.findall(r'((?i)Bodyweight\D+\d+|(?i)Weight*\s\d+(?:[.,]\d+)|(?i)Weight*\s\d+|(?i)Weight\D+\d+(?:[.,]\d+)|Weight\D+\d+)', self.tmp)
        Weight = Weight[0].strip().split()
        Weight = Weight[-1]
        data_to_file = {'FileName' : self.file, 'Weight' : Weight+' lbs', "BMI": BMI ,'BP' : BP}
        file_name = re.sub(r'.pdf', '.txt', self.file)
        with open(file_name, 'w') as outfile:
            json.dump(data_to_file, outfile)

    def find_word(self, starting_word):
        try:
            word = re.findall(r'(?i)%s\D+\d+'%(starting_word),self.tmp)
            word = word[0].strip().split()
            word = word[-1]
            return word
        except:
            return 'An error occured.'
