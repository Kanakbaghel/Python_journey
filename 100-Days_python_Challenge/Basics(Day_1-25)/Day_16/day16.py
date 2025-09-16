## MODULE
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

## PACKAGES
### Example Directory Structure
"""
finance/
    __init__.py
    taxes.py
    payroll.py
"""

## import the entire module
import math_utils

result = math_utils.add(3,5)

# Import specific attributes from a module
from math_utils import add, subtract 
result = add(5,2)

### 3. Import with aliasing
import math_utils as mu

result = mu.add(5, 3)

### 4. Import all names (not recommended)
from math_utils import *

## Importing from Packages
from finance import taxes
from finance.payroll import calculate_salary
