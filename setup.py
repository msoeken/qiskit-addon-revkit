import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
import atexit

long_description = """RevKit oracles for Qiskit Aqua"""

requirements = [
  "qiskit-aqua>=0.4.2",
  "numpy>=1.13",
  "revkit>=3.1",
]

setuptools.setup(
  name='qiskit-addon-revkit',
  version="0.1.0",  # this should match __init__.__version__
  description='Aqua Component',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/msoeken/qiskit-addon-revkit',
  author='Mathias Soeken',
  author_email='mathias.soeken@epfl.ch',
  license='MIT',
  classifiers=(
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: Scientific/Engineering"
  ),
  keywords='qiskit revkit quantum aqua',
  packages=setuptools.find_packages(exclude=['test*']),
  install_requires=requirements,
  include_package_data=True,
  python_requires=">=3.5",
  entry_points={
    'qiskit.aqua.pluggables': [
      'BooleanExpression = qiskit_addon_revkit.aqua:BooleanExpression'
    ]
  }
)
