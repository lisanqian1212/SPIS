###SPIS paper：Score Prior Guided Iterative Solver for Speckles Removal in Optical Coherent Tomography Images

## Data Availability
### 1. One public dataset
  The public Fundus dataset is released in the paper "Fast acquisition and reconstruction of optical coherence
tomography images via sparse representation," [Available link](https://people.duke.edu/~sf59/Fang_TMI_2013.htm)

### 2. Two private AS-OCT dataset
The two private AS-OCT dataset, termed as AS-Casia and CM-Casia, is confidential due to laboratory policies and 
confidentiality agreements, which can be accessed by contacting the corresponding author (J. Liu: liuj@sustech.edu.cn) 
upon reasonable request.


## Train
Ensure the data storage folder in the OCT_dataloader before model training
```
python DDPM_main.py
```
## Test
Ensure the model storage folder before test, an example of testing CM-Casia is given
```
python DDPM_test.py --model_dir model/CMmodel/ 
```


## Reference
Our implementation builds upon several existing publicly available codes
* [ODDM](https://github.com/DeweiHu/OCT_DDPM)
* [DDPM](https://github.com/zoubohao/DenoisingDiffusionProbabilityModel-ddpm-)



