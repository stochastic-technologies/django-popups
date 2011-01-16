===========
Description
===========

``django-popups`` is a small Django application that helps you hide the
notifications you might want to show users.

Web apps usually employ notification systems to show first-time users some
information on how to use the web app. Users can then hide these notifications
by clicking a "don't show this again" link or the developer can choose to do it
automatically. ``django-popups`` facilitates these sorts of scenarios by
generalising these AJAX calls and providing an easy way to perform them.

Installation
------------

You can install ``django-popups`` in multiple ways:

* With pip (preferred), do ``pip install django-popups``.
* With setuptools, do ``easy_install django-popups``.
* To install from source, download it from
  https://github.com/stochastic-technologies/django-popups/ and do
  ``python setup.py install`` or put the ``popups`` folder in your PATH or
  under your Django project directory.

Usage
-----

To use ``django-popups``, you will first need to append
``'popups.context_processors.popups'`` to the TEMPLATE_CONTEXT_PROCESSORS
variable in your settings.py. Then, you will need to add
``('^popups/', include("popups.urls")),`` to your urls.py.

This will give you access to the ``show_popup``
template variable, which you can use in a template like so::

    {% if show_popup.popup_id %} 
    <p>This is a notification.</p>
    {% endif %}

Replace ``popup_id`` with a name you use to identify that popup, so
``django-popups`` knows what to hide. ``show_popup`` returns True unless we
have previously indicated that we want to hide that particular notification by
making an AJAX request to a certain URL. To do this with jQuery, for example,
you can use the following code::

    <a href="#" onclick="j.post('{% url popups-hide %}', {popup: 'popup_id'});
       $('#popup_id').fadeOut(); return false;">
       Don't show this again</a>

This will cause the notification div with id ``#popup_id`` to fade out and
never be shown again (until the user's session is cleared).

As you can see from the code above, django-popups adds a URL (by default, that
is ``popups/hide/`` that expects a POST request with the ``popup`` parameter
containing the id of the popup to hide.

NOTE: Django-popups stores the information about which notifications to hide in
the session, as the use case is that logged-in users will not see any
notifications. This means that notification will be shown again when the user
switches browsers or clears their session, but storage of the data in the
database is trivial to add.

We encourage you to fork the code and send us pull requests if you have any
improvements.

License
-------

``django-popups`` is distributed under the BSD license.
