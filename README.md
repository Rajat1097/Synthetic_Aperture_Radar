# Synthetic_Aperture_Radar
## SAR data downloading and processing 

-----------------------------------------------------------
### data_download
#### Downloads the Sentinel 1 satellite data from the Alaskan Facility center, and change the parameters such as date, orbit, and polarization according to the study. 
----------------------------------------------------------

### data_preprocess
#### Batch preprocessing the Sentinel 1 data using graph tool. Change the input directory where all your raw files are stored and output to the path where you want to store all your files
#### steps in preprocessing 
#### 1) Apply orbit file
#### 2) Thermal noise removal
#### 3) Calibration
#### 4) Terrain correction
#### 5) Linear to Db conversion 
#### 6) Clip to the area of interest (Change the co-ordinates according to your study area)

### Graph.xml
#### graph file where all the instructions for the preprocessing are saved. YOu can change it according to your requirements. An easy way to change is to prepare a file using SNAP software. You can even add a smoothening filter. 
