from setuptools import setup, find_packages

# https://setuptools.pypa.io/en/latest/references/keywords.html

setup(
    name="BassAccorder",
    version="0.2.0",
    description="Une application pour accorder une guitare basse en analysant les frequences audio",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Richalbert",
    author_email="richalbert@free.fr",
    url="https://github.com/Richalbert/BassAccorder",
    packages=find_packages(),
    install_requires=[
        "pyaudio",
        "numpy",
        "matplotlib",
        "scipy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'bass-accorder=bass_accorder.main:main',
        ],
    },
)
