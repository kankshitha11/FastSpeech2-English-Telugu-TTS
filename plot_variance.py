
import torch
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from utils.model import get_model, get_vocoder
from utils.tools import to_device, get_configs_of


def save_plot(values, title, ylabel, output_path):
    values = np.asarray(values).reshape(-1)

    plt.figure(figsize=(12, 4))
    plt.plot(np.arange(len(values)), values, marker=".", linewidth=1)
    plt.title(title)
    plt.xlabel("Phoneme Index")
    plt.ylabel(ylabel)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def plot_predictions(output, name, base_dir):
    pitch = output[2][0].detach().cpu().numpy()
    energy = output[3][0].detach().cpu().numpy()
    duration = output[5][0].detach().cpu().numpy()

    folders = {
        "duration": (duration, "Duration (frames)"),
        "pitch": (pitch, "Predicted pitch"),
        "energy": (energy, "Predicted energy"),
    }

    for category, (values, ylabel) in folders.items():
        save_plot(
            values,
            f"{name} - Predicted {category.title()}",
            ylabel,
            base_dir / category / f"{name}_{category}.png",
        )
