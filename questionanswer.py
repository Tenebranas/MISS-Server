import pdf_to_text

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
def get_answer_transformer(QA_input):
    model_name = "deepset/roberta-base-squad2"

    nlp = pipeline("question-answering",model=model_name, tokenizer=model_name)
    res = nlp(QA_input)
    return res['answer']
#
# QA1_input = {
#     "question": "How much has NPR’s audience grown since 1986?",
#     "context": pdf_to_text.main("https://transition.fcc.gov/osp/inc-report/INoC-21-Types-of-News.pdf")
# }
#
# QA2_input = {
#     "question": "What were the effects of cutbacks?",
#     "context": pdf_to_text.main("https://transition.fcc.gov/osp/inc-report/INoC-21-Types-of-News.pdf")
# }
#
# QA3_input = {
#     "question": "Where does NPR have reporters in?",
#     "context": pdf_to_text.main("https://transition.fcc.gov/osp/inc-report/INoC-21-Types-of-News.pdf")
# }