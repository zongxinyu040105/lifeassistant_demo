import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.original_img = cv2.imread(image_path)
        #self.image_path =  "D:\\de_whelk.jpg"
        #self.original_img = cv2.imread("D:\\de_whelk.jpg")

        self.img = self.original_img.copy()
        self.whelk_xy = []
        self.k = 3  # Kernel size or other parameters can be adjusted here.

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.find_xy)

    def pixel_change(self, img, h, w, k, flag):
        sum_rgb = [0, 0, 0]
        h_min = int(h - (k - 1) / 2)
        h_max = int(h + (k - 1) / 2)
        w_min = int(w - (k - 1) / 2)
        w_max = int(w + (k - 1) / 2)

        if flag == 1:  # Top
            for width in range(w_min, w_max + 1):
                sum_rgb[0] += img[h - 1][width][0] / k
                sum_rgb[1] += img[h - 1][width][1] / k
                sum_rgb[2] += img[h - 1][width][2] / k
        elif flag == 2:  # Bottom
            for width in range(w_min, w_max + 1):
                sum_rgb[0] += img[h + 1][width][0] / k
                sum_rgb[1] += img[h + 1][width][1] / k
                sum_rgb[2] += img[h + 1][width][2] / k
        elif flag == 4:  # Right
            for height in range(h_min, h_max + 1):
                sum_rgb[0] += img[height][w + 1][0] / k
                sum_rgb[1] += img[height][w + 1][1] / k
                sum_rgb[2] += img[height][w + 1][2] / k
        else:  # Left
            for height in range(h_min, h_max + 1):
                sum_rgb[0] += img[height][w - 1][0] / k
                sum_rgb[1] += img[height][w - 1][1] / k
                sum_rgb[2] += img[height][w - 1][2] / k
        return sum_rgb

    def find_xy(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.whelk_xy.append([x, y])
            num = int(len(self.whelk_xy) / 2)
            if len(self.whelk_xy) % 2 == 0:
                cv2.rectangle(self.img, self.whelk_xy[2 * (num - 1)],
                              self.whelk_xy[2 * num - 1], (0, 0, 255), 1)

    def process_image(self):
        assert len(self.whelk_xy) % 2 == 0
        for k in range(int(len(self.whelk_xy) / 2)):
            w = [self.whelk_xy[2 * k][0], self.whelk_xy[2 * k + 1][0]]
            h = [self.whelk_xy[2 * k][1], self.whelk_xy[2 * k + 1][1]]
            while w[1] - w[0] > 0 and h[1] - h[0] > 0:
                for i in w:  # w
                    for j in range(h[0], h[1]):  # h
                        if i == w[0]:
                            flag = 3
                        elif i == w[1]:
                            flag = 4
                        self.img[j][i] = self.pixel_change(self.img, j, i, self.k, flag)
                for j in h:  # h
                    for i in range(w[0], w[1]):
                        if j == h[0]:
                            flag = 1
                        elif j == h[1]:
                            flag = 2
                        self.img[j][i] = self.pixel_change(self.img, j, i, self.k, flag)
                w[0] += 1
                w[1] -= 1
                h[0] += 1
                h[1] -= 1
        cv2.imwrite("D:\\output\\processed_image.jpg", self.img)

    def display_image(self):
        while True:
            cv2.imshow('image', self.img)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):  # quit the program
                break

        cv2.destroyAllWindows()

    def run(self):
        self.display_image()
        if len(self.whelk_xy) % 2 == 0 and len(self.whelk_xy) > 0:
            self.process_image()
            self.display_image()
        else:
            print("Please select pairs of points.")

    @staticmethod
    def open_cvface_window(origin_image):
         #image_path = 'path/to/your/image.jpg'  # Replace with your image path
         processor = ImageProcessor(origin_image)
         processor.run()
#if __name__ == "__main__":
   # image_path = 'path/to/your/image.jpg'  # Replace with your image path
    #processor = ImageProcessor(image_path)
   # processor.run()


