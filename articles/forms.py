# forms file specific to articles app

from django import forms
from articles.models import Article

class ArticleForm(forms.ModelForm):

	class Meta:
		"""docstring for Meta"""
		model = Article
		fields = ('title', 'body', 'pub_date', 'thumbnail')