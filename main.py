# import cv2
# import numpy as np
# import uuid
import os

# def readsave(filename, savepath='output/',inputpath='images/'):
#     src = cv2.imread(inputpath + filename)
#     if src is None:
#         print('Image load failed!')
#     src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
#     # 초록색 범위를 넢게 잡아서 초록색을 추
#     # dst1 = cv2.inRange(src_hsv, (50, 100, 100), (70, 255, 255))
#     dst1 = cv2.inRange(src_hsv, (30, 100, 100), (90, 255, 255))
#     y_indices, _ = np.where(dst1 != 0)
#     if y_indices.size > 0:
#         min_y = np.max(y_indices)
#         cropped_src = src[min_y:, :]
#         cv2.imwrite(savepath+filename, cropped_src)
#     else:
#         print(f"No non-zero pixels found in {filename}")
#         # show the image
#         cv2.imshow("Image", src)
#         cv2.imshow("Mask", dst1)

#         cv2.waitKey(0)

#         return
#     cropped_src = src[min_y:, :]
#     cv2.imwrite(savepath+filename,cropped_src)


# def main():
#     all_files = os.listdir('images')

#     for file in all_files:
#         print(file)
#         readsave(file)
#     print('Done')

# if __name__ == '__main__':
#     main()
print(os.listdir('output'))