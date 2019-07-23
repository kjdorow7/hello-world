import sys
from setuptools import setup

requirements = [
    'datetime>=4.2',
    'numpy>=1.15.0',
    'opencv-python>=3.4.2.17',
    'torch>=1.0.0',
    'torchvision>=0.2.1',
    'psutil>=5.4.8'
    ]

setup(
    name = "helloworldKJ",        # what you want to call the archive/egg
    version = "0.1",
    packages=["helloworld"],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=[requirements],
    extras_require={},      # optional features that other packages can require
                            #   like 'helloworld[foo]'
    package_data = {},
    author="KJ Dorow",
    author_email = "kevin.e.dorow@pnnl.gov",
    description = "The familiar example program in Python",
    license = "UNKNOWN",
    keywords= "example documentation tutorial",
    url = "https://github.com/kjdorow7/hello-world",
    entry_points = {
        "console_scripts": [        # command-line executables to expose
            "helloworld_in_python = helloworld.main:main",
        ],
        "gui_scripts": []       # GUI executables (creates pyw on Windows)
    }
)