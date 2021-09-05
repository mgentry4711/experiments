import sys # for access to the command line arguments
import numpy as np # for numerical python operations
import xarray as xr # for netCDF manipulation
from matplotlib import pyplot as plt # plotting module

'''sys.argv is a list of the space-delimited arguments passed to python from the command line.
You would call this script: "python3 python_commandline.py input output

Example:
matthewgentry$ python3 zonal_mean.py ~/CESM/munged/LENS/TS/b.e11.BRCP85C5CNBDRD.f09_g16.002.cam.h0.TS.208101-210012.meanstate.nc

If you get an error that looks like:

YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.

I did too - it's from importing xarray, and it doesn't affect the script.'''

## assign elements of the list sys.argv to variables
script_name = sys.argv[0] # the name of the script
inpath = sys.argv[1] # the path to the input file

data_in = xr.open_dataarray(inpath, decode_times=False)
## Plot the input data
# plt.figure()
# data_in.plot()

## Define a function for the desired operation.
def F(ds):
    # take the mean over the dimension 'lon'
    # this should work for CAM output.
    y = ds.mean('lon') 
    return y

## Apply the function to the input file
data_out = F(data_in)

### Plot the processed data
plt.figure()
data_out.plot()
plt.show()

## save the processed xr.DataArray object to a .nc file with a new prefix, in the same directory as the input file.
outpath = inpath.split('.nc')[0] + '.zonalmean.nc'
print(outpath)
data_out.to_netcdf(outpath)



