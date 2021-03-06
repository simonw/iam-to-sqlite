from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="iam-to-sqlite",
    description="Load Amazon IAM data into a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/iam-to-sqlite",
    project_urls={
        "Issues": "https://github.com/simonw/iam-to-sqlite/issues",
        "CI": "https://github.com/simonw/iam-to-sqlite/actions",
        "Changelog": "https://github.com/simonw/iam-to-sqlite/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["iam_to_sqlite"],
    entry_points="""
        [console_scripts]
        iam-to-sqlite=iam_to_sqlite.cli:cli
    """,
    install_requires=["click", "sqlite-utils"],
    extras_require={"test": ["pytest"]},
    tests_require=["iam-to-sqlite[test]"],
    python_requires=">=3.6",
)
