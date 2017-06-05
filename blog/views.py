# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Article, Categorie
# Create your views here.

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id):
    """ Afficher un article complet """
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article':article})
