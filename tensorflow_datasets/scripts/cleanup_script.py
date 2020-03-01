import os
#to import the file registered.py
file_path = os.path.join(os.pardir, "core")
sys.path.insert(1, os.path.abspath(1, file_path))
import registered
registered_versions =[]
a = registered.iter_dataset_full_names()
for i in a:
  registered_versions.append(i)

meta_dir = os.path.join(os.pardir, "testing/metadata")
meta_dirs = os.listdir(meta_dir)

dirs = []
for i,j,k in os.walk(os.path.join(os.pardir, "testing/metadata")):
    dirs.append(j)
for
dirs_list = dirs.pop(0)
version_list_test = []
for i in range(1, len(dirs)):
    if dirs[i] == [] and dirs[i-1]!= []:
        version_list_test.append(dirs[i-1])
    elif dirs[i] == [] and dirs[i+1] == []:
        pass

#for checking the version with the registered versions we check what it returns then we see the dir 
#     name in list and rmdir
#for i in a:
#   if not i in registed_version:
#     os.rmdir(os.path.join(path, dirs_list[i]))
#
# 

