from setuptools import setup, find_packages
 
setup(name='My_Library',
      version='0.1',
      url='https://github.com/DAEXDO3240/My_Library',
      license='MIT',
      author='DAEXDO 3240',
      author_email='david.proietto@gmail.com',
      description='this library interacts in various fields, expanding and simplifying, helps you manage the files: math and tkinter',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
