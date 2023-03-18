import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bsedata",
    version="0.5.3",
    author="Shrey Dabhi",
    author_email="shrey.dabhi23@gmail.com",
    description="A package for fetching data from BSE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sdabhi23/bsedata",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
        'lxml'
    ],
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research"
    ),
)
