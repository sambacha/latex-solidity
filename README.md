# pygments-lexer-solidity

Solidity and Yul lexer for Pygments, distributed as a PyPI package.

If you want pretty syntax highlighting in documentation for Solidity
files, and you\'re using Pygments, this might just be the thing for you.

Currently, Solidity keywords up to version 0.8.0 are included, to the
best of my ability. MRs are welcome!

The Yul intermediate language is also supported, including for
stand-alone code blocks.

## Overview

This repo builds on top of the source [which is can be located at https://gitlab.com/veox/pygments-lexer-solidity](https://gitlab.com/veox/pygments-lexer-solidity/).

To use the lexer for LaTeX highlighting simply extract the `lexer-latex.zip` file and upload both the `__init__.py` and `lexer.py` in your document directory or use a service like [overleaf.com](https://www.overleaf.com/).

A reference LaTeX document and generated PDF are included. This was rendered and generated using the overleaf web application. [see latex/example.pdf](./latex/example.pdf)

## LaTeX

![](https://d.pr/i/7G8jZs.jpeg)

### Solidity

```latex
\begin{minted}{lexer.py:SolidityLexer -x}
   ... your code here ...
\end{minted}
```

### Yul

```latex
\begin{minted}{lexer.py:YulLexer -x}
   ... your code here ...
\end{minted}
```

## Installation

Set up your virtual environment, no matter how you do it.

``` shell
 virtualenv .virtualenv/`basename $(pwd)`
 source .virtualenv/`basename $(pwd)`/bin/activate
```

Then install via PyPI:

``` shell
 pip install pygments-lexer-solidity
```

Or from a local git repo:

```shell
 pip install -r requirements.txt
 pip install -e .
```

## Usage

Depends on doc-building infrastructure.

### Sphinx

Have this in Sphinx\'s `conf.py`:

```python
from sphinx.highlighting import lexers
from pygments_lexer_solidity import SolidityLexer, YulLexer
lexers['solidity'] = SolidityLexer()
lexers['yul'] = YulLexer()
```

Then use `.. code-block:: solidity` for Solidity code blocks, or
`.. code-block:: yul` for Yul.

### Command-line

To test a local copy of the lexer on the CLI:

``` shell
 pygmentize -x -l pygments_lexer_solidity/lexer.py:SolidityLexer example.sol
```

To generate a colorized HTML file:

```shell
 pygmentize -v -O full,style=fruity -o example.sol.html example.sol
```

## License

BSD 2-clause simplified. See `LICENSE.txt`.
