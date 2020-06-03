'''
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. 
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file 
in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
'''

# We use the tabs for detecting depth. If the depth increases we add to the path, if it decreases we remove from the path.
def longest_path(string):

  array = string.split('\n')
  cur_path = [ array[0] + '/' ]
  cur_path_length = len(cur_path[0])
  longest_path_length = cur_path_length
  prev_tab_count = 0
  
  for item in array[1:]:
    item_list = item.split('\t')
    item_name = item_list[-1]
    cur_tab_count = len(item_list) - 1
    if cur_tab_count > prev_tab_count:
      cur_path, cur_path_length, longest_path_length = update_path(cur_path, cur_path_length, longest_path_length, item_name)
    else:
      for _ in range(prev_tab_count - cur_tab_count + 1):
        item = cur_path.pop()
        cur_path_length -= len(item)
      cur_path, cur_path_length, longest_path_length = update_path(cur_path, cur_path_length, longest_path_length, item_name)
    prev_tab_count = cur_tab_count
  return longest_path_length

def update_path(path, path_length, longest_path_length, item_name):
  if '.' in item_name:
    path.append(item_name)
    path_length += len(item_name)
  else:
    path.append(item_name + '/')
    path_length += len(item_name) + 1
  if path_length > longest_path_length and '.' in item_name:
    longest_path_length = path_length
  return path, path_length, longest_path_length

a = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(longest_path(a))
