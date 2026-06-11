import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "requirements.txt")) as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="insurance_management",
    version="0.0.1",
    description="Comprehensive AI-powered insurance management application for ERPNext",
    author="Balaji",
    author_email="balaji@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
