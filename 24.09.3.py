import os

def read_file(filename):
  try:
    with open(filename, 'r') as file:
      content = file.read()
    print(f"Saturs: {content}")
  except FileNotFoundError:
    print(f"Fails '{filename}' neeksistē.")
    
read_file("mans_fails.txt") #FileNotFoundError