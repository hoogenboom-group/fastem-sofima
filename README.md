# fastem-sofima
Scable Optical Flow-based Image Alignment (SOFIMA) of FAST-EM datasets.

## Requirements
- PC or HPC operating a Linux distribution with a decent amount of RAM (>128 GB) and CPUs/GPUs. A single GPU with 12GB VRAM was used for testing this software.
- (Remote) access to target datasets on [WebKnossos.org](WebKnossos.org) or a local instance of WebKnossos.

## Installation
It is recommended to install `fastem-sofima` in a [Python virtual environment](https://docs.python.org/3/library/venv.html) or with help of a Python environment manager such as [Conda](https://docs.conda.io/en/latest/) or [Mamba](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html), to prevent changes to your system Python installation.

Instructions for venv (Python virtual environment, requires Python3 installation)
```
python3 -m venv /path/to/new/virtual/environment
```
Activate environment:
```
source /path/to/new/virtual/environment/bin/activate
```

SOFIMA is implemented in Python and can be installed from the Github repository (ensure `venv`or `conda`/`mamba` env is active):  

```
pip install git+https://github.com/google-research/sofima
```

`fastem-sofima` likewise can be directly installed from Github:  

```
pip install git+https://github.com/hoogenboom-group/fastem-sofima
```

## Usage
See `example_notebook.ipynb`

## License
Licensed under the GNU Public license, Version 3.0 (the "License"); you may not use this software except in compliance with the License. SOFIMA is licensed under Apache License, version 2.0. You can find a copy of this license at http://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Support
This code is an important part of the Hoogenboom group code base and we are actively using and maintaining it. This means that the documentation and API may be subject to changes. Issues are encouraged, but this software is released with no fixed update schedule.
