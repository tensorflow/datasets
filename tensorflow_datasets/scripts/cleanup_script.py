import os
#to import the file registered.py
file_path = os.path.join(os.pardir, "core")
sys.path.insert(1, os.path.abspath(1, file_path))
import registered
registered_versions =[]
a = registered.iter_dataset_full_names()
for i in a:
  registered_version.append(i)
