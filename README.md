# Dataset Description

This directory contains the data used for the evaluation of the PrivTrajGen repository.
This repository is ment to be used in combination with the [PrivTrajGen](https://github.com/erik-buchholz/CostOfTrajectoryPrivacy)
and might not work as expected without it.
The data is described below.

[1] [PrivTrajGen Repository](https://github.com/erik-buchholz/CostOfTrajectoryPrivacy)

## Table Of Contents

<!-- TOC -->
* [Dataset Description](#dataset-description)
  * [Table Of Contents](#table-of-contents)
  * [Citation](#citation)
  * [Preprocessed Datasets](#preprocessed-datasets)
  * [Raw Datasets](#raw-datasets)
    * [Foursquare New York City (FS NYC)](#foursquare-new-york-city-fs-nyc)
    * [GeoLife](#geolife)
      * [Download of Raw Dataset](#download-of-raw-dataset)
      * [Pre-Processing](#pre-processing)
    * [Porto](#porto)
  * [Contact](#contact)
  * [Acknowledgements](#acknowledgements)
  * [References](#references)
  * [License](#license)
<!-- TOC -->

## Citation

TBD

## Preprocessed Datasets

The pre-processed datasets used for the evaluation are stored in the following directory:
```
data/processed/
```
However, the GeoLife and Porto Dataset were too large to be included in this repository.
Therefore, these datasets were split up into smaller parts.
The script `data/processed/reconstruct_datasets.py` can be used to reassemble the datasets:
```shell
python data/processed/reconstruct_datasets.py
```

After this, all code should work as expected.

## Raw Datasets

In the following, we desribe how the preprocessed datasets can be obtained from the raw datasets.

### Foursquare New York City (FS NYC)

The files `test_latlon.csv` and `train_latlon.csv` are taken from the LSTM-TrajGAN repository
available at [GitHub](https://github.com/GeoDS/LSTM-TrajGAN).
The file `all_latlon.csv` is the concatenation of the two files above and contains all trajectories.
All three files are already contained in this repository.

| File               | Number of Trajectories | Number of Points | Source                                                                                  |
|--------------------|------------------------|------------------|-----------------------------------------------------------------------------------------|
| `test_latlon.csv`  | 1,027                  | 22,153           | [LSTM-TrajGAN](https://github.com/GeoDS/LSTM-TrajGAN/blob/master/data/test_latlon.csv)  |
| `train_latlon.csv` | 2,052                  | 44,809           | [LSTM-TrajGAN](https://github.com/GeoDS/LSTM-TrajGAN/blob/master/data/train_latlon.csv) |
| `all_latlon.csv`   | 3,079                  | 66,962           | /                                                                                       |

The conversion of the raw data into the npy format used in the evaluation is described in the notebook
`notebooks/fs_nyc.ipynb` which is part of the PrivTrajGen repository [1].


### GeoLife

**If you simply want to reproduce the paper's results, you can use the pre-processed version of the dataset we included in `data/processed/`.
In this case, you don't have to download the raw dataset and can skip the pre-processing step.**

#### Download of Raw Dataset

The GeoLife dataset is available
at [Microsoft Research](https://www.microsoft.com/en-us/download/details.aspx?id=52367).
Due to its size, we do not include into this repository.
Please download it manually from the provided link and extract it into the directory `data/geolife`.

```shell
cd data
wget https://download.microsoft.com/download/F/4/8/F4894AA5-FDBC-481E-9285-D5F8C4C4F039/Geolife%20Trajectories%201.3.zip
unzip Geolife\ Trajectories\ 1.3.zip
mv Geolife\ Trajectories\ 1.3 geolife
```

The resulting directory structure should be as follows:

```
data/
├──geolife/
│  ├──Data/
│  │  ├──000/
│  │  │  ├──Trajectory/
│  │  │  │  ├──20081023025304.plt
│  │  │  │  ├──...
│  │  ├──...
│  ├──User Guide-1.3.pdf
```

#### Pre-Processing

The GeoLife dataset requires some pre-processing before it can be used.
For pre-processing, you can use the script `stg.datasets.geolife.py` which is provided as part of the 
[SoK-TrajGen](https://github.com/erik-buchholz/SoK-TrajGen) repository.
Refer to this [Readme](https://github.com/erik-buchholz/SoK-TrajGen/tree/main/data) for instructions.


### Porto

**The preprocessed version of the dataset is included in `data/processed/`, such that the preprocessing is optional.**

The raw Porto dataset is available at [Kaggle](https://www.kaggle.com/c/pkdd-15-predict-taxi-service-trajectory-i/data).
The preprocessing of the dataset is detailed in `notebooks/porto_taxi.ipynb` of the PrivTrajGen repository [1].

## Contact

**Author:** [Erik Buchholz](https://www.erikbuchholz.de) ([e.buchholz@unsw.edu.au](mailto:e.buchholz@unsw.edu.au))

**Supervision:**

- [Prof. Salil Kanhere](https://salilkanhere.net/)
- [Dr. Surya Nepal](https://people.csiro.au/N/S/Surya-Nepal)

**Involved Researchers:**

- [Dr. Sharif Abuadbba](https://people.csiro.au/A/S/sharif-abuadbba)
- [Dr. David D. Nguyen](https://people.csiro.au/w/s/shuo-wang)
- [Dr. Natasha Fernandes](https://researchers.mq.edu.au/en/persons/natasha-fernandes)

## Acknowledgements

The authors would like to thank the University of New South Wales,
the Commonwealth of Australia, and the Cybersecurity Cooperative Research Centre Limited, whose activities are partially
funded by the Australian Government’s Cooperative Research Centres Programme, for their support.

## References

We would like to thank the following authors for sharing their datasets and/or code that we used in our research:

1. Rao, J., Gao, S.*, Kang, Y. and Huang, Q. (2020).
"LSTM-TrajGAN: A Deep Learning Approach to Trajectory Privacy Protection."
In the Proceedings of the 11th International Conference on Geographic Information Science (GIScience 2021),
12:1--12:17, doi: https://doi.org/10.4230/LIPIcs.GIScience.2021.I.12
2. Dingqi Yang, Daqing Zhang, V. W. Zheng, and Zhiyong Yu,
"Modeling user activity preference by leveraging user spatial temporal characteristics in LBSNs,"
IEEE Trans. Syst., Man, Cybern., Syst., vol. 45, no. 1, pp. 129–142, Jan. 2015,
doi: https://doi.org/10.1109/TSMC.2014.2327053
3. Y. Zheng, L. Zhang, X. Xie, and W.-Y. Ma,
"Mining interesting locations and travel sequences from GPS trajectories," in Proceedings of the 18th international
conference on World wide web, in WWW ’09. New York, NY, USA: Association for Computing Machinery, Apr. 2009,
pp. 791–800. doi: https://doi.org/10.1145/1526709.1526816
4. L. Moreira-Matias, M. Ferreira, J. Mendes-Moreira, L. L., and J. J.,
"Porto taxi - taxi service trajectory - prediction challenge, ECML PKDD 2015."
UCI Machine Learning Repository, 2015. doi: https://doi.org/10.24432/C55W25

## License

CSIRO Open Source Software Licence Agreement (variation of the BSD / MIT License)

Copyright (c) 2025, Commonwealth Scientific and Industrial Research Organisation (CSIRO) ABN 41 687 119 230.

All rights reserved. CSIRO is willing to grant you a licence to these datasets on the following terms,
except where otherwise indicated for third party material.
Redistribution and use of this software in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.
  * Neither the name of CSIRO nor the names of its contributors may be used to endorse or promote products
  derived from this software without specific prior written permission of CSIRO.

EXCEPT AS EXPRESSLY STATED IN THIS AGREEMENT AND TO THE FULL EXTENT PERMITTED BY APPLICABLE LAW,
THE SOFTWARE IS PROVIDED "AS-IS". CSIRO MAKES NO REPRESENTATIONS, WARRANTIES OR CONDITIONS OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY REPRESENTATIONS, WARRANTIES
OR CONDITIONS REGARDING THE CONTENTS OR ACCURACY OF THE SOFTWARE, OR OF TITLE, MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, THE ABSENCE OF LATENT OR OTHER DEFECTS,
OR THE PRESENCE OR ABSENCE OF ERRORS, WHETHER OR NOT DISCOVERABLE.
TO THE FULL EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT SHALL CSIRO BE LIABLE ON ANY LEGAL THEORY(INCLUDING,
WITHOUT LIMITATION, IN AN ACTION FOR BREACH OF CONTRACT, NEGLIGENCE OR OTHERWISE) FOR ANY CLAIM, LOSS,
DAMAGES OR OTHER LIABILITY HOWSOEVER INCURRED.  WITHOUT LIMITING THE SCOPE OF THE PREVIOUS SENTENCE
THE EXCLUSION OF LIABILITY SHALL INCLUDE: LOSS OF PRODUCTION OR OPERATION TIME, LOSS,
DAMAGE OR CORRUPTION OF DATA OR RECORDS; OR LOSS OF ANTICIPATED SAVINGS, OPPORTUNITY, REVENUE, PROFIT OR GOODWILL,
OR OTHER ECONOMIC LOSS; OR ANY SPECIAL, INCIDENTAL, INDIRECT, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES,
ARISING OUT OF OR IN CONNECTION WITH THIS AGREEMENT, ACCESS OF THE SOFTWARE OR ANY OTHER DEALINGS WITH THE SOFTWARE,
EVEN IF CSIRO HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH CLAIM, LOSS, DAMAGES OR OTHER LIABILITY.
APPLICABLE LEGISLATION SUCH AS THE AUSTRALIAN CONSUMER LAW MAY APPLY REPRESENTATIONS, WARRANTIES,
OR CONDITIONS, OR IMPOSES OBLIGATIONS OR LIABILITY ON CSIRO THAT CANNOT BE EXCLUDED, RESTRICTED
OR MODIFIED TO THE FULL EXTENT SET OUT IN THE EXPRESS TERMS OF THIS CLAUSE ABOVE "CONSUMER GUARANTEES".
TO THE EXTENT THAT SUCH CONSUMER GUARANTEES CONTINUE TO APPLY, THEN TO THE FULL EXTENT PERMITTED BY THE APPLICABLE
LEGISLATION, THE LIABILITY OF CSIRO UNDER THE RELEVANT CONSUMER GUARANTEE IS LIMITED (WHERE PERMITTEDAT CSIRO'S
OPTION) TO ONE OF FOLLOWING REMEDIES OR SUBSTANTIALLY EQUIVALENT REMEDIES:
(a)               THE REPLACEMENT OF THE SOFTWARE, THE SUPPLY OF EQUIVALENT SOFTWARE,
OR SUPPLYING RELEVANT SERVICES AGAIN;
(b)               THE REPAIR OF THE SOFTWARE;
(c)               THE PAYMENT OF THE COST OF REPLACING THE SOFTWARE, OF ACQUIRING EQUIVALENT SOFTWARE,
HAVING THE RELEVANT SERVICES SUPPLIED AGAIN, OR HAVING THE SOFTWARE REPAIRED.
IN THIS CLAUSE, CSIRO INCLUDES ANY THIRD PARTY AUTHOR OR OWNER OF ANY PART OF THE SOFTWARE
OR MATERIAL DISTRIBUTED WITH IT.  CSIRO MAY ENFORCE ANY RIGHTS ON BEHALF OF THE RELEVANT THIRD PARTY.

Third Party Components

The following third party components are distributed with the Software.
You agree to comply with the licence terms for these components as part of accessing the Software.
Other third party software may also be identified in separate files distributed with the Software.
___________________________________________________________________
Foursquare NYC Dataset Preprocessed by Rao et al. (2020)

Rao, J., Gao, S.*, Kang, Y. and Huang, Q. (2020).
"LSTM-TrajGAN: A Deep Learning Approach to Trajectory Privacy Protection."
In the Proceedings of the 11th International Conference on Geographic Information Science (GIScience 2021),
12:1--12:17, doi: https://doi.org/10.4230/LIPIcs.GIScience.2021.I.12

Available at: https://github.com/GeoDS/LSTM-TrajGAN
___________________________________________________________________
Above Dataset is derived from the original Foursquare NYC dataset:

Dingqi Yang, Daqing Zhang, V. W. Zheng, and Zhiyong Yu,
"Modeling user activity preference by leveraging user spatial temporal characteristics in LBSNs,"
IEEE Trans. Syst., Man, Cybern., Syst., vol. 45, no. 1, pp. 129–142, Jan. 2015,
doi: https://doi.org/10.1109/TSMC.2014.2327053

Available at: https://sites.google.com/site/yangdingqi/home/foursquare-dataset
___________________________________________________________________
Geolife Dataset

Y. Zheng, L. Zhang, X. Xie, and W.-Y. Ma,
"Mining interesting locations and travel sequences from GPS trajectories," in Proceedings of the 18th international
conference on World wide web, in WWW ’09. New York, NY, USA: Association for Computing Machinery, Apr. 2009,
pp. 791–800. doi: https://doi.org/10.1145/1526709.1526816

This dataset is licensed under the (CC0: Public Domain) License:
https://creativecommons.org/publicdomain/zero/1.0/
___________________________________________________________________
Porto Taxi Service Trajectory Dataset

L. Moreira-Matias, M. Ferreira, J. Mendes-Moreira, L. L., and J. J.,
"Porto taxi - taxi service trajectory - prediction challenge, ECML PKDD 2015."
UCI Machine Learning Repository, 2015. doi: https://doi.org/10.24432/C55W25

Available at: https://archive.ics.uci.edu/dataset/339/taxi+service+trajectory+prediction+challenge+ecml+pkdd+2015

This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) License: https://creativecommons.org/licenses/by/4.0/legalcode
___________________________________________________________________
