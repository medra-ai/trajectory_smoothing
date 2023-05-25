from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup


ext_modules = [
    Pybind11Extension(
        "trajectory_smoothing.trajectory_smoothing_impl",
        ["src/cpp/trajectory_smoothing.cpp", "src/cpp/Trajectory.cpp", "src/cpp/Path.cpp"],  # Sort source files for reproducibility
    ),
]


setup(
    name="trajectory_smoothing",  # <- The package name (e.g. for PyPI) goes here
    version="0.3",  # <- The current version number.
    author="Balakumar Sundaralingam",
    author_email="balakumar-s",
    description="Package produces time-optimal interpolation of a input trajectory",
    url="https://github.com/balakumar-s/trajectory_smoothing",
    python_requires=">=3.7",
    license="BSD",
    #packages=[
    #    "trajectory_smoothing"
    #],  # <- The package will install one module named 'my_ext'
    #package_dir={"": "src"},  # <- Root directory containing the Python package
    #cmake_install_dir="src/trajectory_smoothing",  # <- CMake will place the compiled extension here
    include_package_data=True,
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
)
