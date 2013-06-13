#!/usr/bin/env python

from distutils.core import setup

assets = ["assets/**/*"]

setup(name="MDLive",
      version="0.1.0",
      description="Live Markdown Editor",
      author="Brady Love",
      author_email="love.brady@gmail.com",
      url="https://github.com/bradylove/mdlive",
      packages=['mdlivemodules'],
      package_data={'mdlivemodules': assets},
      scripts=["mdlive"])
