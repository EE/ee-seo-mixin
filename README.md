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

3. Make sure you have `APP_DIRS` set to `True` in your `TEMPLATES` setting. If you feel lost, consult the  [docs](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-TEMPLATES-APP_DIRS).

## prerequisites

**Unfortunately `ee_seo_mixin` package is not completely standalone and depends on assumption that you have a `base.html` template which contains three blocks (see [example](https://github.com/EE/generator-ee/blob/develop/generators/django/templates/src/templates/base.html)):**

- {% block title %}
- {% block meta_description %}
- {% block extrahead %}

## usage

1. In your `models.py`:
  ```python
  # models.py
  from ee_seo_mixin.models import SearchEngineOptimizableEntity

  class StaticPage(SearchEngineOptimizableEntity):
      ...
  ```
2. In your templates simply extend `base_with_seo.html` instead of `base.html`:

  ```python
  # static_page.html
  {% extends 'base_with_seo.html' %}
  ```

3. In your views put the model object that extends `SearchEngineOptimizableEntity` to the context as `seo_object`:

  ```python
  # views.py
  from .models import StaticPage

  def static_page_view(request):
      try:
          page = StaticPage.objects.get(pk=1)
      except StaticPage.DoesNotExist:
          raise Http404("Page does not exist")
      return render(request, 'static_page.html', {'seo_object': page})
  ```
