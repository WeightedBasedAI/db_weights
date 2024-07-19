# Weight Calculation for Semi-Supervised Learning

This package provides tools for calculating weights for test data based on training data using nearest neighbors and various distance measures. The implementation leverages scikit-learn, scipy, and joblib for efficient computation.

## Features

- Calculate weights using Nearest Neighbors
- Calculate weights using different distance measures
- Supports various distance metrics including Euclidean, Mahalanobis, Cosine, etc.
- Parallel processing for faster computation

## Installation

You can install the package using `pip`:

```bash
pip install db-weights
```

## Usage
Importing the package

```python
import numpy as np
from db_weights import WeightCalculator
```


Creating a WeightCalculator instance

```python
weight_calculator = WeightCalculator(n_neighbors=3, algorithm='auto', n_jobs=-1)
```

Calculating weights using Nearest Neighbors
```python
x_train = np.random.rand(100, 5)  # Training data
x_test = np.random.rand(20, 5)    # Test data

weights_nn = weight_calculator.calculate_weights_nn(x_train, x_test, weight=1)
print(weights_nn)
```

Calculating weights using distance measures
```python
weights_dist = weight_calculator.calculate_weights_dist(x_train, x_test, weight=1, measure_type='euclidean')
print(weights_dist)
```

Getting available distance measures
```python
measurements = weight_calculator.get_measurements()
print(measurements)
```

Make WHL
```python
pip install setuptools wheel
python setup.py sdist bdist_wheel
```


## Dependencies
- numpy
- scikit-learn
- scipy
- joblib

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.