# myapp/models.py
from django.db import models

class TextFileUpload(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='txt_files/')
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

