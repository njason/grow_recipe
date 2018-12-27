# Grow Recipe Python Wrapper

A module to provide functionality to the [Grow Recipe Schema](https://github.com/njason/grow-recipe-schema)


## Usage
```
from datetime import datetime

import grow_recipe

# keep track of the start of the grow
start_time = datetime(2018, 12, 17)

with open('some_file.xml') as xml_file:
    temperature_range = grow_recipe.get_metric(
        xml_file, 'air', 'temperature', start_time, datetime.now())

print('Temperature minimum ' + temperature_range.min)
print('Temperature maximum ' + temperature_range.max)
```


## Development

This repo references a submodule, to properly clone this repo with the required submodule, run this command:
`$ git clone --recurse-submodules https://github.com/njason/grow-recipe-python`


This command updates the latest schema from the schema submodule:
`$ git submodule foreach git pull origin master`


### Testing
To run tests, run `$ pytest`
