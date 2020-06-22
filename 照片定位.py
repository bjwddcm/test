import exifread


def get_long_and_lot(photo):
    """
    :param photo:  传入图片路径
    :return:
    """
    f = open('D://3.jpg', 'rb')	# 二进制打开图片
    msg = exifread.process_file(f)

    try:
        exif_longitude = msg['GPS GPSLongitude']		# 图片经度
        exif_latitude = msg['GPS GPSLatitude']			# 图片纬度
        exif_create_date = msg['EXIF DateTimeOriginal']	# 创建图片日期
        print(exif_longitude, exif_latitude, exif_create_date)
        # 返回的值 [113, 20, 1574707/62500] [23, 8, 4155487/200000] 2019:12:09 14:57:32

    except:
        print('Error！！图片中不包含Gps信息')

get_long_and_lot('图片路径')
