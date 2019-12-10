import setuptools

setuptools.setup(
    name="elonet-dl",
    version="0.0.1",
    author="L. Kärkkäinen",
    author_email="tronic@noreply.users.github.com",
    description="Download videos from elonet.finna.fi archive.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Tronic/elonet-dl",
    packages=setuptools.find_packages(),
    license="Public Domain",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        "beautifulsoup4",
        "requests",
    ],
    include_package_data = True,
)
