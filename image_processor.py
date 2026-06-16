import cv2

class ImageProcessing:
    def __init__(self):
        self.image = None

    def read_image(self, path):
        #Reads the image from the given path and stores it.
        self.image = cv2.imread(path)
        if self.image is None:
            print(f"Error: Could not read image at '{path}'. Check the path.")
        return self.image

    def show_image(self, window_name="Processed Image"):
        #Displays the currently loaded image.
        if self.image is not None:
            cv2.imshow(window_name, self.image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("No image is currently loaded to display.")

    def save_image(self, save_path):
        #Saves the currently loaded/edited image to the specified path.
        if self.image is not None:
            # save_path must include a valid extension, e.g., "newImage.jpg"
            success = cv2.imwrite(save_path, self.image)
            if success:
                print(f"Image successfully saved to '{save_path}'")
            else:
                print("Error: Could not save the image.")
            return success
        else:
            print("No image is currently loaded to save.")
            return False

    def resize(self,image):