# DavidBCI

## Welcome! 
DavidBCI is an open-source platform for non-invasive brain computer interface. The project of DavidBCI is led by Dr. Arya Banerjee from Amity University,Newtown, India. DavidBCI has 3 main parts:
* brainda: for importing dataset, pre-processing EEG data and implementing EEG decoding algorithms.
* brainflow: a high speed EEG online data processing framework.
* brainstim: a simple and efficient DBCI experiment paradigms design module. 

This is the first release of DavidBCI, our team will continue to maintain the repository. If you need the handbook of this repository, please contact us by sending email to davidk76011@gmail.com with the following information:
* Name of your teamleader
* Name of your university(or organization)

We will send you a copy of the handbook as soon as we receive your information.

- [DavidBCI](#davidbci)
  - [Welcome!](#welcome)
  - [What are we doing?](#what-are-we-doing)
    - [The problem](#the-problem)
    - [The solution](#the-solution)
  - [Features](#features)
  - [Installation](#installation)
  - [Who are we?](#who-are-we)
  - [What do we need?](#what-do-we-need)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
  - [Acknowledgements](#acknowledgements)

## What are we doing?

### The problem

* DBCI datasets come in different formats and standards
* It's tedious to figure out the details of the data
* Lack of python implementations of modern decoding algorithms
* It's not an easy thing to perform DBCI experiments especially for the online ones.

If someone new to the DBCI wants to do some interesting research, most of their time would be spent on preprocessing the data, reproducing the algorithm in the paper, and also find it difficult to bring the algorithms into DBCI experiments.

### The solution

The David-DBCI will:

* Allow users to load the data easily without knowing the details
* Provide flexible hook functions to control the preprocessing flow
* Provide the latest decoding algorithms
* Provide the experiment UI for different paradigms (e.g. MI, P300 and SSVEP)
* Provide the online data acquiring pipeline.
* Allow users to bring their pre-trained models to the online decoding pipeline.

The goal of the David-DBCI is to make researchers focus on improving their own DBCI algorithms and performing their experiments without wasting too much time on preliminary preparations.

## Features

* Improvements to MOABB APIs
   - add hook functions to control the preprocessing flow more easily
   - use joblib to accelerate the data loading
   - add proxy options for network connection issues
   - add more information in the meta of data
   - other small changes

* Supported Datasets
   - MI Datasets
     - AlexMI
     - BNCI2014001, BNCI2014004
     - PhysionetMI, PhysionetME
     - Cho2017
     - MunichMI
     - Schirrmeister2017
     - Weibo2014
     - Zhou2016
   - SSVEP Datasets
     - Nakanishi2015
     - Wang2016
     - BETA

* Implemented DBCI algorithms
   - Decomposition Methods
     - SPoC, CSP, MultiCSP and FBCSP
     - CCA, itCCA, MsCCA, ExtendCCA, ttCCA, MsetCCA, MsetCCA-R, TRCA, TRCA-R, SSCOR and TDCA
     - DSP
   - Manifold Learning
     - Basic Riemannian Geometry operations
     - Alignment methods
     - Riemann Procustes Analysis
   - Deep Learning
     - ShallowConvNet
     - EEGNet
     - ConvCA
     - GuneyNet
   - Transfer Learning
     - MEKT
     - LST

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/david0154/DavidBCI.git
   ```
2. Change to the project directory
   ```sh
   cd DavidBCI
   ```
3. Install all requirements
   ```sh
   pip install -r requirements.txt 
   ```
4. Install brainda package with the editable mode
   ```sh
   pip install -e .
   ```
## Who are we?

The DavidBCI project is carried out by researchers from 
- Academy of Medical Engineering and Translational Medicine, Amity University,Newtown, India
- Amity Brain Center, India


## What do we need?

**You**! In whatever way you can help.

We need expertise in programming, user experience, software sustainability, documentation and technical writing and project management.

We'd love your feedback along the way.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. **Any contributions you make are greatly appreciated**. Especially welcome to submit DBCI algorithms.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the GNU General Public License v2.0 License. See `LICENSE` for more information.

## Contact

Email: davidk76011@gmail.com

## Acknowledgements
- [MNE](https://github.com/mne-tools/mne-python)
- [MOABB](https://github.com/NeuroTechX/moabb)
- [pyRiemann](https://github.com/alexandrebarachant/pyRiemann)
- [TRCA/eTRCA](https://github.com/mnakanishi/TRCA-SSVEP)
- [EEGNet](https://github.com/vlawhern/arl-eegmodels)
- [RPA](https://github.com/plcrodrigues/RPA)
- [MEKT](https://github.com/chamwen/MEKT)
