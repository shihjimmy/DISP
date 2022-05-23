import cv2
from os import path
import matplotlib.pyplot as plt

video_path = path.join(path.dirname(__file__),'decode.mp4')
video = cv2.VideoCapture(video_path)
FPS = 30

# get frames from video
frames = []
run = True
while run:
    run,frame = video.read()
    if run is False:
        break
    # read the 2d image in grayscale
    frames.append(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY))
#print(len(frames))          # total number of the frames = 61
#print(frames[0].shape)      # size of the 2d image = (1080,1920)
height = frames[0].shape[0]
width = frames[0].shape[1]

# get straight value from each frame
rows = []
for frame in frames:
    r = []
    for row in frame:
        r.append(row[0])
    rows.append(r)
    
# get the difference in each frame
diffs = []
for row in rows:
    diff = []
    for i in range(len(row)-1):
        diff.append(int(row[i+1]) - int(row[i]))
    diff.append(0)
    diffs.append(diff)
    
    
binary = []     # store binary value for every frame
change = []   # change from 1->0 or 0->1
for i in range(len(rows)):
  max_difference = max(diffs[i])
  min_difference = min(diffs[i])
  if max_difference > 10 or min_difference < -10:
    change.append(1)   # there is a change in frame!
    if max_difference + min_difference > 0:
      change_time = diffs[i].index(max_difference)
      binary.append([0]*change_time + [1]*(height-change_time))  # frame is u[n]
    else:
      change_time = diffs[i].index(min_difference)
      binary.append([1]*change_time + [0]*(height-change_time))  # frame is u[-n]
  else:
    change.append(0)
    if sum(rows[i])//height > 140:
      binary.append([1]*height)
    else:
      binary.append([0]*height)
   
# find preamble change 00100 or 000000
pattern_1 = [0,0,1,0,0]      # 1->1 1->1 1->0 0->0 0->0
pattern_2 = [0,0,0,0,0,0]    # 1->1 1->1 1->1 0->0 0->0 0->0
start_position = -1
case = 0
for i in range(len(change)-5):
  if pattern_2 == change[i:i+6]:
    start_position = i+6
    case = 2
    break
if start_position < 0:
  for i in range(len(change)-4):
    if pattern_1 == change[i:i+5]:
      start_position = i+5
      case = 1
      break
#print(start_frame, p)

# get the answer bits
bits = []
if case == 1:
  for i in range(24):
    bits.append(1 - binary[start_position + i][-1])
elif case == 2:
  for i in range(24):
    bits.append(binary[start_position + i][-1])

# turn bits into decimal value
result = 0
for i in bits:
  result <<= 1
  result += i
print('Decode:',result)