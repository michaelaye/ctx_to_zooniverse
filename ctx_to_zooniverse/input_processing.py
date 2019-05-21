# -*- coding: utf-8 -*-
from pathlib import Path

import pandas as pd


def merge_megslist_with_cumindex(path_to_input_csv, has_header=True):
    if not has_header:
        kwargs = dict(header=None, names=['CTX image name'])
    else:
        kwargs = {}
    megslist = pd.read_csv(path_to_input_csv, **kwargs)
    megslist['CTX image name'] = megslist['CTX image name'].map(lambda x: x.strip())
    df = pd.read_hdf(Path(coverage_folder / 'cumindex.h5'), 'df')
    merged = megslist.merge(df, left_on='CTX image name',
                            right_on="PRODUCT_ID")
    return merged
