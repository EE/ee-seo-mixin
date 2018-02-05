# ee-seo-mixin

Django app which provides abstract SEO mixin and a corresponding template to override.

## installation

1. Install the app through pip:

  ```
  pip install git+git://github.com:EE/ee-seo-mixin
  ```

2. Add `ee_seo_mixin` to your installed apps

  ```python
  INSTALLED_APPS = [
      ...
      'ee_seo_mixin',
      ...
  ]
  ```

## usage

1. In your `models.py`:

  ```python
  # models.py
  from ee_seo_mixin.models import SearchEngineOptimizableEntity

  class StaticPage(SearchEngineOptimizableEntity):
      ...
  ```

2. In your templates you now may use 3 additional templatetags:

  ```
  # static_page.html
  {% extends 'base.html' %}

  {% override_title my_page default="Welcome!"%}

  {% override_description my_page default='My default description if my_page does not have any' %}

  {% block_indexing my_page default=True %}

  ```

    Each tag takes two arguments. The first one should be an instance of _SearchEngineOptimizableEntity_ and the second one is a default (fallback) value.

3. In your views put the model object that extends `SearchEngineOptimizableEntity` to the context:

  ```python
  # views.py
  from .models import StaticPage

  def static_page_view(request):
      try:
          page = StaticPage.objects.get(pk=1)
      except StaticPage.DoesNotExist:
          raise Http404("Page does not exist")
      return render(request, 'static_page.html', {'my_page': page})
  ```
