import os
import shutil
import json

# 이미지 경로, 라벨링 경로 폴더 받는 변수 2개 생성
img_dir = 'C:/남서울대/2022 졸작-캡스톤/2020-02-062.도로장애물표면인지(광역시등)_sample/062.도로장애물-표면인지영상(광역시 등)_샘플_원천데이터'
label_dir = 'C:/남서울대/2022 졸작-캡스톤/2020-02-062.도로장애물표면인지(광역시등)_sample/062.도로장애물-표면인지영상(광역시 등)_샘플_라벨링데이터'


# 결과저장폴더 지정
ouput_dir = 'C:/남서울대/2022 졸작-캡스톤/2020-02-062.도로장애물표면인지(광역시등)_sample/2_pothole'

#directory = 'C:/Coding/'
keywords = {'pothole': '8'}


for label_file_name in os.listdir(label_dir):
    if not label_file_name[-4:] == 'json':
        continue

    with open(lable_file_path := os.path.join(label_dir, label_file_name), 'r', encoding='UTF-8') as f:
        data = json.load(f)['annotations']
        number_of_labels = len(data)
        for i in range(number_of_labels):
            if str(data[i]['category_id']) == keywords['a']:
                img_file_name = label_file_name[:-10] + '.png'
                img_file_path = os.path.join(img_dir, img_file_name)
                # move 대신 copy 사용
                shutil.copy(lable_file_path, ouput_dir)
                shutil.copy(img_file_path, ouput_dir)
                exit = True
                break