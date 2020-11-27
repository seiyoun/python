from PIL import ImageGrab

for i in range(1, 11):
    # スキルキャプチャ
    img = ImageGrab.grab()
    # 保存
    img.save("image{}.png".format(i))
