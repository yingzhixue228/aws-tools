#!/usr/bin/env python
from distutils.core import setup

setup(name='aws-tools',
      version='0.1',
      description='Basic helpers for Amazon Web Services',
      author='Serdar Tumgoren',
      author_email='zstumgoren@gmail.com',
      url='https://github.com/zstumgoren/aws-tools',
      license='MIT',
      packages=['aws'],
      scripts=['scripts/s3_upload.py'],
      install_requires=['boto'],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities'
      ]
)
