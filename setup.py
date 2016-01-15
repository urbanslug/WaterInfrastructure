from setuptools import setup

setup(name='waterInfrastructure',
      version='0.1',
      description='Parsing JSON and extracting some water infrastructure data.',
      url='http://github.com/urbanslug/waterInfrastructure',
      author='Njagi Mwaniki',
      author_email='njagi@urbanslug.com',
      license='MIT',
      packages=['waterInfrastructure'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
