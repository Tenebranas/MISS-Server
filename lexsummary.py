import pdf_to_text
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import textwrap
import nltk
nltk.download('punkt')

def lexsummarize(context,sentencecount=6):
    englishtokenize = PlaintextParser.from_string(context,Tokenizer('english')) #tokenizes english text
    summarized = LexRankSummarizer() #summarizes tokenized text
    summary = summarized(englishtokenize.document,sentences_count=sentencecount) #summary from the summarizing^
    output = ''
    for s in summary:
        output = output + ' ' + s._text
    return output

# state = ['']
# for document in state:
#     contextused = pdf_to_text.main(document)
#     finalsummary = lexsummarize(contextused)
#
#     finaltopic = ''
#
#     for topic in finalsummary:
#         topic = textwrap.fill(str(topic).replace('\\n', '').replace('.', '.\n'), 140)
#         finaltopic += topic
#         finaltopic += '\n \n'