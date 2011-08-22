from setuptools import setup, find_packages

setup(
    name='django-cronjobs',
    version='0.2.3',
    description='A simple Django app for running cron jobs.',
    long_description=open('README.rst').read(),
    author='Mozilla',
    author_email='james@mozilla.com',
    url='http://github.com/jsocol/django-cronjobs',
    license='BSD',
    packages=find_packages(),
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
