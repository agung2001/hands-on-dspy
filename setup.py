from setuptools import setup, find_packages

setup(
    name="hands-on-dspy",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires=[
        "dspy>=1.0.0",
    ],
    python_requires=">=3.7",
)