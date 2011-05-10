from setuptools import setup

setup(
    name='django-cronjobs',
    version='0.2',
    description='A simple Django app for running cron jobs.',
    author='Mozilla',
    author_email='james@mozilla.com',
    url='http://github.com/jsocol/django-cronjobs',
    license='BSD',
    packages=['cronjobs'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
