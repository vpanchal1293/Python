import os
mypath = r'G:\Learn\Python'

dir_file_in_mypath = os.listdir(mypath)
list_dir_file_info = []
for dir_file in dir_file_in_mypath:
    full_path = os.path.join(mypath,dir_file)
    file_type = 'File' if os.path.isfile(full_path) else 'Dir '
    list_dir_file_info.append([full_path, file_type])

print('Dir and File Presnet in %s'%(mypath))
for name,file_type in list_dir_file_info:
    print(file_type,'->\t',name)
