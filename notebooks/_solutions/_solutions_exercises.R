
# SOLUTIONS

## @knitr exercise1
# 1. leaflet introduction
leaflet() %>%
    addTiles() %>%  # provide a default openstreetmap background layer to the image
    addMarkers(data = pts)  %>% # Add the points to the map
    # Add the buffer polygons to the map with custom colors
    addPolygons(data = spTransform(pts_lambert_buffer, wgs_84),
                fill = FALSE, color = "Red")

## @knitr exercise2
# 2. point coordinate reprojection
#' reproject XY coordinates from dframe columns
#'
#' @param df data.frame with a x and y coordinate column
#' @param col_long (char) name of the x (longitude) column
#' @param col_lang (char) name of the y (latitude) column
#' @param project_input projection string of class CRS-class defining the
#' current projection
#' @param project_output projection string of class CRS-class defining the
#' projection to convert to
#'
#' @return data.frame with the same columns, but adapted coordinates for the
#' x and y column values
#'
reproject_points <- function(df, col_long, col_lat,
                             project_input, project_output){
    df_spat <- SpatialPoints(df[c(col_long, col_lat)],
                             proj4string = project_input)
    df_reproj <- spTransform(df_spat, project_output)
    df[c(col_long, col_lat)] <- as.data.frame(df_reproj)[c(col_long, col_lat)]
    # rename the columns to have them in the data as well
    return(df)
}

## @knitr exercise3
# 3. leaflet of Nete + centroid
leaflet() %>%
    addTiles() %>%
    addPolygons(data = spTransform(nete, wgs_84), fill = FALSE) %>%
    addCircles(data = spTransform(gCentroid(nete, byid = TRUE), wgs_84),
               color = 'red')

## @knitr exercise4
# 4. ggplot preparation of spatialLines- and spatial PolygonesDataFrames
#' Prepare a SpatialLinesDataFrame or SpatialPolygonsDataFrame for ggplot2
#' plotting
#'
#' @param spatial_df SpatialLinesDataFrame or SpatialPolygonsDataFrame
#' @return data.frame
prepare_spatial_for_ggplot <- function(spatial_df){

    df <- fortify(spatial_df)
    merge(df, as.data.frame(spatial_df))
}

## @knitr exercise5
# 5. rasterize a set of irregular spaced points
base_raster <- raster(xmn = 2.54, ymn = 49.46, xmx = 6.4, ymx = 51.51,
                      resolution = c(0.1, 0.1))
plot(rasterize(lonlat, base_raster, fun = function(x,...)length(x)))

## @knitr exercise6
# 6. Load an Arc/Info Binary Grid from file
grnt_bodem <- raster("../data/grntbodem/hdr.adf")
plot(grnt_bodem, col = bpy.colors(10))

## @knitr exercise7
# 7. Reclassify a raster file
class_table <- read.csv('../data/systemtable_example.txt',
                        sep = " ", header = FALSE)
grnt_bodem_reclassified <- reclassify(grnt_bodem, class_table)
plot(grnt_bodem_reclassified, breaks = c(0, 1, 2, 3),
     col = c(rgb(229, 245, 249, max = 255),
             rgb(153, 216, 201, max = 255),
             rgb(44, 162, 95, max = 255)))

