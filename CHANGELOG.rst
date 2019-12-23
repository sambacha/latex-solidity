python-lexer-solidity change log
================================

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
