import datetime


def transform_price(price_str):
    # normalize price house to normal number amount
    denominations = {"K": 1000, "M": 1000000}
    price_str = price_str.replace('$', '')

    denomination = price_str[-1]

    if denominations.get(denomination):
        price_str = price_str.replace(denomination, '')
        try:
            return float(price_str) * denominations.get(denomination, 1)
        except ValueError:
            print("No valid price!")
            return 0.0


def format_price(price):
    # transform a number into a price format with M for millions and K for thousands
    format_price = 0
    if price >= 1000000:
        format_price = f'{str(price / 1000000)}M'
    elif price >= 1000:
        format_price = f'{str(price / 1000)}K'
    else:
        format_price = price
    return f'${format_price}'


def transform_empty_to_none(data):
    str_fields = [
        'last_sold_date',
        'rentzestimate_last_updated',
        'zestimate_last_updated',
        'zestimate_amount',
        'last_sold_price',
        'rent_price',
        'home_size',
        'property_size',
        'year_built',
        'bathrooms',
        'rentzestimate_amount',
    ]
    for field in str_fields:
        if data.get(field) is '':
            data[field] = None
    return data


def transform_date_format(data):
    date_fields = [
        'last_sold_date',
        'rentzestimate_last_updated',
        'zestimate_last_updated',
    ]
    to_format = '%Y-%m-%d'
    from_format = '%m/%d/%Y'

    for field in date_fields:
        if data.get(field):
            data[field] = datetime.datetime.strptime(
                data.get(field), from_format).strftime(to_format)
    return data


def transform_data(data_house):
    # change empty strings to None
    data_house = transform_empty_to_none(data_house)

    # transform dates to django format
    data_house = transform_date_format(data_house)

    # normalize prices
    data_house['price'] = transform_price(data_house.get('price', ''))
    return data_house


def transform_params(query_params):
    new_params = {}
    for param, value in query_params.items():
        param = param.replace('[eq]', '').replace('[', '__').replace(']', '')
        new_params[param] = value
    return new_params
