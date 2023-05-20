## 天池学习赛——街景字符编码识别 
_Creator： govT_

`Yolov5使用的重点在于：将自己的数据集制作成Yolo需要的格式，之后便可直接使用Yolov5训练、预测
`
*********

**1 **制作数据集****

**1.1** 下载官网数据集至mycoco/all_download_data/目录下, 下载链接见mchar_data_list_0515.csv

**1.2**  运行merge_images.py文件（将所有数据集存放至mycoco/all_images/）

**1.3**  运行json_to_txt.py文件（制作所有图片对应的txt标签，存放至mycoco/all_labels）

**1.4**  运行make_txt.py文件划分数据集

**1.5**  运行train_val.py文件按照划分好的数据集准备数据

至此数据集制作完毕

*********
**2 使用Yolov5**

**2.1**  配置Yolov5所需环境、第三方库

**2.2**  下载官方权重文件（yolov5s.pt 等）

**2.2**  训练（train.py）

**2.3**  检测（detect.py）


`补充：yolov5原github地址：https://github.com/ultralytics/yolov5`


