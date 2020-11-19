import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Geosoft2_Pack-Demo_MB", # Replace with your own username
    version="0.0.1",
    author="Maximilian Busch",
    author_email="m_busc15@wwu.de",
    description="This Package is only for demonstration in a Students Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="---",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
