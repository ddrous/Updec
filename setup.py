from setuptools import setup

setup(
   name='Updec',
   version='0.1.0',
   author='desmond-rn',
   author_email='desmond.ngueguin@gmail.com',
   packages=['updec', 'updec.test'],
#    scripts=['bin/script1','bin/script2'],
   url='http://pypi.python.org/pypi/Updec/',
   license='LICENSE.md',
   description='A package for meshless and data-driven PDE modelling and control',
   long_description=open('README.md').read(),
   install_requires=[
       "jax >= 0.4.1",
       "pytest",
   ],
)