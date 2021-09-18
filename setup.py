"""Package setup module."""

from setuptools import find_packages, setup

setup(
    name="now8_api",
    version="0.0.0",
    description="Estimated time of arrival for public transport vehicles.",
    author="m0wer",
    author_email="m0wer@autisitci.org",
    license="GPLv3",
    long_description=open("README.md").read(),
    packages=find_packages(exclude=("tests",)),
    entry_points={"console_scripts": []},
    install_requires=[
        "aiohttp",
        "fastapi",
        "gunicorn",
        "overrides",
        "pydantic",
        "tenacity",
        "uvicorn",
    ],
)
