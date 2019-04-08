import numpy as np
import cv2
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def cv_imread(file_path):
    ''' read .png .jpg .gif to BGR np.array '''
    img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    if img is None:
        img = Image.open(file_path).convert('RGB')
        img = np.array(img)[:,:,[2, 1, 0]]  # convert to BGR
    return img

def cv_imwrite(img, file_path):
    ''' save .png .jpg .gif to .jpg '''
    cv2.imencode('.jpg', img)[1].tofile(file_path)

if __name__ == '__main__':
    pass
