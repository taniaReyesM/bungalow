from django.db import models


class House(models.Model):
    SQ_FT = 'SqFt'
    MEASURE_UNITS = [
        (SQ_FT, 'Square foots'),
    ]

    SINGLE = 'SingleFamily'
    VACANT = 'VacantResidentialLand'
    MISC = 'Miscellaneous'
    MULTI = 'MultiFamily2To4'
    CONDO = 'Condominium'
    APARTMENT = 'Apartment'
    DUPLEX = 'Duplex'

    HOME_TYPE = [
        (SINGLE, 'Single Family'),
        (VACANT, 'Vacant Residential Land'),
        (MISC, 'Miscellaneous'),
        (MULTI, 'MultiFamily2To4'),
        (CONDO, 'Condominium'),
        (APARTMENT, 'Apartment'),
        (DUPLEX, 'Duplex'),
    ]

    area_unit = models.CharField(
        max_length=4,
        choices=MEASURE_UNITS,
        default=SQ_FT,
    )

    bathrooms = models.FloatField(null=True)

    bedrooms = models.IntegerField(null=False)

    home_size = models.IntegerField(null=True)

    home_type = models.CharField(
        max_length=30,
        choices=HOME_TYPE,
        default=SINGLE,
    )

    last_sold_date = models.DateField(null=True)

    last_sold_price = models.FloatField(null=True)

    link = models.URLField(null=False)

    price = models.FloatField(null=False)

    property_size = models.IntegerField(null=True)

    rent_price = models.FloatField(null=True)

    rentzestimate_amount = models.FloatField(null=True)

    rentzestimate_last_updated = models.DateField(null=True)

    tax_value = models.FloatField(null=False)

    tax_year = models.IntegerField(null=False)

    year_built = models.IntegerField(null=True)

    zestimate_amount = models.FloatField(null=True)

    zestimate_last_updated = models.DateField(null=True)

    zillow_id = models.IntegerField(null=False)

    address = models.CharField(null=False, max_length=100)

    city = models.CharField(null=False, max_length=30)

    state = models.CharField(null=False, max_length=30)

    zipcode = models.CharField(null=False, max_length=5)
