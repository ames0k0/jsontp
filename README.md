CLI tool to view json tree / structure

```bash
cat input.json
# {"a": 1, "b": [{"c": 3}]}
python -m jsontp -i input.json -v
# root -> a
# root -> b
# root -> b -> [0] -> c
python -m jsontp -i input.json -k c
# root -> b -> [0] -> c
```

#### Install
```bash
pip install jsontp
# or
pip install git+https://github.com/ames0k0/jsontp
```

#### CLI Arguments
```
CLI tool to view json tree / structure

options:
  -h, --help  show this help message and exit
  -i I        [i]nput filepath
  -o O        [o]utput filepath
  -v [V]      [v]view json tree
  -k K        [k]ey to search
  -t T        [t]ree to `-o` the data from
  -l L        [l]imit stdout
  -il IL      [i]tems [l]imit stdout
  -fk FK      [f]ilter stdout by `key`
  -fv FV      [f]ilter stdout by `value`
```

#### Usage Example :: CLI
```bash
# View tree / structure with array items limit 1
python -m jsontp -i input.json -v -il 1

# Search for `key` (-k), filter by `key` (-fk)
python -m jsontp -i input.json -k id -fk user

# Search for `key` (-k), filter by `key` (-fk), print the value for `tree`
python -m jsontp -i input.json -k id -fk user -o '*'

# Print the value for `tree` (NOTE: `-o output.json` - to dump a value)
python -m jsontp -i input.json -t 'root -> props -> ... -> user' -o '*'
```

#### Usage Example :: API (Experimental)
```python3
from jsontp import JsonTreeParser
from jsontp.utils import FileIO
from jsontp.config import Key

file_io = FileIO(src="input.json")
file_data = file_io.load()

pdt = JsonTreeParser(data=file_data)
pdt_tree = pdt.tree_by_key_or_view(key="user", result_to=Key.SAVE)

data_for_tree = pdt.data_by_tree(tree=next(pdt_tree))
file_io.dump(data=data_for_tree, dst="output.json")
```

#### License :: MIT
Copyright (c) 2022,2024 ames0k0
