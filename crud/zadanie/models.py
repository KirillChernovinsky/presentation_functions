from django.db import models


class News(models.Model):
    post_name = models.CharField(max_length=20, verbose_name='Имя_поста')
    post_description = models.CharField(max_length=20, verbose_name='Описание_поста')
    post_img = models.URLField()
    popular = models.CharField(max_length=3, default="НЕТ", verbose_name='Сделать популярным? ДА или НЕТ')


    def __str__(self):
        return f'{self.post_name} {self.post_description} {self.post_img} {self.popular}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    Comment = models.CharField(max_length=50, default="None")
    like = models.CharField(max_length=3, default="0", verbose_name='добавить лайки?')

    def __str__(self):
        return f'{self.Comment} {self.like}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Person(models.Model):
    email = models.CharField(max_length=20, default="None")
    password = models.CharField(max_length=20, default="None")

    def __str__(self):
        return f'{self.email} {self.password}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

