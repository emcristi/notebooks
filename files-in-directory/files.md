# Files on one line

Read files from current directry and display their names one on every line.

## Using `os`

- [os.path os.path.isfile](https://docs.python.org/3/library/os.path.html#os.path.isfile)
- [os os.listdir](https://docs.python.org/3/library/os.html#os.listdir)



```python
import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
print("\n".join(files))
```

    files.html
    files.ipynb


## Using `join`

`separator.join(iterable)`

Documentation [stdtypes str.join](https://docs.python.org/3/library/stdtypes.html#str.join)

## Using `pathlib`

1. `Path('.')` : Represents the current directory as a path object
2. `.iterdir()` : Iterates over all entries (files and dirs) in the directory
3. `f.is_file()`

This approach is more modern and uses OOP.


```python
from pathlib import Path

files = [f.name for f in Path('.').iterdir() if f.is_file()]
print("\n".join(files))
```

    files.html
    files.ipynb


### Resources

- [RealPython: python-pathlib](https://realpython.com/python-pathlib/)
- [pathlib pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)
- [pathlib pathlib.Path.iterdir](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir)


## Using bash

### Using `ls`

```bash
ls -p | grep -v /
```

1. `ls -p` : lists all the files and directories, directories are shown with a trailing `/`
2. `grep -v /` : inverted grep, match all lines NOT containing `/` (directories)

### When only files

`ls -1`

List all items in the current directory on one line.

### Using `find`

`find -maxdepth 1 -type f`


