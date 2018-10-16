from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='reviewio',
    version='0.1.5',
    author='borzeckid',
    author_email='borzecki.daniel@gmail.com',
    description= 'Display statistics of pull request reviewers for your project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/borzecki/reviewio',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Colorama',
        'PyGithub'
    ],
    entry_points='''
        [console_scripts]
        reviewio=reviewio.cli:cli
    ''',
)
