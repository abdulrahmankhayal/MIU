import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        list1=[]
        for member in root.findall('object'):
            filename=root.find('filename').text
            width=int(root.find('size')[0].text)
            height=int(root.find('size')[1].text)
            my_class=member[0].text
            list1.append([filename,width,height,my_class])
        list2=[]
        for member in root.findall('.//bndbox'):
            xmin = int(member.find('xmin').text)
            ymin = int(member.find('ymin').text)
            xmax = int(member.find('xmax').text)
            ymax = int(member.find('ymax').text)
            list2.append([xmin,ymin,xmax,ymax])
        for i in range(len(list1)):
            templist=list1[i]+list2[i]    
            templist=tuple(templist)
            xml_list.append(templist)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    train_path = os.path.join(os.getcwd(), 'train/label')
    xml_df = xml_to_csv(train_path)
    xml_df.to_csv('train_labels.csv', index=None)
    print('Successfully converted xml to csv.')
    test_path = os.path.join(os.getcwd(), 'test/label')
    xml_df = xml_to_csv(test_path)
    xml_df.to_csv('test_labels.csv', index=None)
    print('Successfully converted xml to csv.')



main()
