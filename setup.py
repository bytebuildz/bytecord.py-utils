from setuptools import find_packages, setup
from .liftcord import __ver__

packages = [
    'liftcord',
    'liftcord.info'
]

setup(
    name="liftcord.py-tools",
    version=f"{__ver__.version}",
    packages=packages,
    include_package_data=True,
    license="MIT License",
    description="liftcord.py Utils",
    keywords="liftcord.py Utils",
    url="https://github.com/bytebuildz/liftcord.py-tools/",
    author=".drmr",
    author_email="hi@icey.fr",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)