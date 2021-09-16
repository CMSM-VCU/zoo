# zoo

Peridynamics data visualization tool

[<img src="https://img.shields.io/conda/v/hallrc/zoo">](https://anaconda.org/hallrc/zoo)

## Installation

Conda:

``` plaintext
conda install -c hallrc zoo
```

Zoo is not currently available through PIP.

## Usage

Open Zoo from the command line with

``` plaintext
zoo
```

At which point, a file can be opened through the usual *File > Open* menu or with `ctrl+O`. A file can be opened immediately by including it as an argument when opening Zoo.

``` plaintext
zoo path/to/file.h5
```

Zoo expects an hdf5 file that has been written using the Pandas "table" format under the field "data". i.e. A file created with

``` python
dataframe.to_hdf(target_file, "data", "w", format="table")
```

The first set of indeces must be the timestep, and six columns are expected: `x1`, `x2`, `x3`, and `u1`, `u2`, `u3`.

**Note:** Currently, Zoo will behave incorrectly or crash if more than one file is loaded in a session. To view a different file, close and reopen Zoo or start a new instance.
