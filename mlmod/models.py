from django.db import models
from PIL import Image
import uuid
from .utils import mlcall
import numpy as np


class ModelCall(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey('auth.User', related_name='model_calls', on_delete=models.CASCADE)
    image = models.ImageField(
        default='model_call/default.jpg', upload_to='model_call')
    result = models.CharField(max_length=20, blank=True)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.image.url
    def getemo(self):
        #open image
        pil_img = Image.open(self.image)
        cv_image = np.array(pil_img)
        result, score = mlcall(cv_image)
        self.result = str(result)
        self.score = int(score)
        self.save()
        
            

