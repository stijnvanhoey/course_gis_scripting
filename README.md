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

The course notes for the hands-on sessions are available in the [notebook](./notebooks) folder. For the Python sections, Jupyter notebook is used, while the R course material is available as Rmarkdown notebook files. Check the [Github page](https://stijnvanhoey.github.io/course_gis_scripting/#1) for the slides. The individual presentations (stored in the [docs](./docs) folder) can be used as guiding presentations to explain the setup and flow of the course. Specific focus is given to the interaction of both languages to the OSGEO libraries (proj.4, geos and gdal), which has been illustrated hands-on o the command line during the course.

## Running the course material

### Python

The Jupyterhub infrastructure described in the [setup of the Python-slideshow](https://stijnvanhoey.github.io/course_gis_scripting/python_intro.html#3) has been setup and running for the course sessions at INBO itself. Hence, it is not available as a continuous service. Still, the working Python environment can be setup locally as well, as discussed below.

By installing the [Anaconda](https://www.continuum.io/downloads) or [Miniconda](https://conda.io/miniconda.html) Python packaging environment, the required environment can be setup using the `environment.yml` file. To setup the environment, use the [Anaconda navigator tutorial](https://docs.continuum.io/anaconda/navigator/tutorials/manage-environments#importing-an-environment) or define the environment with the command line:

```bash
conda env create -f environment.yml
```
After activation of the environment (select the environment in Anaconda Navigator,  `activate gispython` (windows cmd) or `source activate gispython` (linux terminal)), start Jupyter notebooks to work on the Python notebooks. Startgin Jupyter notebook can be done directly from the Anaconda Navigator by command line:

```bash
jupyter notebook
```

**Remark:** If the usage of the environment file does not work, setup your own environment or install the most essential packages in your current working environment using conda: `conda install pandas numpy geopandas rasterio mplleaflet`. This will support most of the course material.

### R
The easiest way to start working on the Rmarkdown files is by using [Rstudio](https://www.rstudio.com/) as this IDE fully supports the Rmarkdown format. By running the first cells of the [07-gis-r-vectors.Rmd](./notebooks/07-gis-r-vectors.Rmd) notebook, the required dependencies will be installed. 

## Acknowledgements
These course notes are highly inspired by some interesting other sources:
* Excellent *Using Geospatial Data With Python*  at the  [Scipy 2013](http://kjordahl.github.io/SciPy2013) conference and *Geospatial Data with Open Source Tools in Python* at the  [Scipy 2015](http://kjordahl.github.io/SciPy-Tutorial-2015) conference by [`kjordahl`](https://github.com/kjordahl).
* Extended and great [R-GIS introduction](http://rspatial.org/index.html) by [Robert Hjimans](http://biogeo.ucdavis.edu/people.html#robert-hjimans)
* Nice *Introduction to Spatial Data Types in R* [notes](https://rstudio-pubs-static.s3.amazonaws.com/172289_67a42eebbd574197b6bb15d1ef6cfe97.html) by [Claudia Engel](https://github.com/cengel?tab=repositories)
* [Geoscripting course](https://geoscripting-wur.github.io/) by Wageningen University
* Internal INBO course material provided by [Thierry Onkelinx](https://github.com/ThierryO)
* The [Python GDAL/OGR cookbook](https://pcjericks.github.io/py-gdalogr-cookbook/index.html) by [Jared Erickson](https://github.com/pcjericks)
* The [Automating GIS processes course](https://automating-gis-processes.github.io/2016/) by [Henrikki Tenkanen]()
* Package/libraries documentation of the used packages/libraries
