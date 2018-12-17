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

print('Temperature minimum ' + temperature.min)
print('Temperature maximum ' + temperature.max)
```


## Development

This repo references a submodule, to properly clone this repo with the required submodule, run this command to clone:
`$ git clone --recurse-submodules <git repo>`


This command updates the latest schema from the schema submodule:
`$ git submodule foreach git pull origin master`


To run tests, run pytest
