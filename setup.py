"""Setuptools script."""
import os
from setuptools import setup, find_packages


setup(
    name="sqlancer",
    version="1.4.3",
    description="The Next-Gen Automated SQL Injection Discovery & Exploitation Engine.",
    classifiers=["Programming Language :: Python3"],
    author="Mohamed Asem",
    author_email="mohamedasem318@gmail.com",
    packages=find_packages(),
    package_data={"": []},
    include_package_data=True,
    zip_safe=False,
    test_suite="sqlancer",
    install_requires=[
        "tldextract",
        "colorama",
        "requests",
        "chardet",
        "ua_generator",
    ],
    entry_points={"console_scripts": ["sqlancer=sqlancer.scripts.sqlancer:main"]},
    keywords=[
        "mysql",
        "mssql",
        "oracle",
        "postgre",
        "sql",
        "injection",
        "boolean-based",
        "time-based",
        "error-based",
        "stacked-queries",
    ],
    python_requires=">=3.6",
)
