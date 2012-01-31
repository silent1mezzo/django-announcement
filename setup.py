from setuptools import setup, find_packages
import os
import announcements

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name = 'django-announcement',
    version = announcements.__version__,
    author = 'Adam McKerlie',
    author_email = 'adammckerlie@gmail.com',
    description = 'A re-usable Django application for site-wide announcements',
    long_description = open(os.path.join(os,path.dirname(__file__), 'README').read(),
    license = 'BSD License',
    url = 'https://github.com/silent1mezzo/django-announcement',
    install_requires=[
        'Django>=1.2.5',
    ],
    packages = find_packages()
    classifiers=CLASSIFIERS,
)
