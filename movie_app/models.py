from django.db import models


# Create your models here.


class Director(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Режссер"
        verbose_name_plural = "Режиссеры"


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


