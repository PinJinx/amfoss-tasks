# Terminal Chaos

I had a lot of fun with this task. Here is how I completed it:

## Part 1
First, like the task suggested, I used the `ls` and `cd` commands. This gave me a basic understanding of the terminal.  
Next, to find the parchment, I installed and used the `tree` command inside `arakis-dex`.  
After finding the location, I went there and opened the file to get the first part of the link.

## Part 2
To get the second part, I switched to the light realm using the `git checkout` command.  
After this, I used `grep` with `xargs` to find text containing both "holy" and "good" in the content and saved it to a file named `common_files.txt`. (I found this command on Stack Overflow, and with some alterations, it worked for me.)  
Since there were only two files with that name, I manually completed the remaining three steps to get 'LnnmknnlLhrsdhk'.  
Then, I defeated the boss fight to get the amulet code.

## Part 3
I used the amulet code in each chest in Dark Realm 1 and 2 that I found using the `tree` command to receive the corresponding codes.

## Part 4
I decoded all four codes combined with the command from the provided link to get the god suite repository.

## Part 5
I went through all the commits and used the `voidgate` script to decode the last code hidden within one of the commits to get to the final repository.

## Part 6
I cloned the repository and ran `victory.py`.

**All programs were run in the terminal, and all the decoding was also done in the terminal.**

