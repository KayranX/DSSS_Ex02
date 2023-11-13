from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0',
    author='Johannes Enk',
    author_email='enk.johannes98@gmail.com',
    description='Math quiz to test basic capabilities!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KayranX/DSSS_Ex02',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8'
)
