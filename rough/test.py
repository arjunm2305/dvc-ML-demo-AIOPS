import os

def main():
  print(">>>>>> ALWAYS RUN >>>>>>")
  with open(os.path.join("rough", "test.txt"), "w") as f:
    f.write("This is the test file")

if __name__ == '__main__':
  main()