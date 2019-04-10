import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leetcodesupport",
    version="0.1.3",
    author="Stephen Chiang",
    author_email="stephenchiang@yahoo.com",
    description="The Python support for LeetCode",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jianghaoyuan2007/LeetCodeSupport",
    packages=setuptools.find_namespace_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
