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

  {% override_title my_page default=my_page.title %}

  {% override_description my_page default='My default description if my_page does not have any' %}

  {% block_indexing my_page default=False %}

  ```

    Each tag takes two arguments. The first one should be an instance of _SearchEngineOptimizableEntity_ and the second one is a default (fallback) value.
