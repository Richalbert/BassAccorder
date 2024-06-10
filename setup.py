from setuptools import setup, find_packages

setup(
    name="BassAccorder",
    version="0.1.0",
    description="Application pour accorder une guitare basse",
    author="Richalbert",
    packages=find_packages(),
    install_requires=[
        "pyaudio",
        "numpy",
        "matplotlib",
        "scipy"
    ],
    entry_points={
        'console_scripts': [
            'bass-accorder=bass_accorder.main:main',
        ],
    },
)
