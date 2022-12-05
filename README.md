# OMERO for Developers
Materials for the **OMERO for Developers** workshop at the Jackson Laboratory, which covers:
- Using BlitzGateway and [ezomero](https://github.com/TheJacksonLaboratory/ezomero) to view images from OMERO in Python
- Retrieving thumbnails using the JSON API
- Introduction to the Zarr file format

# Set up your environment

## If you use Conda:
On Windows (worked on Windows as of 2020, has not been checked recently): 
```
conda env create -f environment_windows.yml
```

On Mac (works on Mac OS 12.6 with M1 chip as of Oct 2022): 
```
conda env create -f environment_mac.yml
```

## If you use pip:
 ```
 pip -r requirements.txt
 ```

## If you use Docker:
```
docker build -t omero_devs -f Dockerfile .
```
NOTE: does not currently work on ARM (M1) Macs because zeroc-ice wheel expects x86 architecture

# Workshop notebooks

[1-Introduction.ipynb](1-Introduction.ipynb)

[2-JSON_API.ipynb](2-JSON_API.ipynb)

[3-Blitz_API.ipynb](3-Blitz_API.ipynb)

[4-Zarr.ipynb](4-Zarr.ipynb)