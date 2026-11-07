# Implementation of FastSpeech 2-Based Text-to-Speech Synthesis

## 1. Project Overview

This project implements two separate FastSpeech 2 text-to-speech systems:

- **English:** Svarah dataset
- **Telugu:** IndicTTS Telugu dataset

The implementation is based on the FastSpeech 2 repository by ming024:

https://github.com/ming024/FastSpeech2

The objective is to generate speech from text in both English and Telugu using separately trained FastSpeech 2 models.

## 2. Dataset Preparation

For each language, approximately five hours of audio were selected for training and one hour for validation.

Audio was resampled to 22,050 Hz. Training and validation recordings were separated without overlap.

Preprocessing includes:

- Text normalization and phoneme/grapheme conversion
- Forced alignment
- Mel-spectrogram extraction
- Pitch (F0) extraction
- Energy extraction
- Phoneme-level duration extraction

### Dataset Details

| Language | Dataset | Training Audio | Validation Audio |
|---|---|---:|---:|
| English | Svarah | 5 hours | Approximately 1 hour |
| Telugu | IndicTTS Telugu | Approximately 5 hours | Approximately 1 hour |

## 3. Model Architecture

FastSpeech 2 is a non-autoregressive text-to-speech architecture.

The model consists of:

- **Encoder:** Processes input text representations.
- **Variance Adaptor:** Predicts duration, pitch, and energy.
- **Decoder:** Generates mel-spectrograms.
- **HiFi-GAN Vocoder:** Converts generated mel-spectrograms into speech waveforms.

The same overall architecture is used to train separate English and Telugu models.

## 4. Language-Specific Implementation

### English

- Dataset: Svarah
- Text processing: English cleaners and phoneme conversion
- Sampling rate: 22,050 Hz
- Training steps: 10,000
- Model checkpoint: 10,000 steps

### Telugu

- Dataset: IndicTTS Telugu
- Text processing: Telugu Unicode normalization and grapheme handling
- Custom Telugu symbol inventory
- Telugu-specific text processing modifications
- Sampling rate: 22,050 Hz
- Training steps: 10,000
- Model checkpoint: 10,000 steps

## 5. Results

Speech samples were generated for all five test cases in each language, including the alternative sentences E2(a), E2(b), T2(a), and T2(b).

Each language includes:

- Five generated test audio samples
- Five duration prediction plots
- Five pitch (F0) prediction plots
- Five energy prediction plots
- Training and validation loss plots where available

### Final Training Results

| Metric | English | Telugu |
|---|---:|---:|
| Training steps | 10,000 | 10,000 |
| Final training loss | 3.2916 | 1.6960 |
| Final validation loss | 4.4079 | 4.3766 |

### English Loss Documentation

The original English training logs were unavailable after the training session was restored. The recorded final English training and validation loss values are documented in the technical report.

Original English training and validation loss curves are therefore not included. The English final-loss visualizations are endpoint comparisons and are not reconstructed training curves.

Telugu training and validation loss curves are included in the Results directory.

## 6. Model Checkpoints and Preprocessed Data

The trained checkpoints and preprocessed features are hosted externally because of their large file sizes.

### English

- **Trained Model Checkpoint:** [Download English Checkpoint](https://www.kaggle.com/datasets/kankshita/fastspeech2-english-final-checkpoint)
- **Preprocessed Data and Configuration:** [Download English Training Data](https://www.kaggle.com/datasets/kankshita/fastspeech2-english-training)

### Telugu

- **Checkpoint and Backup:** [Download Telugu Backup](https://www.kaggle.com/datasets/kankshita/fastspeech2-telugu-dataset-backup)

Download the required files and place them in their corresponding language directories when reproducing the project.

Access to the original datasets, compatible vocoder weights, external acoustic models, and dictionaries may also be required.

## 7. Directory Structure

```text
FastSpeech2-English-Telugu-TTS/
│
├── English/
│   ├── config/
│   └── checkpoints/
│
├── Telugu/
│   ├── config/
│   └── checkpoints/
│
├── Results/
│   ├── English/
│   │   ├── English_final_loss_components_comparison.png
│   │   ├── English_final_total_loss_comparison.png
│   │   ├── test_generated_audios/
│   │   └── variance_adaptor_plots/
│   │       ├── duration/
│   │       ├── pitch/
│   │       └── energy/
│   │
│   └── Telugu/
│       ├── training_loss.png
│       ├── validation_loss.png
│       ├── test_generated_audios/
│       └── variance_adaptor_plots/
│           ├── duration/
│           ├── pitch/
│           └── energy/
│
├── Report/
│   └── Technical_Report.pdf
│
├── audio/
├── model/
├── text/
├── transformer/
├── utils/
│
├── train.py
├── preprocess.py
├── synthesize.py
├── plot_variance.py
├── dataset.py
├── README.md
└── requirements.txt
```

The English final-loss visualizations are endpoint comparisons, not training curves. The actual training and validation loss history was unavailable.

The language-specific configurations, preprocessing scripts, training scripts, and inference implementation are included in the repository.

## 8. Reproducibility

Install the dependencies listed in `requirements.txt`.

Use the corresponding language-specific YAML configurations and preprocessed features for training and inference.

The project includes:

- Separate English and Telugu configurations
- Dataset preprocessing implementation
- FastSpeech 2 training implementation
- Speech synthesis implementation
- Variance adaptor visualization implementation

Training and inference require compatible model checkpoints and vocoder weights.

Dataset access and any required external acoustic models or dictionaries must be configured separately.

## 9. Acknowledgements

### FastSpeech 2 Implementation

https://github.com/ming024/FastSpeech2

### Svarah Dataset

https://huggingface.co/datasets/ai4bharat/Svarah

### IndicTTS Dataset

https://github.com/AI4Bharat/Indic-TTS
