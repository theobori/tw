"""setup module"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read()

setuptools.setup(
    name="tw",
    version="0.0.1",
    author="Théo Bori",
    author_email="theo1.bori@epitech.eu",
    description="Easy Teeworlds deployment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/theobori/tw",
    packages=setuptools.find_packages(),
    license="MIT",
    entry_points = '''
        [console_scripts]
        cooltool=tw:cli
    ''',
    install_requires=[requirements],
    python_requires='>=3.11',
)
