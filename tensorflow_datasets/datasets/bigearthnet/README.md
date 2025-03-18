The BigEarthNet is a new large-scale Sentinel-2 benchmark archive, consisting of
590,326 Sentinel-2 image patches. The image patch size on the ground is 1.2 x
1.2 km with variable image size depending on the channel resolution. This is a
multi-label dataset with 43 imbalanced labels.

To construct the BigEarthNet, 125 Sentinel-2 tiles acquired between June 2017
and May 2018 over the 10 countries (Austria, Belgium, Finland, Ireland, Kosovo,
Lithuania, Luxembourg, Portugal, Serbia, Switzerland) of Europe were initially
selected. All the tiles were atmospherically corrected by the Sentinel-2 Level
2A product generation and formatting tool (sen2cor). Then, they were divided
into 590,326 non-overlapping image patches. Each image patch was annotated by
the multiple land-cover classes (i.e., multi-labels) that were provided from the
CORINE Land Cover database of the year 2018 (CLC 2018).

Bands and pixel resolution in meters:

*   B01: Coastal aerosol; 60m
*   B02: Blue; 10m
*   B03: Green; 10m
*   B04: Red; 10m
*   B05: Vegetation red edge; 20m
*   B06: Vegetation red edge; 20m
*   B07: Vegetation red edge; 20m
*   B08: NIR; 10m
*   B09: Water vapor; 60m
*   B11: SWIR; 20m
*   B12: SWIR; 20m
*   B8A: Narrow NIR; 20m

License: Community Data License Agreement - Permissive, Version 1.0.

URL: http://bigearth.net/
