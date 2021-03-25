pygments-lexer-solidity
=======================

Solidity lexer for Pygments, distributed as a PyPI package.

If you want pretty syntax highlighting in documentation for Solidity
files, and you're using Pygments, this might just be the thing for you.

Currently, Solidity keywords up to version 0.8.0 are included, to the
best of my ability. MRs are welcome!

The Yul intermediate language is also supported, including for
stand-alone code blocks.


Installation
------------

Set up your virtual environment, no matter how you do it.

.. code-block:: shell
   
   % virtualenv .virtualenv/`basename $(pwd)`
   % source .virtualenv/`basename $(pwd)`/bin/activate

Then install via PyPI:

.. code-block:: shell
   
   % pip install pygments-lexer-solidity

Or from a local git repo:

.. code-block:: shell
   
   % pip install -r requirements.txt
   % pip install -e .


Usage
-----

Depends on doc-building infrastructure.

Sphinx
^^^^^^

Have this in Sphinx's ``conf.py``:

.. code-block:: python
   
   from sphinx.highlighting import lexers
   from pygments_lexer_solidity import SolidityLexer, YulLexer
   lexers['solidity'] = SolidityLexer()
   lexers['yul'] = YulLexer()

Then use ``.. code-block:: solidity`` for Solidity code blocks, or
``.. code-block:: yul`` for Yul.

Command-line
^^^^^^^^^^^^

To test a local copy of the lexer on the CLI:

.. code-block:: shell
   
   % pygmentize -x -l pygments_lexer_solidity/lexer.py:SolidityLexer example.sol

To generate a colorised HTML file:

.. code-block:: shell
   
   % pygmentize -v -O full,style=fruity -o example.sol.html example.sol


License
-------

BSD 2-clause simplified. See ``LICENSE.txt``.
