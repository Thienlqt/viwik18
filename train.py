from gensim.models import Word2Vec
from gensim.models.callbacks import CallbackAny2Vec

class EpochLogger(CallbackAny2Vec):
    """Callback to print epoch completion details."""
    def __init__(self):
        self.epoch = 0

    def on_epoch_begin(self, model):
        print(f"Starting epoch {self.epoch + 1}...")

    def on_epoch_end(self, model):
        print(f"Finished epoch {self.epoch + 1}")
        self.epoch += 1

epoch_logger = EpochLogger()

model = Word2Vec(
        corpus_file="dataset_ready/viwik18_lineSentences.txt", 
                 vector_size=300, 
                 window=5, 
                 min_count=1,  
                 sg=1, # switch to Skipgram
                 negative=3, # turn on Negative sampling
                 workers=4, 
                 callbacks=[epoch_logger])
model.save(f"models/sgns/word2vec_sgns.model")