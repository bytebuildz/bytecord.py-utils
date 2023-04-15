from setuptools import find_packages, setup

packages = [
    'bytecord',
    'bytecord.py_gui',
    'bytecord.py_logger',
    'bytecord.py_mobile'
]

setup(
    name="bytecord",
    version="1.0.0",
    packages=packages,
    include_package_data=True,
    license="MIT License",
    description="bytecord.py Utils",
    keywords="bytecord.py Utils",
    url="https://github.com/bytebuildz/bytecord.py-utils/",
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
