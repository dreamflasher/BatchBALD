from setuptools import setup


setup(name='BatchBALD',
      description='BatchBALD',
      url='https://github.com/BlackHC/BatchBALD/',
      packages=['BatchBALD', 'BatchBALD/joint_entropy'],
      install_requires=[line.rstrip('\n') for line in open("requirements.txt")],
      zip_safe=True)
