import setuptools
from PublicDataReader.config.info import __version__, __author__, __contact__, __github__

with open("requirements.txt") as f:
    tests_require = f.readlines()
install_requires = [t.strip() for t in tests_require]

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
    install_requires=install_requires,
)
