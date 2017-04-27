pygments-lexer-solidity
=======================

Solidity lexer for Pygments, distributed as a PyPI package.

If you want pretty syntax highlighting in documentation for Solidity
files, and you're using Pygments,this might just be the thing for you.

Installation
------------

``pip install pygments-lexer-solidity``

Usage
-----

Depends on doc-building infrastructure.

Sphinx
^^^^^^

Have this in Sphinx's `conf.py`:

.. code-block::
   
   from sphinx.highlighting import lexers
   from pygments_lexer_solidity import SolidityLexer
   lexers['solidity'] = SolidityLexer()
