import setuptools
from PublicDataReader.config.info import __version__, __author__, __contact__, __github__

with open("requirements.txt") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PublicDataReader",
    version=__version__,
    license="MIT",
    author=__author__,
    author_email=__contact__,
    description="Open Source Public Data Reader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__github__,
    packages=setuptools.find_packages(),
    package_data={"PublicDataReader": ["raw/*.json"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
)