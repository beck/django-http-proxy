#!/usr/bin/env python
from distutils.core import setup
from httpproxy import __version__

setup(
    name='django-http-proxy',
    version=__version__,
    description='A simple HTTP proxy for the Django framework.',
    url='https://github.com/beck/django-http-proxy',
    author='Yuri van der Meer',
    author_email='django-http-proxy@yvandermeer.net',
    packages=['httpproxy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
