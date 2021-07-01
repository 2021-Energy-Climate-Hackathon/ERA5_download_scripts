import cdsapi


for YEAR in range(2015,2021):
    for MONTH in range(1,13):

        if MONTH in [9,4,6,11]:
            day_data = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
        elif MONTH in [2]:
            day_data = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
        else: 
            day_data = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        m = str(MONTH).zfill(2) # make sure it is 01, 02 etc
        y = str(YEAR)
        c = cdsapi.Client()
        c.retrieve('reanalysis-era5-single-levels',
        {'product_type': 'reanalysis',
        'variable': ['100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_wind','10m_v_component_of_wind', '2m_temperature', 'maximum_2m_temperature_since_previous_post_processing','mean_sea_level_pressure', 'minimum_2m_temperature_since_previous_post_processing', 'surface_solar_radiation_downwards'],
        'year': [y],
        'month': [m],
        'day': day_data,
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',],
        'area': [72, -22, 35, 35,],
        'format': 'netcdf',
    },
                    
    'ERA5_1hr_field_set_1_' + y + '_' + m + '.nc')
