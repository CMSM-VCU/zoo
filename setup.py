import setuptools
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zoo",
    version="0.0.7",
    author="Riley Hall",
    author_email="riley.hall.va@gmail.com",
    description="A tool for visualizing Peridynamic simulation results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CMSM-VCU/zoo",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[Path(path).stem() for path in Path(".").glob("src/*.py")],
    include_package_data=True,
    package_data={"": ["*.glsl"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["pandas", "tables", "pyvista", "pyvistaqt", "pyqt5"],
    entry_points={"console_scripts": ["zoo = zoo:run"]},
)
