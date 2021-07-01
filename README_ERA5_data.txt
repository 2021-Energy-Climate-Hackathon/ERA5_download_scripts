********
*
*
* Details of the ERA5 data in /gws/pw/j05/cop26_hackathons/oxford/Data/ERA5_data_EU_domain
*
*
*
*********


The data has been downloaded in individual files per month.
The file format is ERA5_1hr_field_set_X_YEAR_MONTH.nc

So for example:

ERA5_1hr_field_set_1_2020_01.nc

Is hourly data for ERA5, for the year 2020, and month 1 (January)
Please note all februarys have 28 days. If you require the leapdays then
contact h.c.bloomfield@reading.ac.uk to discuss.

Data has been downloaded over a European domain
Latitudes: 35N --> 75N
Longitudes: -22E --> 35W

There are 3 sets of fields downloaded:

********************************************
*field_set_1 contains (with the netcdf keys):
********************************************

- longitudes, (longitude)
- latitudes, (latitude)
- time, (time)
- eastward component of wind at 10m (u10)
- northward component of wind at 10m (v10)
- eastward component of wind at 100m (u100)
- northward component of wind at 100m (v100)
- 2m temperature (t2m)
- maximum 2m temperature (mx2t)
- minimum 2m temperature (mn2t)
- mean sea level pressure (msl)
- Surface solar radiation downwards (ssrd)

********************************************
*field_set_2 contains (with the netcdf keys):
********************************************
- longitudes, (longitude)
- latitudes, (latitude)
- time, (time)
- Runoff (ro)
- Snowfall (sf)
- Total cloud cover (tcc)
- Total precipitation (tp)

********************************************
*field_set_3 contains (with the netcdf keys):
********************************************

- longitudes, (longitude)
- latitudes, (latitude)
- time, (time)
- level (level)
- eastward component of wind 
- northward component of wind 


In field set 3 the eastward and northward component of the wind are stored in arrays with dimensions [time,level,latitude,longitude] where the three levels are:

- 700 hPa
- 850 hPa
- 925 hPa

These levels represent the height of the constant pressure level that the measurements were taken from.

***********************
**** FURTHER TIPS *****
***********************


- Use the command ncdump -h filename.nc to print the headers of the .nc file and see what is in them
- If you are unfamiliar with reading .nc files example scripts will be available in python (ask Hannah for their location - she will update this README when she's worked out where to put them! :-) )
- If you require a field that is not included in this information then please contact Hannah to discuss downloading it into a new field set. field_set_4.



