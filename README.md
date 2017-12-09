# Newpro

A script to create a boilerplate for text projects.

## Introduction

This script will create a directory containing files for writing projects in
my workflow. I don't know if anyone else will benefit from this, but there's no
harm in sharing. My workflow involves writing in markdown, and generating a pdf
and word document using [pandoc][]. The making process is controlled by a
makefile.

[pandoc]: https://pandoc.org/

## Installation

Install from PyPi:

```bash
sudo pip3 install newpro
```

Alternatively install from the working github repository:

```bash
git clone https://github.com/awesmubarak/newpro
cd newpro
sudo python setup.py install
```

Full disclosure, I've only tested this on Linux. It _should_ also work on macOS
and windows, but don't take my word for it.

## Usage

The script is interactive, so there's no fancy magic required. This section
will walk through every section anyway.

**Running the script**

Change into the directory you want the project in and run `newpro`.

**Author name**

Normally, you'll be presented with a prompt for the author's name (typically
your own). This step is tedious and can be skipped by creating a text file
located at `~/.config/newpro.txt`. Enter only your name into this file. This
will skip the author prompt.

**Project title**

This is the proper title of your project. No explaining to do here.

**Project name**

This is the _name_ of your project. This should be a short identifier as it
will be used as the directory path and the base for all file names. For example
entering `example` will create `example.md` as your main markdown file.

**Bibliography**

If you choose to include a bibliography file will be created. This includes an
example bibtex entry. For more information see this [biblatex tutorial][].

[biblatex tutorial]: https://www.latex-tutorial.com/tutorials/bibtex/

**License**

I like using the [CC-BY-SA][] license in my work. This will temporary license
text at the bottom. This text won't have any metadata and a todo comment will
also be created.

[CC-BY-SA]: https://creativecommons.org/licenses/by-sa/4.0/

## Example

A typical run might look as follows:

    % newpro
    Project title: Project title
    Project name: name
    Create a bibliography (y/N)? y
    Include CC-BY-SA license (y/N)? y

Creating the following structure:

    %tree
    .
    └── name
        ├── Makefile
        ├── name.bib
        └── name.md

    1 directory, 3 files

**Makefile**

```Makefile
name: name.md
    pandoc name.md --from markdown --output name.pdf --bibliography name.bib
    pandoc name.md --from markdown --to docx --output name.docx --bibliography name.bib
```

**name.bib**

```bibtex
/* @misc{ CHANGEME, */
/*        author = "CHANGEME", */
/*        title = "CHANGEME", */
/*        year = "CHANGEME", */
/*        publisher = "CHANGEME", */
/* } */
```

**name.md**

```markdown
---
title: Project title
date: 2017-12-09
author: Awes Mubarak

---

-------------------------------------------------------------------------------
This work is licensed under a [Creative CommonsAttribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
<!-- TODO: see https://creativecommons.org/choose/ -->
```

All focus can then be directed to the markdown file (and bibliography if used).
