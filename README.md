# Implementation of FastSpeech 2-Based Text-to-Speech Synthesis

## 1. Project Overview

This project implements two separate FastSpeech 2 text-to-speech systems:

- English: Svarah dataset
- Telugu: IndicTTS Telugu dataset

The implementation is based on the FastSpeech 2 repository by ming024:
https://github.com/ming024/FastSpeech2

## 2. Dataset Preparation

For each language, approximately five hours of audio were selected for
training and one hour for validation.

Audio was resampled to 22,050 Hz. Training and validation recordings
were separated without overlap.

Preprocessing includes:
- Text normalization and phoneme/grapheme conversion
- Forced alignment
- Mel-spectrogram extraction
- Pitch (F0) extraction
- Energy extraction
- Phoneme-level duration extraction

## 3. Model Architecture

FastSpeech 2 is a non-autoregressive text-to-speech architecture.
It uses a variance adaptor to predict duration, pitch, and energy.
A decoder generates mel-spectrograms, which are converted into speech
using a HiFi-GAN vocoder.

## 4. Language-Specific Implementation

### English
- Dataset: Svarah
- Text processing: English cleaners and phoneme conversion
- Checkpoint: 10,000 training steps

### Telugu
- Dataset: IndicTTS Telugu
- Text processing: Telugu Unicode normalization and grapheme handling
- Custom Telugu symbol inventory and text cleaner
- Checkpoint: 10,000 training steps

## 5. Results

Each language includes:
- Five generated test audio samples
- Five duration prediction plots
- Five pitch prediction plots
- Five energy prediction plots
- Training and validation loss plots where available

The English training logs were not available in the restored session.
The recorded final English losses are documented in the technical report.
Original English loss curves are therefore not included.

## 6. Directory Structure

- English/: English configuration, preprocessing features and checkpoint
- Telugu/: Telugu configuration, preprocessing features and checkpoint
- Results/: Generated audio, variance-adaptor plots and loss plots
- train.py: Model training
- preprocess.py: Dataset preprocessing
- synthesize.py: Speech synthesis
- plot_variance.py: Variance-adaptor prediction plots

## 7. Reproducibility

Install the dependencies listed in requirements.txt.
Use the language-specific YAML configurations and the corresponding
preprocessed features to reproduce training or inference.

Training and inference require compatible model checkpoints and vocoder
weights. Dataset access and any required external acoustic models or
dictionaries must be configured separately.

## 8. Acknowledgement

FastSpeech 2 implementation:
https://github.com/ming024/FastSpeech2

Svarah:
https://huggingface.co/datasets/ai4bharat/Svarah

IndicTTS:
https://github.com/AI4Bharat/Indic-TTS
