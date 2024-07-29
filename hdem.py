import click
import rasterio
from scipy.ndimage import zoom
import numpy as np

def upscale_dem(input_path, output_path, scale_factor):
    # Load SRTM data
    with rasterio.open(input_path) as src:
        srtm_data = src.read(1)
        transform = src.transform
        profile = src.profile

    # Use scipy's zoom function to upscale the DEM
    high_res_dem = zoom(srtm_data, scale_factor, order=3)  # cubic interpolation

    # Update the transform and profile for the new resolution
    new_transform = rasterio.Affine(transform.a / scale_factor, transform.b, transform.c,
                                    transform.d, transform.e / scale_factor, transform.f)
    profile.update({
        'height': high_res_dem.shape[0],
        'width': high_res_dem.shape[1],
        'transform': new_transform
    })

    # Save the upscaled DEM
    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(high_res_dem, 1)

    print(f"High-resolution DEM saved to: {output_path}")

@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.option('--scale', default=2.0, help='Scale factor for upscaling. Default is 2.0.')
def main(input_path, output_path, scale):
    """Upscale a DEM file using cubic interpolation."""
    upscale_dem(input_path, output_path, scale)

if __name__ == "__main__":
    main()
