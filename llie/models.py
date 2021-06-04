import h5py
import numpy as np
import requests, io
import cv2, os, glob
from PIL import Image
import tensorflow as tf
from django.db import models
import tensorflow_addons as tfa
from django.conf import settings
from keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow_addons.layers import InstanceNormalization
from keras.preprocessing.image import img_to_array, load_img, save_img, array_to_img

# Create your models here.
class Llie(models.Model):
    image = models.ImageField(upload_to='images')
    predicted = models.BooleanField(default=False)
    result = models.CharField(max_length=250, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        try:
            path = os.path.join(settings.CUSTOM_SERVER_URL, 'media/images/')

            Llie.objects.all().delete()
            filelist = glob.glob(os.path.join(settings.BASE_DIR, 'media/images/*'))
            for f in filelist:
                os.remove(f)

            print(str(self.image))
            # Processing Image
            img = Image.open(self.image)
            img_arr = (img_to_array(img) - 127.5) / 127.5
            #resized = cv2.cvtColor(img_arr, cv2.COLOR_BGR2RGB)
            resized = cv2.resize(img_arr, (256, 256), interpolation=cv2.INTER_AREA)
            ready_img = np.expand_dims(resized, axis=0)

            # Loading Model
            #file_model = os.path.join(settings.BASE_DIR, 'llie\Trained Model\enhance_image9.h5')
            #file_model = os.path.join(settings.BASE_DIR, 'llie\Trained Model\llie_model.h5')
            #model = load_model(file_model)
            file_model = '<add model link>'
            data = requests.get(file_model).content
            f1 = io.BytesIO(data)
            with h5py.File(f1, 'r') as local_file:
                model = load_model(local_file)

            # Prdicting Image
            pred = model.predict(ready_img)
            pred = (cv2.medianBlur(pred[0], 1) + 1) / 2
            pred = array_to_img(pred)
            save_img(os.path.join(settings.BASE_DIR, "media\images\\" + str(self.image)[:-4] + "_pred.png"), pred)
            self.predicted = True
            self.result = path + str(self.image)[:-4] + "_pred.png"
            
        except Exception as e:
            print(e)
            self.result = e
            self.predicted = False

        return super().save(*args, **kwargs)
