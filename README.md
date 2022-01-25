# zoo

Peridynamics data visualization tool

[<img src="https://img.shields.io/conda/v/hallrc/zoo">](https://anaconda.org/hallrc/zoo)

## Installation

Conda:

The full set of dependencies for Zoo is quite complex. **It's recommended that you create a new environment for Zoo to avoid any conflicts.** This can be done with

``` plaintext
conda create -n zooenv -c conda-forge -c hallrc zoo
```

Note: The name of the environment can be anything, and is `zooenv` in this example.

You can install the Zoo package in the standard way with

``` plaintext
conda install -c conda-forge -c hallrc zoo
```

(`conda-forge` must be included for dependencies.)

The Zoo package can be updated with

``` plaintext
conda update -c conda-forge -c hallrc zoo
```

Zoo is not currently available through PIP.

## Usage

After activating the relevant environment (e.g. `conda activate zooenv`), open Zoo from the command line with

``` plaintext
zoo
```

At which point, a file can be opened through the usual *File > Open*, with `ctrl+O`, or by dragging a file into the window.

A file can be opened immediately by including it as an argument when opening Zoo.

``` plaintext
zoo path/to/file.h5
```

If you want to, Zoo can be opened from within Python with

``` python
import zoo
zoo.run()
```

Zoo currently accepts two types of files:

1. An hdf5 file that has been written using the Pandas "table" format under the field "data". i.e. A file created with

    ``` python
    dataframe.to_hdf(target_file, "data", "w", format="table")
    ```

    The first set of indeces must be the timestep, and six columns are expected: `x1`, `x2`, `x3`, and `u1`, `u2`, `u3`.

2. An Emu grid file that is either comma-separated (CSV) or whitespace-separated. The first row of the file is ignored, and the first four columns are expected to be the x-y-z coordinates and the material number. Any extra columns are ignored.

**Note:** The file type is inferred from the extension. The compatible file extensions are currently `.hdf5` and `.h5` for an hdf5 file, and `.grid` and `.csv` for a grid file.

___

**Warning:** Currently, not all memory is released when a tab is closed. Zoo may need to be restarted to recover memory after opening and closing many files.
