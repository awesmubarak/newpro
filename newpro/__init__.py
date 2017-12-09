#!/usr/bin/env python3

"""Newpro.py

A script to create text projects.

"""


from datetime import datetime
from os import path, makedirs


def get_config():
    """Gets project name.

    Returns:
        short_pro_name (str): name of the project sperated with dashes.
        long_pro_name (str): full name of the project.

    """
    config = {}
    # get author information
    try_path = path.join(path.expanduser("~"), ".config", "newpro.txt")
    try:
        with open(try_path, "r") as file:
            config["author"] = file.read()
    except FileNotFoundError:
        config["author"] = input("Author name: ").title()
    # project name
    config["long_pro_name"] = input("Project title: ")
    config["short_pro_name"] = input("Project name: ").replace(" ", "-")
    # project settings
    config["create_bib"] = input("Create a bibliography (y/N)? ") == "y"
    config["license"] = input("Include CC-BY-SA license (y/N)? ") == "y"
    return config


def make_directories(config):
    """Creates directory."""
    short_pro_name = config["short_pro_name"]
    if path.exists(short_pro_name):
        print("Error: path alreay exists: {0}".format(short_pro_name))
        exit(1)
    makedirs(short_pro_name)


def make_bibliography(config):
    """Creates bibliography."""
    if not config["create_bib"]:
        return
    example = (
        "/* @misc{ CHANGEME, */\n"
        "/*        author = \"CHANGEME\", */\n"
        "/*        title = \"CHANGEME\", */\n"
        "/*        year = \"CHANGEME\", */\n"
        "/*        publisher = \"CHANGEME\", */\n"
        "/* } */\n")
    short_pro_name = config["short_pro_name"]
    with open(path.join(short_pro_name, short_pro_name + ".bib"), "w") as file:
        file.write(example)


def make_makefile(config):
    """Create makefile."""
    short_pro_name = config["short_pro_name"]
    base = ("{0}: {0}.md\n"
            "\tpandoc {0}.md --from markdown --output {0}.pdf{1}\n"
            "\tpandoc {0}.md --from markdown --to docx --output {0}.docx{1}")
    if config["create_bib"]:
        bib_string = " --bibliography {0}".format(short_pro_name + ".bib")
    else:
        bib_string = ""
    makefile = base.format(short_pro_name, bib_string)
    with open(path.join(short_pro_name, "Makefile"), "w") as file:
        file.write(makefile)


def make_markdown_file(config):
    """Create markdown file."""
    base = "---\ntitle: {0}\ndate: {1}\nauthor: {2}\n---\n\n"
    date = datetime.strftime(datetime.now(), "%Y-%m-%d")
    markdown = base.format(config["long_pro_name"], date, config["author"])
    short_pro_name = config["short_pro_name"]
    file_name = short_pro_name + ".md"
    with open(path.join(short_pro_name, file_name), "w") as file:
        file.write(markdown)


def make_license(config):
    """Creates license."""
    if not config["license"]:
        return
    short_pro_name = config["short_pro_name"]
    license_link = "Creative Commons Attribution 4.0 International License."
    license_link = ("This work is licensed under a [Creative Commons"
                    "Attribution 4.0 International License]"
                    "(https://creativecommons.org/licenses/by/4.0/).\n"
                    "<!-- TODO: see https://creativecommons.org/choose/ -->")
    with open(path.join(short_pro_name, short_pro_name + ".md"), "a") as file:
        file.write("-" * 79 + "\n" + license_link)


def main():
    """Main function."""
    config = get_config()
    make_directories(config)
    make_bibliography(config)
    make_makefile(config)
    make_markdown_file(config)
    make_license(config)


if __name__ == "__main__":
    main()
