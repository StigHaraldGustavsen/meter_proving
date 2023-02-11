# Meter proving
Simple package for caluclating random uncertanity of a set of repeted measurments.

```Bash
pip install meter-proving
```


```python
from meter_proving.meter_proving import calculate_uncertanity

res = calculate_uncertanity([1000.00, 1000.00, 1000.00, 1000.25, 999.75])
print(res)
```

By default standard error is gotten from range of values, if this where to come from standard deviation set repetability param to false with a confidence intervall of 95% (coverage factor of almost 2), but theses can be parameterized.

```python
from meter_proving.meter_proving import calculate_uncertanity

res = calculate_uncertanity(
    [1000.00, 1000.00, 1000.00, 1000.25, 999.75],
    repetability = False
    )

print(res)
```

Standard error from standard deviation and has coverage factor of 1, witch gives a confidence interval of 68%

```python
from meter_proving.meter_proving import calculate_uncertanity

res = calculate_uncertanity(
    [1000.00, 1000.00, 1000.00, 1000.25, 999.75],
    coverage_factor = 1.0,
    repetability = False
    )

print(res)
```
