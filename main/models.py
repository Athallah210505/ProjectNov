from django.db import models
import uuid

class Kartu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_pengirim = models.CharField(max_length=100)
    pesan = models.TextField()
    wish = models.TextField()
    
