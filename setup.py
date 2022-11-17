#!/usr/bin/env python
# Setup
# JD Linares
# 2022 11 16
# pip install -e .

import os
from setuptools import setup

setup(
        name="provider_data",
        versioin="0.0.1",
        description="Pull and analyze provider data",
        long_description=open(
            os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
            ).read(),
        long_description_content_type="text/markdown",
        author="JD Linares",
        packages=["provider_data"],
        install_requires=["setuptools","docopt"]
)



