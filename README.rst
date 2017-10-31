pygments-lexer-solidity
=======================

Solidity lexer for Pygments, distributed as a PyPI package.

If you want pretty syntax highlighting in documentation for Solidity
files, and you're using Pygments,this might just be the thing for you.

Currently, Solidity keywords up to version 0.4.18 are included, to the
best of my ability. MRs are welcome!


Installation
------------

``pip install pygments-lexer-solidity``


Usage
-----

Depends on doc-building infrastructure.

Sphinx
^^^^^^

Have this in Sphinx's ``conf.py``:

.. code-block:: python
   
   from sphinx.highlighting import lexers
   from pygments_lexer_solidity import SolidityLexer
   lexers['solidity'] = SolidityLexer()

Then use ``.. code-block:: solidity`` for Solidity code blocks.


License
-------

BSD variant. See ``LICENSE.txt``.
