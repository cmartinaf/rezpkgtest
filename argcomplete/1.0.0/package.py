name = "argcomplete"

version = "1.0.0"

authors = [
    "Andrey Kislyuk"
]

description = \
    """
    Bash tab completion for argparse
    """

build_requires = [
    "python-2.7",
]

variants = [
    ["platform-linux", "python-2.7"]
]

tools = [
]

requires = [
    "python-2.7"
]

uuid = "python_packages.argcomplete-1.0.0"

def commands():
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
    env.PATH.append("{root}/bin")

    source('{root}/argcomplete.sh')

