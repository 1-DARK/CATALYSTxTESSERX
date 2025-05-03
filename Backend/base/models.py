from django.db import models

class Text(models.Model):
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_text

class Img(models.Model):
    title = models.CharField(max_length=80, blank=False, null=True)
    image_url = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title

# TODO
class Audio(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    audio = models.FileField(upload_to='audio_files/')
    
    def __str__(self):
        return self.title

# TODO
class Video(models.Model):
    context = models.TextField(max_length=500, blank=False, null=True)
    video = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.context
    
class Pdf(models.Model):
    title = models.CharField(max_length=50, blank=False, null=True)
    file = models.FileField(upload_to='pdfs/')
    
    def __str__(self):
        return self.title
    
