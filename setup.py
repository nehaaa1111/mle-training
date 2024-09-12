from setuptools import find_packages, setup

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="housing_price_prediction_NR",  # Name of the package
    version="0.1.0",  # Version of the package
    author="Neha Rawat",  # Author name
    author_email="neha.rawat@tigeranalytics.com",  # Author's email
    description="A package for predicting \
    housing prices using machine learning models",  # Short description
    long_description=long_description,  # Long description from README
    long_description_content_type="text/markdown",
    # Format of long description
    url="https://github.com/nehaaa1111/mle-training",
    # URL to the repository (or website)
    packages=find_packages(where="src"),
    # Automatically find packages in the src directory
    package_dir={"": "src"},  # Specify the directory where the code is located
    classifiers=[  # Metadata classifiers
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version required
    install_requires=[  # External dependencies
        "matplotlib>=3.0",
        "numpy>=1.19",
        "pandas>=1.0",
        "scikit-learn>=0.24",
        "scipy>=1.5",
        "six>=1.15",
    ],
    # entry_points={  # For command-line tools if needed
    #     "console_scripts": [
    #         "housing_price_predictor=src.ingest_data:main",
    # # Define a script entry point
    #     ],
    # },
)
