import os.path
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pygments-lexer-solidity',
    version='0.7.0',
    description='Solidity lexer for Pygments (includes Yul intermediate language)',
    long_description=read('README.rst'),
    license="BSD",
    author='Noel Maersk',
    author_email='veox+packages+spamremove@veox.pw',
    url='https://gitlab.com/veox/pygments-lexer-solidity',
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    packages=['pygments_lexer_solidity'],
    python_requires='>=3.3, <4',
    install_requires=[
        'pygments>=2.1'
    ],
    keywords='pygments lexer syntax highlight solidity sol yul ethereum',
    entry_points="""
    [pygments.lexers]
    solidity = pygments_lexer_solidity:SolidityLexer
    yul = pygments_lexer_solidity:YulLexer
    """
)
