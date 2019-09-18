import os
import time
import collections

folder_path = ''
#folder_path = 'C:\\Users\\pc\\Pictures\\Screenshots\\'

filenames = list(filter(lambda x: x[-4:] == '.png', os.listdir(folder_path)))
filename_with_date = {}
now = time.time()
for filename in filenames:
    filename_with_date[filename] = now - os.path.getmtime(folder_path + filename)

sorted_filenames = sorted(filename_with_date, key=filename_with_date.get, reverse=True)
total_size = len(sorted_filenames)
index = 1
for filename in sorted_filenames:
    os.rename(folder_path + filename, folder_path + '%djalksdjfhiojfalk.png' % index)  # Some random filename in case of ambiguity
    index += 1

filenames = list(filter(lambda x: x[-4:] == '.png', os.listdir(folder_path)))
for filename in filenames:
    index = 1
    while True:
        if filename[index] == 'j':
            break
        index += 1
    os.rename(folder_path + filename, folder_path + '屏幕截图(%s).png' % filename[:index])
