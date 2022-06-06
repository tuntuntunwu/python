import cv2
from pyzbar import pyzbar


def decodeDisplay(image):
    barcodes = pyzbar.decode(image)  # 尝试识别所有bar codes
    # print(barcodes)
    if barcodes:
        for barcode in barcodes:

            barcodeData = barcode.data.decode("UTF8")
            barcodeType = barcode.type
            # 向终端打印条形码数据和条形码类型
            print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
            return 1

            # 提取二维码的边界框的位置
            # 画出图像中条形码的边界框
            # (x, y, w, h) = barcode.rect
            # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # 绘出图像上条形码的数据和条形码类型
            # text = "{} ({})".format(barcodeData, barcodeType)
            # cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,.5, (0, 0, 125), 2)
    else:
        print("No QRCODE")
        return 0


if __name__ == '__main__':
    # 转为灰度图像
    img = cv2.imread("./6.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    decodeDisplay(gray)
    print("------")
    img = cv2.imread("./7.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    decodeDisplay(gray)
    print("------")
    img = cv2.imread("./multi.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    decodeDisplay(gray)
    # img = decodeDisplay(gray)
    # cv2.imshow("data", img)

