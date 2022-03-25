import setuptools

setuptools.setup(
    name="ship_game",
    version="0.0.1",
    author="Ben Southcott",
    author_email="benjamin.southcott@gmail.com",
    description="Interface for playing battleship",
    url="https://github.com/blsouthcott/battleship-game",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[]
)