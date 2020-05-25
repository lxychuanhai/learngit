# path_read:读取dicom的文件路径  path_save:保存nii的文件路径
import SimpleITK as sitk
import os
import json
from medpy.io import load, save

def ima2nii(path_read, path_save):
    # GetGDCMSeriesIDs读取序列号相同的dcm文件
    series_id = sitk.ImageSeriesReader.GetGDCMSeriesIDs(path_read)
    # GetGDCMSeriesFileNames读取序列号相同dcm文件的路径，series[0]代表第一个序列号对应的文件
    series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(path_read, series_id[0])
    # print(len(series_file_names))
    # print(series_file_names[0])
    # print(series_file_names[-1])
    series_reader = sitk.ImageSeriesReader()
    series_reader.SetFileNames(series_file_names)
    image3d = series_reader.Execute()
    sitk.WriteImage(image3d, path_save) # , useCompression = True

if __name__ == '__main__':

    # ima2nii('data/1.2.392.200036.9116.2.6.1.37.2417525921.1419322466.14353', 'data/test.nii.gz')
    # ima2nii('data/1.2.392.200036.9116.2.6.1.37.2417525921.1419322466.14353', 'data/test_origin.nii.gz')
    # ima2nii('data/1.2.392.200036.9116.2.6.1.37.2417525921.1419322466.14353', 'data/test_delete_xml.nii.gz')

    # img, img_header = load('data/test.nii.gz')
    # img_origin, img_header_origin = load('data/test_origin.nii.gz')
    # img_delete_xml, img_header_delete_xml = load('data/test_delete_xml.nii.gz')
    #
    # print('对比结束！')

    ima2nii('/home/share/aortic_dissection/CHEN-AICHUN/20130417_ZS0005756786/1.2.392.200036.9116.2.5.1.37.2417546393.1366206226.761676/1.2.392.200036.9116.2.5.1.37.2417546393.1366206441.780849', '/home/share/aortic_dissection/nii_files_total/CHENAICHUN_20130417.nii.gz')
    ima2nii('/home/share/aortic_dissection/CHENBINGJI/CHENBINGJI 20110318', '/home/share/aortic_dissection/nii_files_total/CHENBINGJI_20110318.nii.gz')
    ima2nii('/home/share/aortic_dissection/JIANG-ZHUGEN/20160328_ZS0012496311/1.2.124.113532.10.16.70.8.20160328.100739.6775980/1.2.392.200036.9116.2.6.1.3268.2047398344.1459131796.93317', '/home/share/aortic_dissection/nii_files_total/JIANGZHUGEN_20160328.nii.gz')
    ima2nii('/home/share/aortic_dissection/LI-GUIGEN/20170120_ZS0015092467/1.2.124.113532.10.16.70.8.20170120.10404.7783744/1.2.392.200036.9116.2.5.1.37.2417546393.1484846643.95336', '/home/share/aortic_dissection/nii_files_total/LIGUIGEN_20170120.nii.gz')




# path_resource = "E:/modeled_data/CTA"
# path_dirpaths = os.listdir(path_resource)
#
# for i, path_dirpath in enumerate(path_dirpaths):
#     path_folder = path_resource + '/' + path_dirpath
#     # print(path_folder)
#     path_save = "E:/modeled_data/NII/volume-" + str(i) + ".nii" # ".nii.gz"
#     # print(path_save)
#     ima2nii(path_folder, path_save)

# path_resource = "E:/modeled_data/revised"
# path_dirpaths = os.listdir(path_resource)
#
# for i, path_dirpath in enumerate(path_dirpaths):
#     path_folder = path_resource + '/' + path_dirpath
#     # print(path_folder)
#     os.rename(path_folder, "E:/modeled_data/revised/segmentation-" + str(i) + ".nii.gz")

#
# ## 刘锐打标的92例数据进行nii.gz文件的生成
# path_resource = "/share/aorta"
#
# with open('confirm_patients_index_LR_20200219.json', 'r') as p_dict:
#     p_dict = json.load(p_dict)
#
# for i in range(1,93):
#     print(i)
#     path_dirpath = p_dict[str(i)]
#     path_folder = path_resource + '/' + path_dirpath
#     path_save = "data/TrainingData/volume-" + str(i) + ".nii.gz"  # ".nii.gz"
#     ima2nii(path_folder, path_save)
#
# print('程序结束！')
#




