from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="db_weights",
    version="0.0.1",
    author="Aydin Abedinia",
    author_email="abedinia.aydin@gmail.com",
    description="Calculating db_weights for test data based on training data.",
    long_description="Distance based weighting alg for semi-supervised learning. more infor: https://link.springer.com/article/10.1007/s13042-024-02161-z",
    long_description_content_type="text/markdown",
    url="https://github.com/WeightedBasedAI/weights",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'scipy',
        'joblib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

