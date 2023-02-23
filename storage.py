import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dataclasses import dataclass
import threading
from process import processJob
import time
import traceback
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
jobs = db.collection('jobs')
results = db.collection('results')
def delete_collection(coll_ref, batch_size):
    docs = coll_ref.list_documents(page_size=batch_size)
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.get().to_dict()}')
        doc.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)
delete_collection(jobs,5)
@dataclass
class Job:
    id: str
    url: str
    question: str
@dataclass
class Result:
    id: str
    summary: str
    answer: str
    views : int
    likes : int
    originalQuestion : str
    timestamp : int(time.time())
    def to_dict(self):
        return {
            'summary': self.summary,
            'answer': self.answer,
            'views' : self.views,
            'likes' : self.likes,
            'originalQuestion' : self.originalQuestion,
            'ref' : self.id,
            'timestamp' : self.timestamp
            }
def getJob(id):
    doc = jobs.document(id).get().to_dict()
    return Job(id, doc['source'], doc['question'])
def postResult(res):
    doc = results.document(res.id)
    doc.set(res.to_dict())

def waitForJob():
    # Create an Event for notifying main thread.
    callback_done = threading.Event()

    # Create a callback on_snapshot function to capture changes
    def on_snapshot(col_snapshot, changes, read_time):
        try:
            print(u'Callback received query snapshot.')
            print(u'Current active jobs:')
            for change in changes:
                if change.type.name == 'ADDED':
                    print(f'{change.document.id}')
                    newJob = getJob(change.document.id)
                    print(newJob)
                    s, a = processJob(newJob)
                    print(s, a)
                    postResult(Result(newJob.id, s, a,0,0,newJob.question,timestamp=int(time.time())))
                    jobs.document(change.document.id).delete()
            callback_done.set()
        except Exception as e:
            print('Error processing job:',e)
            print(traceback.format_exc())

    col_query = db.collection(u'jobs')

    # Watch the collection query
    query_watch = col_query.on_snapshot(on_snapshot)