# OMERO for Developers
Materials for the **OMERO for Developers** workshop at the Jackson Laboratory, which covers:
- Using BlitzGateway and [ezomero](https://github.com/TheJacksonLaboratory/ezomero) to view images from OMERO in Python
- Retrieving thumbnails using the JSON API
- Introduction to the Zarr file format

# Set up your environment

## If you use Conda:
```
conda env create -f environment.yml
```

## Otherwise:
You'll need to install dependencies yourself. This workshop will use `jupyterlab`, `ezomero`, `matplotlib`, `ome-zarr` and `omero-cli-zarr`. Latest versions should be fine.

# Workshop notebooks

[1-Introduction.ipynb](1-Introduction.ipynb)

[2-JSON_API.ipynb](2-JSON_API.ipynb)

[3-Blitz_API.ipynb](3-Blitz_API.ipynb)

[4-Zarr.ipynb](4-Zarr.ipynb)
