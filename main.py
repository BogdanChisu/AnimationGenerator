import os
import cv2
from PIL import Image

#Checking the current directory path
print(os.getcwd())

# Folder which contains all the images
# from which the video is to be generated
os.chdir(r"D:\running_pics\CK24\0RPM")
path = r"D:\running_pics\CK24\0RPM"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))
print(f"Number of image files is {num_of_images}")

for file in os.listdir('.'):
    im = Image.open(os.path.join(path, file))
    width, height = im.size
    mean_width += width
    mean_height += height
    # im.show() # uncomment to show the image

mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

print(f"Mean image dimensions are {mean_width} x {mean_height}")

# -----------------------------------------------------------------------------
# Resizing the images to make give them
# the same width and height

for file in os.listdir('.'):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        # opening image using PIL Image
        im = Image.open(os.path.join(path, file))

        # im.size includes the height and width of image
        width, height = im.size
        print(f"Original image dimensions are: {width} x {height}")

        # resizing
        imResized = im.resize((mean_width, mean_height))
        imResized.save(file, 'JPEG', quality = 95) # quality setting

# Video Generating Function
def generate_video():
    image_folder = r"D:\running_pics\CK24\0RPM"
    video_name = "0RPM.avi"
    os.chdir(r"D:\PycharmProjects\animationGenerator")


    # Images list will only consider the image files
    # ignoring others if any
    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
                 img.endswith("jpeg") or
                 img.endswith("png")]

    print(f"The images list: \n {images}")

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    # setting the frame width, height
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 10, (width, height))

    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # Deallocating memories taken for window creation
    cv2.destroyAllWindows()
    video.release() # releasing the video generated


def main():
    generate_video()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
