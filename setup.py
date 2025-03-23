from setuptools import setup

setup(
    name="githelper",
    version="0.1.0",
    description="A retro-styled command-line tool for Git repository management",
    author="paolowu5",
    author_email="info@paoloallegretti.com",
    url="https://github.com/paolowu5/githelper",
    py_modules=["githelper"],
    install_requires=["colorama>=0.4.6"],
    entry_points={
        "console_scripts": [
            "githelper = githelper:main_menu"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)