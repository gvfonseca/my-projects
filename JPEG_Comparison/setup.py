from PIL import Image
import os
import imageio

def convert_png_to_jpeg_and_jp2_resolutions(input_png_path, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Open the PNG image
    with Image.open(input_png_path) as img:
        # Convert the image to RGB mode if it's not
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Define output paths for JPEG
        baseline_path = os.path.join(output_directory, 'baseline.jpg')
        progressive_path = os.path.join(output_directory, 'progressive.jpg')

        # Define output paths for JPEG 2000
        baseline_jp2_path = os.path.join(output_directory, 'baseline.jp2')
        progressive_jp2_path = os.path.join(output_directory, 'progressive.jp2')

        # Save as Baseline JPEG
        img.save(baseline_path, 'JPEG')

        # Save as Progressive JPEG
        img.save(progressive_path, 'JPEG', progressive=True)

        # Save as Baseline JPEG 2000
        # Please ensure that imageio.plugins.freeimage is installed or use standard imageio JPEG2000 writer
        imageio.imwrite(baseline_jp2_path, img, format='JP2')

        # Save as Progressive JPEG 2000 - Note: Progressive scan mode is not typical for JP2
        # Omitted the quality_mode argument as it's not used for JPEG 2000
        imageio.imwrite(progressive_jp2_path, img, format='JP2')

        # Save multiple resolution images for simulating Hierarchical loading
        resolutions = [1, 0.75, 0.5, 0.25]  # Different scales for resolution
        for scale in resolutions:
            width, height = img.size
            resized_img = img.resize((int(width * scale), int(height * scale)), Image.LANCZOS)
            
            # Save resized JPEG
            resized_path = os.path.join(output_directory, f'hierarchical_scale_{scale}.jpg')
            resized_img.save(resized_path, 'JPEG')
            
            # Save resized JPEG 2000
            resized_jp2_path = os.path.join(output_directory, f'hierarchical_scale_{scale}.jp2')
            imageio.imwrite(resized_jp2_path, resized_img, format='JP2')

            print(f'Resized image saved: {resized_path}')
            print(f'Resized JP2 image saved: {resized_jp2_path}')

# Usage example
convert_png_to_jpeg_and_jp2_resolutions('static/lossless/Beautiful-landscape.png', 'static')
