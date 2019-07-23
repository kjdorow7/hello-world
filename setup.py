import sys
from setuptools import setup

requirements = [
    'numpy',
    'torchvision',
    'psutil'
    ]

setup(
    name = "helloworld",        # what you want to call the archive/egg
    version = "0.1",
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=requirements,
    extras_require={},      # optional features that other packages can require
                            #   like 'helloworld[foo]'
    package_data = {},
    author="KJ Dorow",
    author_email = "kevin.e.dorow@pnnl.gov",
    description = "The familiar example program in Python",
    license = "UNKNOWN",
    keywords= "example documentation tutorial",
    url = "https://github.com/kjdorow7/hello-world",
)