from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name = "Наименование")
    content = models.TextField(blank=True,  verbose_name = "Контент")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name = "Дата публикации")
    updated_at = models.DateTimeField(auto_now=True,  verbose_name = "Обновлено")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',  verbose_name = "Фото", blank = True)
    is_published = models.BooleanField(default=True, verbose_name = "Публикация")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name = "Категории")
    view = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['create_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['title' ]
