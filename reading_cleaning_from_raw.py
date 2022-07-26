"""
Script which takes all txt files from a folder, convert them and save them in to csv file.
"""
import csv

import pandas as pd
import os
import sys
import re
from utils import trim_py, save_df, add_country_col, c1_to_cn, \
    add_dst_cols, add_sdg_cols


def concat_df(root_dir_path, sdg_number: int, dst_tag=""):
    """

    Parameters
    ----------
    root_dir_path path
        folder path where are located all the text files used to create the concatenated db

    Returns
    -------
    dataframe
        the dataframe containing all the concatenated files

    Args:
        sdg_number (str): the number associated to the SDG
    """

    lst_of_df = []
    columns = ['PT', 'AU', 'TI', 'SO', 'LA', 'DE', 'AB', 'C1', 'EM', 'TC', 'PY',
               'WC', 'UT']
    # We explore the folder and its sub-folder looking for .txt to be read as
    # dataframes
    for subdir, dirs, files in os.walk(root_dir_path):
        size = len(files)
        for num, file in enumerate(files):
            print(f'{num}/{size}')
            file_path = subdir + '/' + file

            try:
                # Error bad lines = False to skip parsing errors
                df = pd.read_csv(file_path, sep='\t', encoding='utf-8',
                                 index_col=False, on_bad_lines="skip",
                                 quoting=csv.QUOTE_NONE)
                # we keep only a handful of useful variables, to avoid bugs,
                # we only keep the file if our 8 variables are present.

                set_columns = set(columns)
                if set_columns.issubset(set(df.columns)):
                    # making sure to only keep rows that have the proper columns
                    df = df[['PT', 'AU', 'TI', 'SO', 'LA', 'DE', 'AB', 'C1',
                             'EM', 'TC', 'PY', 'WC', 'UT']]
                else:
                    continue

                # We need to remove NaN values
                df = df.dropna(
                    subset=['PT', 'AU', 'TI', 'LA', 'DE', 'AB', 'C1', 'PY'])

                # Language = English Only
                condition_language = df.LA == "English"
                df = df[condition_language]
                df.drop('LA', axis=1, inplace=True)

                # Fixing C1 from Address to Country
                df = c1_to_cn(df)
                df = trim_py(df, 1975, 2021)

                # Adding columns with sdg number or
                # columns with DST if the raw texts are DST related

                if sdg_number != 0:
                    df = add_sdg_cols(df, sdg_number)
                if dst_tag != "":
                    df = add_dst_cols(df, dst_tag)

                lst_of_df.append(df)

            except pd.errors.ParserError:
                # print("Parser Error", file_path)
                continue
            except pd.errors.EmptyDataError:
                print("No columns to parse from file")
                print(file_path)
                continue

    #  Concatenation
    df_concat = pd.concat(lst_of_df)

    # Removing Duplicates
    df_concat = df_concat.drop_duplicates(['UT'], keep='last')

    # Categorical values
    df_concat['PT'] = df_concat['PT'].astype('category')
    df_concat['PY'] = df_concat['PY'].astype('category')
    df_concat['WC'] = df_concat['WC'].astype('category')
    df_concat['TC'] = df_concat['TC'].astype('int')

    return df_concat


if __name__ == "__main__":

    # MODIFY root_dir and final_path here or add them as arguments
    """
    root_dir = "data/raw_dst/AI"

    df = concat_df(root_dir, sdg_number=0, dst_tag="AI")
    df.to_pickle("data/dataframes/AI.pkl")

    print(df.PY.describe())
    print(df.info())
    print(df.CN.head(10))
    """
    root_superdir_path = "data/raw_dst/DST_pre_2010/"
    for dirs in os.listdir(root_superdir_path):
        # sdg_number = re.search(r'SDG-(\d+)', dirs).group(1)
        # sdg_number = int(sdg_number)
        dst_tag = dirs
        print(dst_tag)

        df = concat_df(root_dir_path=root_superdir_path + dirs,
                       sdg_number=0, dst_tag=dst_tag)
        root_exit_path = "data/dataframes/dst_pre_2009/"
        save_df(df, root_exit_path + dirs + ".pkl")

