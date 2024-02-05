import re
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print(f"Preprocessing: rows with zero passengers = {data['passenger_count'].isin([0]).sum()}")

    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # print('Upon filtering the dataset where the passenger count is equal to 0 or the trip distance is equal to zero, how many rows are left?')
    # print(data.shape[0])

    
    # print('What are the existing values of vendorID?')
    # print(data['VendorID'].unique())
    # print(data.columns)



    # data.columns = (data.columns
    #             .str.replace(' ', '_')
    #             .str.lower()
    # )

    # def snake_case(column):
    #     return column.replace(r'(?<!^)(?=[A-Z])', '_')

    # cols_list = []
    # for column in data.columns:
    #     cols_list.append(snake_case(column))

    # data.columns = cols_list

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance'
    # assert 'vendor_id' is in data.columns
 



