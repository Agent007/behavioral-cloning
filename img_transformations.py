def cropout_sky_hood(img, hood_pixel_size=25):
    """
    https://chatbotslife.com/using-augmentation-to-mimic-human-driving-496b569760a9#.1rfh1giot
    """
    height = img.height # expecting 160
    width = img.width # expecting 320
    img = img.crop((0, int(height / 5.0), width, height - hood_pixel_size))
    return img
