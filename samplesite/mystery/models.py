from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    context = models.TextField(null=True, blank=True, verbose_name='Текст')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['published']

class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']
