from pathlib import Path

from setuptools import setup


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="jsontp",
    version="1.2.0",
    description="JSON Tree Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nodaa Gaji",
    author_email="c0d3r.nodiru.gaji@gmail.com",
    url="https://pypi.org/project/jsontp",
    download_url="https://github.com/ames0k0/jsontp",
    packages=["jsontp"],
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
    platforms=[
        "Operating System :: OS Independent",
    ],
)
