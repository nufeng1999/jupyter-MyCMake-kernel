#!/usr/bin/env python
# coding: utf-8
with open("README.md", "r") as f:
	long_description = f.read()
import setuptools
setuptools.setup(name='jupyter_MyCMake_kernel',
      vecmakelistsion='0.0.1',
      description='Minimalistic CMake kernel for Jupyter',
    long_description=long_description,
    long_description_content_type="text/markdown",
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      url='https://github.com/nufeng1999/jupyter-MyCMake-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyCMake-kernel/releases/tag/0.0.1',
    packages=setuptools.find_packages(),
	classifiecmakelists=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
      scripts=['jupyter_MyCMake_kernel/install_MyCMake_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'cMake','cmakelists'],
      include_package_data=True
      )
