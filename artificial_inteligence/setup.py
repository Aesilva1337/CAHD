from setuptools import find_packages, setup

__version__ = '0.1.0'
__description__ = 'Api CAHD'
__long_description__ = "API's expostas para o funcionamento do sistema CAHD"

__author__ = 'Arthur Elidio da silva e Leonardo Oliveira'
__author_email__ = 'arthur.elidio.ae@gmail.com'

setup(
    name='api',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/Aesilva1337/CAHD',
    keywords='API',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
)