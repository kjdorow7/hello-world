import sys
from setuptools import setup

setup(
    name = "helloworld",        # what you want to call the archive/egg
    version = "0.1",
    packages=["helloworld"],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=[],
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