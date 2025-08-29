from setuptools import setup, find_packages

setup(
    name="nmap-parser",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["tabulate", "colorama"],
    entry_points={
        'console_scripts': [
            'nmap-parser = nmap_parser.main:main',
        ],
    },
    author="x.tig4r",
    description="Parses Nmap output to show connected device info.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    author="x.tig4r",
)

