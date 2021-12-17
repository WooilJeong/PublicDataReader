import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PublicDataReader",
    version="2021.11.17",
    license="MIT",
    author="Wooil Jeong",
    author_email="wooil@kakao.com",
    description="Open Source Public Data Reader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WooilJeong/PublicDataReader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
