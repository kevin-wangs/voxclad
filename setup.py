from setuptools import setup, find_packages
setup(name="voxclad", version="0.1.0", description="CLI gateway and API server for multi-device compute management", author="Kevin Wangs", url="https://github.com/kevin-wangs/voxclad", package_dir={"": "src"}, packages=find_packages(where="src"), python_requires=">=3.9")
