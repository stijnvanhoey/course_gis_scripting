# Introduction to scripting GIS analysis

## Introduction

These course notes provide an introduction to the usage of Python and R for GIS procedures. The course notes were developed for a hands-on session at the [Institute for Nature and Forest Research (INBO)](ww.inbo.be), May 2017.

The course can be split up in three main sections:
1. Introduction to (scientific) Python: crash course introduction to the Python standard library and some essential scientific Python packages (Numpy/Pandas). Still, for a more extended introduction course of (scientific) Python, check these [course notes](https://github.com/jorisvandenbossche/DS-python-data-analysis) providing a more extended Python introduction.
  * [00-jupyter_introduction.ipynb](./notebooks/00-jupyter_introduction.ipynb)
  * [01-python-introduction.ipynb](./notebooks/01-python-introduction.ipynb)
  * [02-scientific-python-introduction.ipynb](./notebooks/02-scientific-python-introduction.ipynb)
2. Introduction to Python for GIS: Introduction to some essential vector and raster packages in Python, such as `geopandas`, `fiona`, `rasterio`, ...
  * [03-geopandas-appetizer.ipynb](./notebooks/03-geopandas-appetizer.ipynb)
  * [04-gis-python-vectors.ipynb](./notebooks/04-gis-python-vectors.ipynb)
  * [05-the-power-of-gdal.ipynb](./notebooks/05-the-power-of-gdal.ipynb)
  * [06-gis-python-rasters.ipynb](./notebooks/06-gis-python-rasters.ipynb)
3. Introduction to R for GIS: introduction to some essential vector and raster packages in R, such as `sp`, `raster`, `ggmap`, ...
  * [07-gis-r-vectors.Rmd](./notebooks/07-gis-r-vectors.Rmd)
  * [08-gis-r-rasters.Rmd](./notebooks/08-gis-r-rasters.Rmd)

The course notes are available in the [notebook](./notebooks) folder. For the Python sections, Jupyter notebook is used, while the R course material is available as Rmarkdown notebook files. The individual presentations in the [docs](./docs) folder can be used as guiding presentations to explain the setup and flow of the course. Specific focus is given to the interaction of both languages to the OSGEO libraries (proj.4, geos and gdal).

## Running the course material

### Python
By installing the Anaconda or Miniconda packaging environment, the required environment can be setup using the `environment.yml` file.

### R
The easiest way to start working on the Rmarkdown files is by using Rstudio. By running the first cells of the [07-gis-r-vectors.Rmd](./notebooks/07-gis-r-vectors.Rmd) notebook, the required dependencies are installed. 

## Acknowledgements
These course notes are translated from some interesting sources:
* Excellent introduction by `kjordahl` at the  [EuroScipy 2013](http://kjordahl.github.io/SciPy2013) and  [EuroScipy 2015](http://kjordahl.github.io/SciPy-Tutorial-2015) conferences
* Extended and great [R-GIS introduction](http://rspatial.org/index.html)
* Internal INBO course material provided by [Thierry Onkelinx]()
