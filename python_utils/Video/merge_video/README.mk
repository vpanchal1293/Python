We can merge videos with same quality using ffmpeg

Required tool-
ffmpeg.exe

list1.txt will contain all input video filename with full path as below
file 'G:\\Marriage\\00000.MTS'
file 'G:\\Marriage\\00001.MTS'
file 'G:\\Marriage\\00002.MTS'
file 'G:\\Marriage\\00003.MTS'
file 'G:\\Marriage\\00004.MTS'
file 'G:\\Marriage\\00005.MTS'
file 'G:\\Marriage\\00006.MTS'

Output filename-> video.MTS

Command
ffmpeg.exe -f concat -safe 0 -i "list filename" -c copy "Output filename"
Ex:
ffmpeg.exe -f concat -safe 0 -i "list1.txt" -c copy "video.MTS"
