# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from typing import Final
from os import path, mkdir
from glob import glob

k_raw_base_dir: Final = "data/raw"
k_processed_base_dir: Final = "data/processed"

@click.command()
@click.argument('input_name', type=click.Path())
@click.argument('output_name', type=click.Path())
def main(input_name, output_name):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    raw_data_path = path.join(k_raw_base_dir, input_name) 
    if not path.exists(raw_data_path):
        raise ValueError("Given data directory does not exist")

    train_fpath    = glob(path.join(raw_data_path, "*.train"))[0]
    dev_fpath      = glob(path.join(raw_data_path, "*.dev"))[0]
    test_fpath     = glob(path.join(raw_data_path, "*.test"))[0]
    dev_key_fpath  = glob(path.join(raw_data_path, "*.dev.key"))[0]
    test_key_fpath = glob(path.join(raw_data_path, "*.test.key"))[0]

    proc_data_path = path.join(k_processed_base_dir, output_name)

    if not path.exists(proc_data_path):
        mkdir(proc_data_path)

    write_inp_data(train_fpath, path.join(proc_data_path, "train.dat"))
    write_inp_data(dev_fpath, path.join(proc_data_path, "dev.dat"))
    write_inp_data(test_fpath, path.join(proc_data_path, "test.dat"))



def write_inp_data(input_path, output_path):
    with open(input_path, "r") as fi:
        data = fi.read()

    data = data.split("\n\n")
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    main()
