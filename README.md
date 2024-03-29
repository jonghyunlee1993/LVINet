# LVI Net 

Ensemble Deep Learning Model to Predict Lymphovascular Invasion in Gastric Cancer

## Abstract

Lymphovascular invasion (LVI) is one of the most important prognostic factors in gastric cancer as it indicates a higher likelihood of lymph node metastasis and poorer overall outcomes for the patient. Despite its importance, the detection of LVI(+) in histopathology specimens of gastric cancer can be a challenging task for pathologists as invasion can be subtle and difficult to discern. Herein, we propose a deep learning‐based LVI(+) detection method using H&E‐stained whole‐slide images. The ConViT model showed the best performance in terms of both AUROC and AURPC among the classification models (AUROC: 0.9796; AUPRC: 0.9648). The AUROC and AUPRC of YOLOX computed based on the augmented patch-level confidence score were slightly lower (AU-ROC: -0.0094; AUPRC: -0.0225) than those of the ConViT classification model. With weighted average of the patch-level confidence scores, the ensemble model exhibited the best AUROC, AUPRC, and F1 scores of 0.9880, 0.9769, and 0.9280, respectively. The proposed model is expected to contribute to precision medicine by potentially saving examination-related time and labor and reducing disagreements among pathologists.

## Flowdiagram

![image](https://github.com/jonghyunlee1993/LVINet/assets/37280722/19657fd7-b512-4839-a832-4c0e5cc43326)

Panel A portrays the preprocessing step and annotations, while Panel B illustrates the workflow of the LVI Net. The patch image is input into both the classification and detection models. Subsequently, the prediction outcomes from these models conducted weighted averaging, resulting in the computation of the final confidence level (referred to as the ensemble confidence). This ensemble confidence is then utilized to predict the ultimate diagnosis of LVI(+) or LVI(-).

## Installation

I recommend using Conda. Type commands as follows:

```
git clone https://github.com/jonghyunlee1993/LVINet.git
cd LVINet

conda create -n LVINet python=3.8
conda activate LVINet
conda install pytorch==1.13.1 torchvision==0.14.1 pytorch-cuda=11.6 -c pytorch -c nvidia
pip install -r requirements.txt

cd YOLOX
pip install -v -e .
```

## Validation dataset

You can download publicly available datasets to test our project. Visit [zenodo](https://zenodo.org/records/10020633).

The original paper is [A robust model training strategy using hard negative mining in a weakly labeled dataset for lymphatic invasion in gastric cancer](https://pathsocjournals.onlinelibrary.wiley.com/doi/full/10.1002/cjp2.355).

- Citation information: Lee, J., Ahn, S., Kim, H. S., An, J., & Sim, J. (2023). A robust model training strategy using hard negative mining in a weakly labeled dataset for lymphatic invasion in gastric cancer. The Journal of Pathology: Clinical Research.

## Run

1. Move patch images of the external validation dataset (hard-labeled dataset) to the data folder.
2. Do inference using ConViT. (Use notebook file)
3. Do inference using YOLOX. (Use the following commands)

   ```
   cd YOLOX
   python ./tools/LVI_prediction.py image -n yolox_m_LVI -expn yolox_m_LVI --path ../data/ --save_result --conf 0.001 --ckpt weights/LVINet_yolox_m.pth --device gpu
   ```
4. Do inference using an ensemble prediction notebook.

## Performance

| Method          | Model   | AUROC                | AUPRC              | Accuracy            | F1 score            |
|-----------------|---------|----------------------|--------------------|---------------------|---------------------|
| Classification  | ConViT  | 0.9184 (0.898-0.939)| 0.8690 (0.834-0.904)| 0.8674 (0.847-0.888)| 0.7896 (0.754-0.825)|
| Detection       | YOLOX   | 0.8915 (0.864-0.919)| 0.8319 (0.788-0.876)| 0.8592 (0.836-0.882)| 0.7934 (0.758-0.829)|
| Ensemble        |         | 0.9438 (0.926-0.962)| 0.9132 (0.888-0.939)| 0.8983 (0.879-0.918)| 0.8358 (0.804-0.868)|

