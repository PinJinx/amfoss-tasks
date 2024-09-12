# Task 7: A Pirate's Dilemma

## Overview
For this task, there is the `Subtitles.py` script. You can run the program by typing:

```bash
python3 Subtitles.py --path=arg1 --language=arg2 --filesize=arg3 --hash=arg4 --output=arg5 --batch=arg6
```

- **arg** stands for argument; replace it with what you need.
- **arg1, arg2, arg4, arg5** are strings.
- **arg3** is an integer.
- **arg6** is a boolean.

I have added two 10-second video clips that have been renamed into two different movie names in the `Example` folder. When running the app, if the `--path` is not provided, it should default to this path. I have also added an `Output` folder that will be used as the default path to download subtitles.

## Arguments
The command takes in 4 arguments:

- `-p` or `--path`: Specify the path to the file or files.
- `-l` or `--language`: Filter subtitles by language.
- `-f` or `--filesize`: Filter subtitles by file size (in bytes).
- `-h` or `--hash`: Filter subtitles by hash.
- `-o` or `--output`: Specify the output directory for subtitles.
- `-b` or `--batch`: Process subtitles in batch mode. This enables you to read and download subtitles for multiple files as batches.
