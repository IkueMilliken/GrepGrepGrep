#Let's check meal reputation by whom and price.
import sys
args = sys.argv
param1 = "curry"
path1 = r"pathname\producNametList.txt"
with open (path1) as f:
    lines = f.readlines()

for line in lines:
  if line.find(param1) >= 0:
    keyword1 = line[13:28]
    print("moji1= " + keyword1)
    path2 = r"pathname\purchaseLog.txt"
    with open (path2) as f2:
      lines = f2.readlines()
      for line in lines:
        if line.find(keyword1) >= 0:
          print("moji2= "+ line)
          
          outputfilepath1 = r"pathname\outLog.txt"
          fileout = open(outputfilepath1, mode ="wt",newline="")
          fileout.write(line) 
