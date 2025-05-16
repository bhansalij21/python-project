from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires=[
        # List your dependencies here
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python project",
    keywords="python, project",
    url="https://github.com/bhansalij21/python-project",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
)
