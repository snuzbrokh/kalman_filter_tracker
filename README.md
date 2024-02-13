# Kalman Filter 2D Object Tracking

This repository contains code for implementing a Kalman Filter for tracking an object traveling in 2D space.

## Description

The Kalman Filter is a recursive algorithm that estimates the state of a dynamic system with noisy measurements. In the context of this repository, the Kalman Filter is used to track the position and velocity of an object moving in a 2D plane.

The main components of this repository are as follows:

- `tracker.py`: This script contains the simulation code for generating measurements of the object's position and running the Kalman Filter to estimate its state.
- `kf_tracker.py`: This module implements the Kalman Filter model with methods for initializing the filter, predicting the next state, and updating the state based on measurements.
- `utils.py`: This module provides utility functions for generating noisy measurements and plotting the results.
- `requirements.txt`: This file lists the required dependencies for running the code.

## Usage

To run the object tracking simulation using the Kalman Filter, follow these steps:

1. Install the required dependencies listed in `requirements.txt` by running the following command:
```
pip install -r requirements.txt
```

2. Import the necessary modules and classes:
```python
import numpy as np
from tracker import run_sim
from kf_tracker import KalmanFilterModel
```

3. Set the simulation options and Kalman Filter options:
```python
sim_options = {
    'time_step': 0.01,
    'end_time': 120,
    'measurement_rate': 1.5,
    'measurement_noise_std': 10,
    'motion_type': 'circle',
    'start_at_origin': False,
    'start_at_random_speed': True,
    'start_at_random_heading': True,
    'draw_plots': True,
    'draw_animation': True
}

kf_options = {
    'accel_std': 0.5,  # Q Matrix Param
    'meas_std': 10,  # R Matrix  
    'init_on_measurement': True
}
```

4. Run the simulation using the `run_sim` function:
```python
run_sim(KalmanFilterModel, sim_options, kf_options)
```

## Results

The simulation will generate plots and animations to visualize the object's true path, measured positions, and the estimated trajectory based on the Kalman Filter. These visualizations help in understanding the effectiveness of the Kalman Filter for object tracking in 2D space.

## Contributing

If you would like to contribute to this project, you can do so by following these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request describing the changes you have made.
