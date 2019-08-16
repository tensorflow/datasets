import os
import io
from threading import Thread

import requests
from tensorflow_datasets.core import utils

headers = {}

# TODO limit for download paralleling just for big files use parallel
# TODO find ideal chunk size


#url = ("https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip", "kagglecatsanddogs_3367a.zip")
#url = ('http://download.thinkbroadband.com/5MB.zip', '5mbcim.zip')
# url = ('http://ipv4.download.thinkbroadband.com/100MB.zip', '100mbcim.zip')
# url = ('file:///Users/syny/Downloads/telegram-cloud-document-4-5854705667637511635.mp4','selim.mp4')
url = ('https://storage.googleapis.com/cvdf-datasets/mnist/train-images-idx3-ubyte.gz', 'mnist.gz')
#url = ("http://download.tensorflow.org/example_images/flower_photos.tgz", "flowers.tgz")
# url = ("http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz", "food101.tar.gz")

def split_blocks_to_file(num, div):
  buffer_size = 1024
  part = num // buffer_size  # 9680 ve kalan
  plu = part // div
  marker = 0
  dic = {}

  for i in range(div+1):
    p = [marker, (i+1)*plu*buffer_size]
    marker += plu*buffer_size

    file_name = os.path.join('downloaded', 'file{}'.format(i))
    dic[file_name] = p
  print(dic)
  return dic

#print(split_blocks_to_file(5242880, 5))

def fetch_or_resume2(url, filename, startpoint, stoppoint):
  pos = startpoint
  with open(filename, 'ab') as f:
    if f.tell() > 0:
      pos += f.tell()
    print('start = ', startpoint)
    if pos < stoppoint:
      headers['Range'] = 'bytes={pos}-'.format(pos=pos)
    else:
      return
    response = requests.get(url, headers=headers, stream=True)
    print("start headers = ", headers)
    counter = startpoint
    total_size = int(response.headers.get('content-length'))
    print('total_size = ', total_size)
    with utils.async_tqdm(total=(stoppoint - startpoint) // 1024, unit='KB',) as pbar:
      for data in response.iter_content(chunk_size=1024):
        f.write(data)
        counter += 1024
        pbar.update(n=1024)
        if counter >= stoppoint:
          print('counter&&stoppoint = ', counter, stoppoint)
          break

# working code it's

def join(fromdir, tofile):
  readsize = io.DEFAULT_BUFFER_SIZE
  output = open(tofile, 'wb')
  parts = os.listdir(fromdir)
  parts.sort()
  print('parts', parts)
  for filename in parts:
    filepath = os.path.join(fromdir, filename)
    fileobj = open(filepath, 'rb')
    while 1:
      filebytes = fileobj.read(readsize)
      if not filebytes: break
      output.write(filebytes)
    fileobj.close()
  output.close()



def download():
  print('starting ...')
  response = requests.head(url[0], allow_redirects=True)
  size = int(response.headers.get('content-length', 0))
  # TODO add func to how many parts should be parallel
  print(size)
  th = []
  for fname, points in split_blocks_to_file(size, 5).items():
    #print('points = ', points[0], points[1])
    start_point = points[0]
    finish_points = points[1]
    #print('point starting... ', points)
    #fetch_or_resume2(url[0], fname, start_point, finish_points)
    t = Thread(target=fetch_or_resume2, args=(url[0], fname, start_point, finish_points))
    t.start()
    th.append(t)
    #print('point finished... ', points)
  for i in th:
    i.join()

download()
print('waiting...')
print('now merge files ...')
join('downloaded', url[1])