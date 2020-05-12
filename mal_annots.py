import glob
import os
import xml.etree.ElementTree as ET
from PIL import Image



def mal_annots(anns_path,imgs_path):
    for xml_file in glob.glob(anns_path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
	   		temp=[]
            filename=root.find('filename').text
            width=int(root.find('size')[0].text)
            height=int(root.find('size')[1].text)
            temp.append((width,height))

        my_img=imgs_path+filename
        image = Image.open(my_img)
        width1, height1 = image.size
        if width1 or height1 == 0:
        	print(filename)

        for ann in temp:

            if width1 != ann[0]:
                print(filename)
            elif height1 != ann[1]:
                print(filename)           


def main():
    imgs_path = os.path.join(os.getcwd(), 'images')
    anns_path = os.path.join(os.getcwd(), 'annotations')
    mal_annots(imgs_path,anns_path)
    


main()