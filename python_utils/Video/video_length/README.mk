This util will length of video in seconds

tool:
ffprobe.exe

Ex:
ffprobe.exe -i "G:\Marriage\00009.MTS" -show_entries format=duration -v quiet -of csv="p=0"
