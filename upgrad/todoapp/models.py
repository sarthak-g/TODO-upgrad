from django.db import models

# Create your models here.

class TodoItem(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    created_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"
        ordering = ['-created_time']
