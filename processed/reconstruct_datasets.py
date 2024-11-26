#!/usr/bin/env python3
"""Reconstruct the large datasets from chunks."""
import argparse
import logging
import os
import sys
from pathlib import Path

import numpy as np


# Resolve the base directory
base_dir = Path(__file__).resolve().parents[2]
# Print the base directory being used
print(f"Using base directory: {base_dir}")
# Append the base directory to the system path
sys.path.append(str(base_dir))

from privtrajgen.config import Datasets, BASE_DIR
from privtrajgen.datasets.difftraj_dataset import difftraj_paths
from privtrajgen.utils import logger, printc

CHUNK_PATH = os.path.join(BASE_DIR, "data", "processed", "chunks") # / {dataset} / {chunk_idx}.npy
CHUNK_SIZE = 50 * 1024 * 1024  # 50 MB

log = logger.configure_root_loger(logging.INFO)

def human_readable_size(size: int) -> str:
    """Convert a size in bytes to a human-readable format."""
    if size < 1024 ** 2:
        return f"{size / 1024:.2f} KB"
    elif size < 1024 ** 3:
        return f"{size / 1024 ** 2:.2f} MB"
    else:
        return f"{size / 1024 ** 3:.2f} GB"

def split_into_chunks(dataset: Datasets, chunk_size: int) -> None:
    """Split a dataset into chunks of a given size and save them to disk."""
    path = difftraj_paths[dataset]

    data = np.load(path)

    num_chunks = int(np.ceil(data.nbytes / chunk_size))
    log.info(f"Splitting {dataset} into {num_chunks} chunks of size {human_readable_size(chunk_size)}")

    ds_chunk_path = os.path.join(CHUNK_PATH, str(dataset))
    os.makedirs(ds_chunk_path, exist_ok=True)

    for i, chunk in enumerate(np.array_split(data, num_chunks)):
        chunk_file = os.path.join(ds_chunk_path, f"{i}.npy")
        np.save(chunk_file, chunk)
        log.info(f"Saved chunk {i} to {chunk_file}")

def load_from_chunks(dataset: Datasets, compare: bool = False) -> np.ndarray:
    """Load a dataset from chunks."""
    ds_chunk_path = os.path.join(CHUNK_PATH, str(dataset))
    # Properly create the list of files in correct order (..., 9, 10, 11, ...)
    chunk_files = [f for f in os.listdir(ds_chunk_path) if f.endswith(".npy")]
    # Sort by the chunk index
    chunk_files.sort(key=lambda x: int(x.split(".")[0]))
    chunks = [np.load(os.path.join(ds_chunk_path, f)) for f in chunk_files]
    # Store as reconstructed dataset
    if not os.path.exists(difftraj_paths[dataset]):
        path = difftraj_paths[dataset]
    else:
        path = os.path.join(BASE_DIR, "data", "processed", f"{dataset.lower()}_reconstructed.npy")
        if not compare:
            log.warning(f"Dataset {dataset} already exists. Saving to '{path}' instead.")
        # Compare the reconstructed dataset with the original
        original = np.load(difftraj_paths[dataset])
        match = np.array_equal(np.concatenate(chunks), original)
        printc(f"Loaded Dataset {dataset} matches original:", match)
        if not match:
            raise ValueError("Reconstructed dataset does not match the original.")
    if not compare:
        np.save(path, np.concatenate(chunks))
        log.info(f"Saved reconstructed dataset to {path}")
    return np.concatenate(chunks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reconstruct large datasets from chunks.")
    parser.add_argument("--compare", action="store_true",
                        help="Compare the reconstructed dataset with the original without saving.")
    parser.add_argument("--split", action="store_true", help="Split the datasets into chunks.")
    args = parser.parse_args()
    for dataset in [Datasets.GEOLIFE, Datasets.PORTO]:
        if args.split:
            split_into_chunks(dataset, CHUNK_SIZE)
        else:
            data = load_from_chunks(dataset, compare=args.compare)
            log.info(f"Successfully reconstructed {dataset} from chunks.")
