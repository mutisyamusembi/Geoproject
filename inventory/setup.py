import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    setup_requires=['wheel'],
    name="InventoryAPI",
    version="0.0.1",
    author="Brian Mutisya",
    description="A inventory system package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "inventory"},
    packages=setuptools.find_packages(where="inventory"),
    python_requires=">=3.6",
)