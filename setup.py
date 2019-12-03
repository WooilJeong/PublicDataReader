import setuptools

setuptools.setup(
    name="PublicDataReader",
    version="0.0.1",
    license='MIT',
    author="Wooil Jeong",
    author_email="wooil@kakao.com",
    description="Open Source Public Data Reader",
    long_description=open('pip_README.md').read(),
    url="https://github.com/WooilJeong/PublicDataReader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
