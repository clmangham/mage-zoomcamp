import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from typing import Dict, List



@data_loader
def dataframe_generator(*args, **kwargs):
    months = ['04', '05']   
    for month in months:
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz'
        yield pd.read_csv(url, sep=",", compression='gzip')


# def load_data_from_api(*args, **kwargs):
#     df_generator = dataframe_generator(months)
#     print(df_generator)

    

#     return df_generator



# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'