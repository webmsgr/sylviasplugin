# -*- coding: utf-8 -*-
"""
    slyv
    ~~~~

    A short description of the plugin.

    :copyright: (c) 2018 by Zachary.
    :license: Not open source, see LICENSE for more details.
"""
import ast
import re
from setuptools import find_packages, setup
from setuptools.command.install import install


with open("slyv/__init__.py", "rb") as f:
    version_line = re.search(
        r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
    ).group(1)
    version = str(ast.literal_eval(version_line))


setup(
    name="flaskbb-plugin-slyv",
    version=version,
    url="https://flaskbb.org",
    author="Zachary",
    author_email="you@example.org",
    description="A short description of the plugin.",
    long_description=__doc__,
    keywords="flaskbb plugin",
    packages=find_packages("."),
    include_package_data=True,
    package_data={
        "": ["slyv/translations/*/*/*.mo",
             "slyv/translations/*/*/*.po"]
    },
    zip_safe=False,
    platforms="any",
    entry_points={
        "flaskbb_plugins": [
            "slyv = slyv"
        ]
    },
    install_requires=[
        "FlaskBB"  # pin to a version to has pluggy integration
    ],
    setup_requires=[
        "Babel",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
