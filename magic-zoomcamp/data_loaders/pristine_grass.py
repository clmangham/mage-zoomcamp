from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
from typing import Dict, List
import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


config_path = path.join(get_repo_path(), 'io_config.yaml')
config_profile = 'default'

bucket_name = 'zoomcamp-clm'

@data_loader
def load_data(*args, **kwargs) -> List[List[Dict]]:
    df_list = []
    metadata = []

    for i in ['04', '05']:
        object_key = f'yellow/yellow_tripdata_2020-{i}.parquet'
        curr_df = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).load(
        bucket_name,
        object_key,
        )
        print(type(curr_df))

        break


        df_list.append(dict(id=i, name=f'df_{i}', df = curr_df))
        metadata.append(dict(block_uuid=f'for_df_{i}'))

    return [
        df_list,
        metadata,
    ]

