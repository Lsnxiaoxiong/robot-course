import cv2

scale = 0.5  # 缩放到原来的 50%
def show_scaled(win, image, scale):
    h, w = image.shape[:2]
    interp = cv2.INTER_AREA if scale < 1.0 else cv2.INTER_LINEAR
    resized = cv2.resize(image, (int(w*scale), int(h*scale)), interpolation=interp)
    cv2.imshow(win, resized)

img = cv2.imread("tonypi.png")
# 2. 转换到 YCrCb 颜色空间
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv2.split(ycrcb)

# 3. 模拟 JPEG 压缩：降低色度分辨率（4:2:0）
Cr_down = cv2.resize(Cr, (Cr.shape[1]//2, Cr.shape[0]//2), interpolation=cv2.INTER_AREA)
Cb_down = cv2.resize(Cb, (Cb.shape[1]//2, Cb.shape[0]//2), interpolation=cv2.INTER_AREA)

# 再上采样回原尺寸
Cr_up = cv2.resize(Cr_down, (Cr.shape[1], Cr.shape[0]), interpolation=cv2.INTER_LINEAR)
Cb_up = cv2.resize(Cb_down, (Cb.shape[1], Cb.shape[0]), interpolation=cv2.INTER_LINEAR)

# 4. 合并回 YCrCb 并转换为 BGR
compressed_ycrcb = cv2.merge([Y, Cr_up, Cb_up])
compressed_img = cv2.cvtColor(compressed_ycrcb, cv2.COLOR_YCrCb2BGR)

show_scaled("ori", img, 0.5)
show_scaled("compressed_img", compressed_img, 0.5)

cv2.imwrite("crowd_compressed.jpeg", compressed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
