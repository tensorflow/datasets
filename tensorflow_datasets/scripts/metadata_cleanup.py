import os
from tensorflow_datasets.core import registered
import re
import shutil

# Get list of all available versions of datasets
registered_versions = sorted([i for i in registered.iter_dataset_full_names()])

meta_dirs = []
for root, dirs, files in os.walk(os.path.join(os.pardir, "testing/metadata")):
    meta_dirs.append(root)

# Get all paths in proper format.

paths = []
for meta_dir in meta_dirs:
    match = re.search(r'\d.\d.\d', meta_dir)
    try:
            meta_dir == match.group()
            paths.append(os.path.relpath(meta_dir, '..\\testing/metadata'))
    except:
        continue


number_of_meta_removed = 0
for i in range(0,len(paths)):
    
    if paths[i] not in registered_versions:
        number_of_meta_removed+=1
        shutil.rmtree(os.path.join(os.pardir, "testing/metadata",paths[i]))

print("*"*80)
print("Total number of registered datasets : ", len(registered_versions))  
print("Total number of subdirectories in metadata direcotry : ", len(paths)) 
print("Total number of meta directories removed : ", len(number_of_meta_removed)) 
print("*"*80)
