# hdem: High DEM Upscaler CLI Tool

This repository contains hdem, a command-line tool for upscaling Digital Elevation Models (DEMs) using cubic interpolation. The tool leverages the rasterio and scipy libraries to read, process, and save DEM data.

It is not intended to accurately represent the underlying terrain. It comes in handy when making more real looking 3D models. 

## Installation

To use the hdem upscaler tool, you need to have Python installed. Additionally, you need to install the required dependencies:

``` 
pip install -r requirements.txt
```

## Usage 

The CLI tool takes an input DEM file, an output path for the upscaled DEM, and an optional scale factor.

### Command-Line Usage

```bash
python hdem.py <input_path> <output_path> --scale <scale_factor>
```

- `input_path`: Path to the input DEM file (e.g., path_to_your_srtm_data.tif).
- `output_path`: Path to save the upscaled DEM file (e.g., path_to_save_high_res_dem.tif)
- `--scale` (Optional): Scale factor for upscaling. Default is 2.0.

For example, to upscale a DEM by a factor of 5:

```bash
python hdem.py example_dem.tif upscaled_dem.tif --scale 5
```