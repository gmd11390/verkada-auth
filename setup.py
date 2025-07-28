from setuptools import setup, find_packages

setup(
    name="verkada_auth",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    author="George Dorsey",
    author_email="gmd11390@gmail.com",
    description="Helper utilities for managing Verkada API token-based authentication.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)