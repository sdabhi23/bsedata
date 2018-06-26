import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bsedata",
    version="0.1.0",
    author="Shrey Dabhi",
    author_email="shrey.dabhi23@gmail.com",
    description="A package for fetching data about BSE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sdabhi23/bsedata",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)