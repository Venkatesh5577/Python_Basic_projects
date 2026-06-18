import cv2
import os


UPLOAD_FOLDER = "images"
OUTPUT_FOLDER = "images"


# create folders if not exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def resize_image(
        filename,
        scale_percent=50,
        quality=60
    ):

    input_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    output_path = os.path.join(
        OUTPUT_FOLDER,
        "resized_" + filename
    )


    # read image
    img = cv2.imread(
        input_path,
        cv2.IMREAD_UNCHANGED
    )


    if img is None:
        print("Image not found")
        return


    # original size
    height = img.shape[0]
    width = img.shape[1]


    # calculate new size
    new_width = int(
        width * scale_percent / 100
    )

    new_height = int(
        height * scale_percent / 100
    )


    # resize
    resized = cv2.resize(
        img,
        (new_width,new_height),
        interpolation=cv2.INTER_AREA
    )


    # save with compression
    cv2.imwrite(
        output_path,
        resized,
        [
            cv2.IMWRITE_JPEG_QUALITY,
            quality
        ]
    )


    print("Done!")
    print("----------------")
    print("Original:")
    print(width, "x", height)

    print("New:")
    print(new_width, "x", new_height)

    print("Saved at:")
    print(output_path)



# -------------------------
# RUN PROGRAM
# -------------------------

file = input(
    "Enter image name: "
)


scale = int(
    input(
    "Enter resize percentage (example 50): "
    )
)


quality = int(
    input(
    "Enter quality 0-100: "
    )
)


resize_image(
    file,
    scale,
    quality
)