import os.path
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pygments-lexer-solidity',
    version='0.2.0',
    description='Solidity lexer for Pygments',
    long_description=read('README.rst'),
    license="BSD",
    author='Noel Maersk',
    author_email='veox+packages+spamremove@veox.pw',
    url='https://gitlab.com/veox/pygments-lexer-solidity',
    packages=['pygments_lexer_solidity'],
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    keywords='pygments lexer syntax highlight solidity sol ethereum',
    install_requires=[
        'pygments>=2.1'
    ],
    entry_points="""
    [pygments.lexers]
    solidity = pygments_lexer_solidity:SolidityLexer
    """
)
