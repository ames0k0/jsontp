#### Script structure
```
# tree -I '__pycache__|env|build|jsontp.egg-info'
.
├── jsontp
│   ├── __init__.py
│   ├── __main__.py
│   ├── config.py
│   ├── utils.py
│   └── run.py
├── tests
│   ├── __init__.py
│   └── test_page_data_tree.py
├── data
│   ├── ranker_writer-ignore_me.json
│   └── ranker_writer_user_content-ignore_me.json
├── setup.py
├── LICENSE
├── README.md
├── UPDATES.txt
└── CONTRIBUTORS.md
```

#### Dependencies
```bash
pip -V		# 22.1.1
python -V	# 3.10.5
pytest -V	# 6.2.5
```

#### MyEditorSettings
```
" set nomodeline

tabs
	vim: ts=8 sw=8
spaces
	vim: ts=2 sw=2 expandtab
```
Coding process: https://youtu.be/DkBAIKMN7x0

#### MyTODO
- [x] use 2 spaces instead of 4
	- [x] use tabs for UPPERCASE files (.md, ...)
- [x] remove or move to another file the entrypoint block
- [x] make it an API (package)
- [x] add tests
- [ ] add documentations
- [x] update version at `jsontp/__init__.py`
- [x] rename project (package)

#### WhatTODO
- [x] nested json
- [x] json in the list
- [x] check for multiple keys
	- [x] return multiple keys (iterable result)
	- [ ] unique multiple keys (not every single item in the list)
- [ ] check for keys by value
- [x] access to the data in the list
	- [x] add and get the index from `tree`
- [ ] handle errors on searching for a non string key
- [x] fix errors on reading and writing to the json file without filename
	- [x] no need to test for writing
	- [x] raising an error `FileNotFoundError` for not valid input filepath

##### API
- [ ] Flags

##### CLI
- [x] Input
	- [x] json file
- [ ] Key
	- [x] search: `str`
	- [x] filter `tree` by must have `key` (-fk)
		- [ ] multiple (-fk)
	- [x] filter `tree` by must have `value` (-fv)
		- [ ] multiple (-fv)
	- [x] result (config.py[Key]): `print`, `return`
- [x] Limit
	- [x] `print`
	- [x] `return`
- [ ] Output
	- [x] dump a `value` to the file (`-o <output_filepath>`)
	- [ ] append to the dump file
	- [x] `print`: '\*'
