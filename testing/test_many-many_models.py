from myapp.models import Publication, Article
p1 = Publication.objects.create(title="Title 1")
p2 = Publication.objects.create(title="Title 2")
p3 = Publication.objects.create(title="Title 3")
a1 = Article.objects.create(headline="Headline 1")
a2 = Article.objects.create(headline="Headline 2")
a3 = Article.objects.create(headline="Headline 3")
a1.publications
# <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7faab1450ca0>
a1.publications.all()
# <QuerySet []>
a1.publications.add(p1)
a1.publications.all()
# # <QuerySet [<Publication: Title 1 is a Publication>]>
a1.publications.add(p2, p3)
a1
# <Article: Headline 1 is a Article>
a1.publications.all()
# # # # <QuerySet [<Publication: Title 1 is a Publication>, <Publication: Title 2 is a Publication>, <Publication: Title 3 is a Publication>]>
p1
# <Publication: Title 1 is a Publication>
p1.article_set.all()
# # <QuerySet [<Article: Headline 1 is a Article>]>
p1.article_set.add(a2, a3)
p1.article_set.all()
# # # # <QuerySet [<Article: Headline 1 is a Article>, <Article: Headline 2 is a Article>, <Article: Headline 3 is a Article>]>

