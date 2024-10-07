# OMERO for Developers
Materials for the **OMERO for Developers** workshop at the Jackson Laboratory, which covers:
- Using BlitzGateway and [ezomero](https://github.com/TheJacksonLaboratory/ezomero) to view images from OMERO in Python
- Retrieving thumbnails using the JSON API
- Introduction to the Zarr file format

# Set up your environment

## With any conda-like (I recommend miniforge):
```
conda env create -f environment.yml
```

## Otherwise:
You'll need to install dependencies yourself. This workshop will use `jupyterlab`, `ezomero`, `matplotlib`, `ome-zarr` and `omero-cli-zarr`. Latest versions should be fine.

# Running notebooks

Just go to your command-line, `conda activate omero_devs` and then run `jupyter lab`. Either you'll get a browser window open with Jupyter Lab, or you'll get an address to paste in your browser.

Next, we'll need to set up `config.py` - use `config_template.py` as a starting point and change it accordingly based on instructions during the workshop.

If you're using the JAX dev server (as we will during the workshop), you'll need to be on the VPN.

# Workshop notebooks

[1-Introduction.ipynb](1-Introduction.ipynb)

[2-JSON_API.ipynb](2-JSON_API.ipynb)

[3-Blitz_API.ipynb](3-Blitz_API.ipynb)

[4-Zarr.ipynb](4-Zarr.ipynb)
