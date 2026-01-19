from django.db import models

class Trek(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='treks/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
