# Trajectory Smoothing

This repository is a wrapper around Tobias Kunz and Mike Stilman's time-optimal trajectory 
generation method from the below paper:

> Paper: Kunz, Tobias, and Mike Stilman. "Time-optimal trajectory generation for path following 
with bounded acceleration and velocity." Robotics: Science and Systems VIII (2012): 1-8.

original cpp code: https://github.com/tobiaskunz/trajectories



There are two wrappers in this repository:

1. ros_1 wrapper: https://github.com/balakumar-s/trajectory_smoothing/tree/v0.1

2. python wrapper: main branch

## Adding this package to your python project

You can add this package as a dependency to your python package by adding the following to your
setup.cfg: 

`trajectory_smoothing @ https://github.com/balakumar-s/trajectory_smoothing/raw/main/dist/trajectory_smoothing-0.2-cp38-cp38-linux_x86_64.whl`

## Installing the python wrapper

1. `pip install trajectory_smoothing@git+https://github.com/balakumar-s/trajectory_smoothing.git`
2. Look at `examples/smooth_example.py` for an example which will draw a plot as below:

![Plot](plot.png)

