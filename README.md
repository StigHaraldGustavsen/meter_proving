# Meter proving
Simple package for caluclating random uncertanity of a set of repeted measurments.

```Bash
pip install meter-proving
```


```python
from meter_proving.meter_proving import calculate_uncertanity
import numpy as np

x = np.array([1000.00, 1000.00, 1000.00, 1000.25, 999.75])

res = calculate_uncertanity(x)
print(res)
```

By default standard error is gotten from range of values, if this where to come from standard deviation set repetability param to false

```python
from meter_proving.meter_proving import calculate_uncertanity
import numpy as np

x = np.array([1000.00, 1000.00, 1000.00, 1000.25, 999.75])

res = calculate_uncertanity(x, repetability = False)
print(res)
```
