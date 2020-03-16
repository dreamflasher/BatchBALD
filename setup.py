from setuptools import setup


setup(name='batchbald',
      description='BatchBALD',
      url='https://github.com/BlackHC/BatchBALD/',
      packages=['src'],
      install_requires=[line.rstrip('\n') for line in open("requirements.txt")],
      zip_safe=True)
