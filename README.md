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

## If you use Docker:
On Windows:
```
docker build -t omero_devs -f Dockerfile .
docker run -it -p 8888:8888 -v <local_path_to_mount>:/home/jovyan/mounted omero_devs
```

On Mac:
```
docker build --platform linux/amd64 -t omero_devs -f Dockerfile .
docker run -it -p 8888:8888 -v <local_path_to_mount>:/home/jovyan/mounted \
--platform linux/amd64 omero_devs
```

# Workshop notebooks

[1-Introduction.ipynb](1-Introduction.ipynb)

[2-JSON_API.ipynb](2-JSON_API.ipynb)

[3-Blitz_API.ipynb](3-Blitz_API.ipynb)

[4-Zarr.ipynb](4-Zarr.ipynb)