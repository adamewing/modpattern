#!/usr/bin/env python

from setuptools import setup, find_packages

if __name__ == '__main__':

    setup(
        name='modpattern',
        version='0.1.0',
        author='Adam Ewing',
        author_email='adam.ewing@gmail.com',
        description=("find modfied base patterns from nanopore data"),
        license='MIT',
        url='https://github.com/adamewing/modpattern',
        scripts=['modpattern'],
        packages=find_packages(),
        install_requires = [
            'torch',
            'torch-summary',
            'torchvision',
            'matplotlib',
            'pysam',
            'bx-python',
            'scikit-learn',
            'scipy',
            'numpy',
            'pillow'
        ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
        ],

    )
