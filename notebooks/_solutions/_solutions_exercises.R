
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




