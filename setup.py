from setuptools import setup,find_packages
import os

setup(
    name='Flask-auto_modules',
    version='1.0',
    packages=find_packages(),
    url='http://example.com/flask-auto_modules/',
    license='BSD',
    author='Zakirjanov Rinat',
    author_email='rinat643@gmail.com',
    description='Auto modules install',
    platforms='any',
    entry_points={
        'console_scripts':
            ['create = src.command:create_module']
    },
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)