import os
import shutil

sets = ['train', 'trainval']

wd = os.getcwd()
print(wd)
for image_set in sets:
    if not os.path.exists('all_labels/'):
        os.makedirs('all_labels/')
    image_ids = open('ImageSets/%s.txt' % (image_set)).read().strip().split()
    image_list_file = open('images_%s.txt' % (image_set), 'w')
    labels_list_file = open('labels_%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        image_list_file.write('%s.png\n' % (image_id))
        labels_list_file.write('%s.txt\n' % (image_id))
    image_list_file.close()
    labels_list_file.close()


def copy_file(new_path, path_txt, search_path):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    with open(path_txt, 'r') as lines:
        filenames_to_copy = set(line.rstrip() for line in lines)
    for root, _, filenames in os.walk(search_path):
        for filename in filenames:
            if filename in filenames_to_copy:
                shutil.copy(os.path.join(root, filename), new_path)


# 按照划分好的训练文件的路径搜索目标，并将其复制到yolo格式下的新路径
copy_file('./images/train/', './images_train.txt', './all_images')
copy_file('./images/val/', './images_trainval.txt', './all_images')
copy_file('./labels/train/', './labels_train.txt', './all_labels')
copy_file('./labels/val/', './labels_trainval.txt', './all_labels')
