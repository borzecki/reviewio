from setuptools import setup, find_packages

setup(
    name='reviewio',
    version='0.1.0',
    author='borzeckid',
    author_email='borzecki.daniel@gmail.com',
    description= 'Display statistics of pull request reviewers for your project',
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
        reviewio=reviewio:cli
    ''',
)
