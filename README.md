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
* [DRDM](https://github.com/HJ-harry/score-MRI)

## Comparison
The experimental results demonstrate the superiority of our SPIS compared to various algorithms.
To benefit other researchers, we have organized the code for these comparative algorithms. It is
noted that citing the original paper  according to the codes.
* [WBM3D](https://github.com/ashkan-abbasi66/OCT-denoising-package)
* [NLM](https://github.com/zhangprofessor/fast-Non-local-Means-and-Asymptotic-Non-local-Means)
* [ANLM]
* [WKSVD](https://github.com/ashkan-abbasi66/NWSR)
* [UINT](https://github.com/mingyuliutw/unit)
* [CUT](https://github.com/taesungp/contrastive-unpaired-translation)
* [HDcycleGAN](https://github.com/IljaManakov/HDcycleGAN)
* [speckle2void](https://github.com/diegovalsesia/speckle2void)
* [ODDM](https://github.com/DeweiHu/OCT_DDPM)
* [DRDM](https://github.com/HJ-harry/score-MRI)

