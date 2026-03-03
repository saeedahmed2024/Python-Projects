import cv2

source = "panaversity.png"
destination = "panaversity_resized.png"

while True:
    try:
        percentage_scale = int(input("Enter the percentage scale (how much you want to scale the image): "))
        break
    except ValueError:
        print("Please enter a number.")

image = cv2.imread(source)

user_width = int(image.shape[1] * (percentage_scale/100))
user_height = int(image.shape[0] * (percentage_scale/100))
resize_points = (user_width, user_height)

resized_image = cv2.resize(image, resize_points, interpolation = cv2.INTER_LINEAR)

cv2.imshow("Resized image", resized_image)
cv2.waitKey(0)

cv2.destroyAllWindows()

save_image = input("Do you want to save this image? (y/n): ").lower()
if save_image == "y":
    cv2.imwrite(destination, resized_image)

#press any key to close all windows

