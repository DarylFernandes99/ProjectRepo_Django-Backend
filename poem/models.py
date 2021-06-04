import h5py
import pickle
import numpy as np
import requests, io
import cv2, os, glob
import tensorflow as tf
from django.db import models
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Create your models here.
class Poem(models.Model):
    phrase = models.CharField(max_length=250)
    length = models.IntegerField(default=False)
    result = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        try:
            file_model = '<add model link>'
            data = requests.get(file_model).content
            f1 = io.BytesIO(data)
            with h5py.File(f1, 'r') as local_file:
                model = load_model(local_file)

            #model = load_model(os.path.join(settings.BASE_DIR, 'poem\Trained Model\poem_generation(csv_txt).h5'))
            pickle_file = os.path.join(settings.BASE_DIR, 'poem\Trained Model\\tokenizer.pkl')
            tokenizer = pickle.load(open(pickle_file, 'rb'))
            
            seed_text = str(self.phrase + "\n")
            next_words = int(self.length)

            word_index = tokenizer.word_index
            words = list(word_index.keys())
            values = list(word_index.values())

            for i in range (next_words*8*4):
                token_list = tokenizer.texts_to_sequences([seed_text])[0]
                token_list = pad_sequences([token_list], maxlen=332, padding='pre')
                pred = model.predict_on_batch(token_list)
                predicted = np.random.choice(len(pred[0]), p=pred[0])
                output_word = ""
                for index in values:
                    if index == predicted:
                        output_word = words[values.index(index)]
                        break
                seed_text += " " + output_word
                if i <= (next_words*8*4 - 8):
                    if (i + 1) % 32 == 0:
                        seed_text += "\n"
                    if (i + 1) % 8 == 0:
                        seed_text += "\n"

            self.result = seed_text.replace('\n ', '\n')
            
        except Exception as e:
            print(e)
            self.result = e

        return super().save(*args, **kwargs)
