django-tooltips
====================

Manageable bootstrap panels


Requirements
============

- Django
- Bootstrap

Installation
============

Install:

    $ python setup.py install

Add `panels` to your installated apps:

```python
INSTALLED_APPS = (
    ...
    'panels',
    ...
```

Add the processor to your `TEMPLATE_CONTEXT_PROCESSORS`:

```python
TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    'panels.processors.panels',
)
```

Include this in your templates (eg, `base.html`):

```python
    {% include "panels/panels.html" %}
```