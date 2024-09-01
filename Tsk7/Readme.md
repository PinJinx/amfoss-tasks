###Task7: A Pirates Dilemma


##Overview
For this task there is the Subtitles.py script you can run the program by typing,
**arg stands for argument replace it with what you need**
python3 Subtitles.py --path=arg1 --language=arg2 --filesize=arg3 --hash=arg4 --output=arg5 --batch=arg6
**arg 1,2,4,5 are string arg 3 is integer and arg5 is a boolean**
I have added two 10s videoClip that have been renamed into two different movie names in the Example Folder.When running the app if the path is not provided it should default to this path.Likewise i have also added a Output folder that will be used as a default path to download subtitles.


The command takes in 4 argurments namely:
-p or --path =>Specify the path to the file or files.
-l or --language =>Filter subtitles by language.
-f or --filesize =>Filter subtitles by file size.(in bytes)
-h or --hash =>Filter subtitles by hash.
-o or --output =>Specify the output directory for subtitles.
-b or --batch =>Process subtitles in batch mode.This enables you to read and download subtitles for multiple files as batches
