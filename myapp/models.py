from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(verbose_name="Tên Địa Điểm", max_length=50)
    address = models.CharField(verbose_name="Địa Chỉ", max_length=100)
    country = models.CharField(verbose_name="Quốc Gia", max_length=100, default="Việt Nam")

    def __str__(self):
        return f"{self.name} the place"
    
    class Meta:
        db_table = "Place"

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True
    )
    serves_hot_dogs = models.BooleanField(verbose_name="Phục vụ Hotdogs", default=False)
    serves_pizza = models.BooleanField(verbose_name="Phục vụ Pizza", default=False)
    serves_pho = models.BooleanField(verbose_name="Phục vụ Phở", default=True)

    def __str__(self):
        return f"{self.place.name} the restaurant"

    class Meta:
        db_table = "Restaurant"

class Waiter(models.Model):
    # 
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} is a waiter at {self.restaurant}"

    class Meta:
        db_table = "Waiter"

class Publication(models.Model):
    title = models.CharField(max_length=100)
    # articles = models.ManyToManyField("Article")
    class Meta:
        db_table = "Publication"

    def __str__(self):
        return f"{self.title} is a Publication"

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)

#     class Meta:
#         db_table = "Article"

#     def __str__(self):
#         return f"{self.headline} is a Article"

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    url = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    published_date = models.DateTimeField()

    class Meta:
        db_table = "Article"

class Source(models.Model):
    article = models.OneToOneField(
        Article,
        primary_key=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    class Meta:
        db_table = "Source"
