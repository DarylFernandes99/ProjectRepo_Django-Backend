import h5py
import numpy as np
import requests, io
import cv2, os, glob
from PIL import Image
import tensorflow as tf
from django.db import models
from django.conf import settings
from keras.preprocessing import image
from tensorflow.keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img, save_img, array_to_img

# Create your models here.
class Colorize(models.Model):
    image = models.ImageField(upload_to='images')
    predicted = models.BooleanField(default=False)
    result = models.CharField(max_length=250, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        img = Image.open(self.image).convert('1')
        img_arr = img_to_array(img)
        resized = cv2.resize(img_arr, (256, 256), interpolation=cv2.INTER_AREA)
        ready_img = np.expand_dims(resized, axis=0)

        try:

            path = os.path.join(settings.CUSTOM_SERVER_URL, 'media/images/')

            Colorize.objects.all().delete()
            filelist = glob.glob(os.path.join(settings.BASE_DIR, 'media/images/*'))
            for f in filelist:
                os.remove(f)

            #file_model = os.path.join(settings.BASE_DIR, 'Colorize\Trained Model\colorize_image.h5')
            #model = load_model(file_model)
            file_model = '<link to model>'
            data = requests.get(file_model).content
            f1 = io.BytesIO(data)
            with h5py.File(f1, 'r') as local_file:
                model = load_model(local_file)
            
            pred = model.predict(ready_img)
            pred = array_to_img(pred[0])
            save_img(os.path.join(settings.BASE_DIR, "media\images\\" + str(self.image)[:-4] + "_pred.png"), pred)
            self.predicted = True
            self.result = path + str(self.image)[:-4] + "_pred.png"
            
        except Exception as e:
            print(e)
            self.result = e
            self.predicted = False

        return super().save(*args, **kwargs)
