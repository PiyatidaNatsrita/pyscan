#!/usr/bin/env python
from setuptools import setup

setup(
    name='pyscan',
    version="2.4.1",
    description="PyScan is a python class that performs a scan for single or multiple given knobs.",
    author='Paul Scherrer Institute',
    requires=["numpy", 'pcaspy', 'requests'],
    packages=['pyscan',
              "pyscan.dal",
              "pyscan.positioner",
              "pyscan.interface",
              "pyscan.interface.pyScan"]
)
