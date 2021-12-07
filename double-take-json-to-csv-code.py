import json
import csv

row_list = []

f = open('triarte-scalar-main/double-take.json')
data = json.load(f)
#print(data)

for item in data['objects']:
    URL = (item['URL'])
    Disp_Access_No = (item['Disp_Access_No'])
    Disp_Create_DT = (item['Disp_Create_DT'])
    Disp_Title = (item['Disp_Title'])
    Obj_Title = (item['Obj_Title'])
    Disp_Maker_1 = (item['Disp_Maker_1'])
    Disp_Height = (item['Disp_Height'])
    Disp_Width = (item['Disp_Width'])
    Medium = (item['Medium'])
    Info_Page_Comm = (item['Info_Page_Comm'])
    Dedication = (item['Dedication'])
    Disp_Obj_Type = (item['Disp_Obj_Type'])
    Images = (item['Images'])
    for url in Images:
         ImagePath = url['ImagePath']
         ThumbnailPath = url["ThumbnailPath"]
         
         eachitem = [URL, Disp_Access_No, Disp_Create_DT, Disp_Title,
         Obj_Title, Disp_Maker_1, Disp_Height, Disp_Width, Medium,
         Info_Page_Comm, Dedication, Disp_Obj_Type, ImagePath, ThumbnailPath]
         
         row_list.append(eachitem)

with open('double-take.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list) # I just manually added the headers/metadata fields because I forgot how to do that in python