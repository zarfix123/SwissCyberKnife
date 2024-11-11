from setuptools import setup, find_packages

setup(
    name="cyber-swiss-army",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "cryptography",
        "scapy",
    ],
    entry_points={
        "console_scripts": [
            "swissknife=swissknife.main:main",
        ]
    },
)
