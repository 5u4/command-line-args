import setuptools

with open('readme.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='cl_args',
    version='1.0.0',
    author='Senhung Wong <0x53656e@gmail.com>',
    description='A python command line interface package.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/senhungwong/command-line-args',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
