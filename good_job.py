# 抠图
# 获取抠图坐标点
a = np.array(shape['points'])  # 抠图所需点坐标列表
min_w, min_h = a.min(0)
max_w, max_h = a.max(0)
# 为显示清楚，抠图各边padding20像素
img = cv2.imread()  # 原图
h, w = img.shape[0], img.shape[1]
minw = int(np.floor(min_w - 20 if (min_w - 20) > 0 else 0))
maxw = int(np.ceil(max_w + 20 if (max_w + 20) < w else w))
minh = int(np.floor(min_h - 20 if (min_h - 20) > 0 else 0))
maxh = int(np.ceil(max_h + 20 if (max_h + 20) < h else h))
# 抠图
cropped = img[minh:maxh, minw:maxw]


# excel表格坐标
ALPHABET = [chr(i) for i in range(65, 91)]
COL = ALPHABET
for CHR in ALPHABET:
    CHR_LIST = list(CHR) * 26
    EXT = [i + j for i, j in zip(CHR_LIST, ALPHABET)]
    COL = COL + EXT

