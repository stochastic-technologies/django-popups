#!/usr/bin/env python

from setuptools import setup

setup(
    name = "django-popups",
    version = "0.1",
    author = "Stochastic Technologies",
    author_email = "info@stochastictechnologies.com",
    url = "https://github.com/stochastic-technologies/django-popups/",
    description = "A Django application to hide notifications for users.",
    long_description = "An application that hides users' notification banners using AJAX.",
    license = "BSD",
    packages = ["popups"],
)
