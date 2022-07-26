import os
import re

from concat_sdg import concat_sdg_duplicate
from digitalscience_annotation import filter_w_digital_science
from reading_cleaning_from_raw import concat_df
from utils import save_df, add_type_sdg_cat, filter_for_eu_countries, add_dst_col

if __name__ == "__main__":
    """
    # From raw csv to single dataframe
    # # SDG
    # root_sdg_path = "data/raw/SDG/"
    # for dirs in os.listdir(root_sdg_path):
    #     print(root_sdg_path+dirs)
    #     sdg_number = re.search(r'SDG-(\d+)', dirs).group(1)
    #     sdg_number = int(sdg_number)
    #
    #     df = concat_df(root_dir_path=root_sdg_path + dirs,
    #                    sdg_number=sdg_number, dst_tag="")
    #     root_exit_path = "data/dataframes/SDG/"
    #     df.to_pickle(root_exit_path + dirs + ".pkl")

    # DST

    root_dst_path = "data/raw_dst/"
    for dirs in os.listdir(root_dst_path):
        dst_tag = dirs

        df = concat_df(root_dir_path=root_dst_path + dirs,
                       sdg_number=0, dst_tag=dst_tag)
        root_exit_path = "data/dataframes/dst/"
        df.to_pickle(root_exit_path + dirs + ".pkl")

    # SDG

    root = "data/dataframes/SDG/"
    df_tot = concat_sdg_duplicate(root_path=root, typ="SDG")
    df_tot = filter_w_digital_science(df=df_tot)
    df_tot = add_type_sdg_cat(df=df_tot)
    df_tot = filter_for_EU_countries(dataframe=df_tot, how="add")
    df_tot = add_dst_col(dataframe=df_tot)
    # New DF for intersection of DST and SDG
    df_sdg_dst = df_tot[df_tot['DST']]
    df_sdg_dst.reset_index(drop=True, inplace=True)
    df_sdg_dst.to_pickle("data/output/sdg_dst.pkl")
    df_tot.to_pickle("data/output/all_sdg.pkl")
    """
    # ALL DST
    root = "data/dataframes/dst/"
    df_tot = concat_sdg_duplicate(root_path=root, typ="DST")
    df_tot = filter_for_eu_countries(dataframe=df_tot, how="add")
    df_tot.reset_index(drop=True, inplace=True)
    df_tot.to_pickle("data/output/all_digital.pkl")
    # df_tot.to_feather("data/output/all_digital_europe")
