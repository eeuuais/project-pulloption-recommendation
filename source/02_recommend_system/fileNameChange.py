import os
  
folder_list = os.listdir('./사진')

for folder in folder_list:
    file_list = os.listdir('./사진/' + folder)
    i = 0
    for file in file_list :
        file_oldname = os.path.join('./사진/' + folder, file)
        file_newname_newfile = os.path.join('./사진/' + folder, folder + "pic_" + str(i) + ".jpg")

        os.rename(file_oldname, file_newname_newfile)
        i = i+1
