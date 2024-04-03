import os
from PIL import Image
from pillow_heif import register_heif_opener

class HeicConverter():

    def __init__(self, path) -> None:
        register_heif_opener()
        self.dir_path = path
        self.out_path = path
        self.images = self.__find_heic_images()
        print(f"Path: {self.dir_path}\nImages: {self.images}\n")

    def __find_heic_images(self) -> list:
        images = [
            os.path.join(self.dir_path, f)
            for f in os.listdir(self.dir_path)
            if f.endswith(".heic")
        ]
        return images

    def __convert_image(self, img_path: str) -> None:
        img = Image.open(img_path)
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        img.save(os.path.join(self.out_path, f"{base_name}.jpeg"), format="JPEG")

    def convert_all(self, progress_callback=None) -> None:
        n = len(self.images)
        for i, img in enumerate(self.images, start=1):
            self.__convert_image(img)
            if progress_callback:
                progress_callback(i, n)
