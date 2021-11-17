from setuptools import setup, find_packages

setup(  
        name = 'package',
        version = '1.0',
        packages = find_packages(exclude=['tests*']),
        license = 'MIT',
        description = 'Used t return the n top words in a list',
        long_description = open('README.md').read(),
        url = "https://github.com/<gogzicole>/<package-name>"
    )