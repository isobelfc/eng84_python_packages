# Python Packages
## What is a package
### Why should we use them
### What is pip
- `pip` is a package manager in Python to install any packages
- `pip install package_name` to use
- `pip3 install requests`

```python
from random import random  # random used to generate random numbers
import math

print(random())

num_float = 23.7

print("actual float value " + str(num_float))

print(math.ceil(num_float))  # ceil() rounds up the value
print(math.floor(num_float))  # floor() rounds down the value
```

## API
- Application Programming Interface
- Allows the user to interact with a program without editing it directly