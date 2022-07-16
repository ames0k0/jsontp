Script to get a json `key_tree` by `key` and saving the content of the `key` by `key_tree`
- yet another parser (not searched the www for scripts that may solve my task)
```json
{"a": 1, "b": 2, "d": {"c": 3}}		# 'root -> d -> c'
{"a": 1, "b": 2, "d": [{"c": 3}]}	# 'root -> d -> [0] -> c'
```

#### Dependencies
```bash
pip -V		# 22.1.1
python -V	# 3.10.5
pytest -V	# 6.2.5
```

#### Start
```bash
# no need to if `requirements.txt` is empty
python -m venv env && source env/bin/activate
pip install -r requirements.txt

# check functions if necessary
pytest .

# run script
python src/run.py
```

#### Script structure
```
.
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── utils.py
│   └── run.py
├── tests
│   ├── __init__.py
│   └── test_page_data_tree.py
├── data
│   ├── key_content-ignore_me.json
│   └── ranker_writer-ignore_me.json
├── README.md
├── CONTRIBUTORS.md
└── requirements.txt
```

#### TODO
- [x] nested json
- [x] json in the list
- [x] check for multiple keys
	- [ ] return multiple keys (iterable result)
	- [ ] unique multiple keys (not every single item in the list)
- [ ] check for keys by value
- [x] access to the data in the list
	- [x] add and get the index from `key_tree`
- [ ] handle errors on searching for a non string key
- [x] fix errors on reading and writing to the json file without filename
	- [x] no need to test for writing
	- [x] raising an error `FileNotFoundError` for not valid input filepath

Coding process: https://youtu.be/DkBAIKMN7x0
