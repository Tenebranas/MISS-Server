import questionanswer
import pdf_to_text
import lexsummary

inputsource = "https://www.myperfectwords.com/blog/book-report/book-report-of-harry-potter-and-the-sorcerer-stone-converted.pdf"
inputquestion = "Who wrote Harry Potter?"
inputkeyword = "hello","hello"

inputsource2 = "https://transition.fcc.gov/osp/inc-report/INoC-21-Types-of-News.pdf"
inputquestion2 = "Where does NPR have reporters in?"
inputkeyword2 = "hi","hello"

inputsource3 = "https://www.bsu.edu/-/media/www/departmentalcontent/biology/pdf/rinard-orchid-greenhouse/informational-documents/classification-of-plants.pdf"
inputquestion3 = "What is a subtribe?"
inputkeyword3 = "hi","hiii"

def process(inputsource,inputquestion):
    inputsourcefinal = pdf_to_text.main(inputsource)
    question1 = {
        "question": inputquestion,
        "context": inputsourcefinal
    }
    summary = lexsummary.lexsummarize(inputsourcefinal)
    answer = questionanswer.get_answer_transformer(question1)
    return summary, answer

def processJob(job):
    return process(job.url, job.question)

# process(inputsource,inputquestion)

    # print(similarity.fetch_keywords(inputsource))
    # print(similarity.compute_cosine_similarity(inputkeyword))

# main(inputsource,inputkeyword,inputquestion)
# main(inputsource2,inputkeyword2, inputquestion2)
# main(inputsource3,inputkeyword3,inputquestion3)