python-lexer-solidity change log
================================

[v0.7.0] - 2021-03-25
---------------------
Added
^^^^^
* Keywords from Solidity v0.7 and v0.8. (`#5`_)
* In-comment highlighting before the SPDX license identifier. (`#6`_)

Thanks to @axic!

.. _#5: https://gitlab.com/veox/pygments-lexer-solidity/-/merge_requests/5
.. _#6: https://gitlab.com/veox/pygments-lexer-solidity/-/merge_requests/6


[v0.6.0] - 2021-03-25
---------------------
Added
^^^^^
* Two new NatSpec keywords, ``@inheritdoc`` and ``@custom:..``.
* Python version requirement in ``setup.py``. (`#1`_)

.. _#1: https://gitlab.com/veox/pygments-lexer-solidity/-/issues/1


[v0.5.1] - 2020-04-20
---------------------
Changed
^^^^^^^
* Detect ``:`` as punctuation when used in Yul variable declaration
  with type hints.


[v0.5.0] - 2020-04-07
---------------------
Added
^^^^^
* ``YulLexer``, a new lexer that has some commonalities with
  ``SolidityLexer``, but is made specifically to highlight code
  (and object descriptions!) written in the Yul language.
* Also added some missing instructions in inline assembly.


[v0.4.1] - 2020-04-03
---------------------
Added
^^^^^
* Missing keywords, such as ``calldata``, as identified in
  `lexer PR for Rouge`_.
* Use of ``$`` in names.

.. _lexer PR for Rouge: https://github.com/rouge-ruby/rouge/pull/760

Changed
^^^^^^^
* Corrected M, N ranges for ``[u]fixed{M}x{N}`` types.
* Re-classified many keywords from ``Keywords.Reserved`` to just
  ``Keywords``, since they now have functionality, or were previosly
  erroneously mis-classified.


[v0.4.0] - 2019-12-23
---------------------
Changed
^^^^^^^
* Updated keywords to those of ``solc`` v0.6.0.


[v0.3.1] - 2018-05-24
---------------------
Changed
^^^^^^^
* Only match actual "nested" keywords (global variables), not all
  instances of their partials; e.g., ``msg.sender`` but not ``sender``.


[v0.3.0] - 2018-05-24
---------------------
Added
^^^^^
* NatSpec ``@special`` keywords.
* Integers in exponential notation.
* Floating-point numbers.


[v0.2.0] - 2018-04-17
---------------------
Changed
^^^^^^^
* Updated keywords to those of ``solc`` v0.4.22.


[v0.1.0] - 2018-03-08
---------------------
Changed
^^^^^^^
* Updated keywords to those of ``solc`` v0.4.21.


[v0.0.3] - 2017-10-31
---------------------
Added
^^^^^
* Minimal instructions in README.

Changed
^^^^^^^
* Updated keywords to those of ``solc`` v0.4.18.


[v0.0.2] - 2017-04-27
---------------------
Changed
^^^^^^^
* License: from MIT to BSD.

[v0.0.1] - 2017-04-27
---------------------
Added
^^^^^
* Ported ``pygments-main`` `PR #626`_ to this package.

.. _PR #626: https://bitbucket.org/birkenfeld/pygments-main/pull-requests/626/add-solidity-lexer
