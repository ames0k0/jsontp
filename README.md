CLI tool to view json tree / structure

- [x] searches for keys or values
- [x] filters by keys or values
- [x] Adding limit for list items and search results
- [x] Dumping the value for a given tree / path

```json
{"a": 1, "b": 2, "d": {"c": 3}}		# 'root -> d -> c'
{"a": 1, "b": 2, "d": [{"c": 3}]}	# 'root -> d -> [0] -> c'
```

#### Start
```bash
pip install jsontp
# or
pip install git+https://github.com/ames0k0/jsontp
```

#### CLI
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

#### Usage Example (CLI)
```bash
# View tree / structure with array items limit 1
python -m jsontp -i <input_filepath> -v -il 1

# Search for `key` (-k), filter by `key` (-fk)
python -m jsontp -i <input_filepath> -k id -fk user

# Search for `key` (-k), filter by `key` (-fk), print the value for `tree`
python -m jsontp -i <input_filepath> -k id -fk user -o '*'

# Print the value for `tree` (NOTE: `-o <output_filepath>` - to dump a value)
python -m jsontp -i <input_filepath> -t 'root -> props -> ... -> user' -o '*'
```

#### Experimental Usage Example (API)
```python3
from jsontp import PageDataTree
from jsontp.utils import FileIO
from jsontp.config import Key

input_filepath = 'ranker_writer-ignore_me.json'
output_filepath = 'ranker_writer_user_content-ignore_me.json'

file_io = FileIO(input_filepath)
file_data = file_io.load()

pdt = PageDataTree(file_data)
pdt_tree = pdt.tree_by_key(key='user', result_to=Key.SAVE)

user_data = pdt.data_by_tree(next(pdt_tree))
file_io.dump(user_data, output_filepath)
```

#### License
MIT
<br />
Copyright (c) 2022,2024 ames0k0
