import json


with open(example.json) as f: # example.json is not a real file, just an example
    data = json.load(f)

# here it is predefind clean-up action, so we don't have to worry about it f it automatically closes the file after the block of code is executed, even if an error occurs.

