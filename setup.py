from setuptools import setup, find_packages

setup(
    name="MLE-TRAINING",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "bottleneck==1.3.7",
        "joblib==1.4.2",
        "numexpr==2.8.7",
        "numpy==1.26.4",
        "pandas==2.2.2",
        "python-dateutil==2.9.0",
        "pytz==2024.1",
        "scikit-learn==1.5.1",
        "scipy==1.13.1",
        "six==1.16.0",
        "threadpoolctl==3.5.0",
    ],
    entry_points={
        "console_scripts": [
            # Create command-line tools here if needed
            'mycli=src.mymodule:main_function',
        ],
    },
)

