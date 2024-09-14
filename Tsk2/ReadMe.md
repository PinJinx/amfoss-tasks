# Terminal Chaos

I had a lot of fun with this task. Here is how I completed it:

## Part 1:
I started by navigating the directory structure using basic commands:

```bash
ls
cd <directory_name>
```

Once inside the `arakis-dex` directory, I needed to find a parchment. To visualize the directory tree, I installed the `tree` command and used it as follows:

```bash
sudo apt-get install tree  # If not already installed
tree
```
This helped me locate the parchment containing the first part of the link. I used `cat` to open the file:

```bash
cat <file_name>
```
The first part of the link was extracted from here.


## Part 2
To get the second part, I switched to the light realm using the `git checkout` command.  
```git checkout The-Light-Realm ```
After this, I used `grep` with `xargs` to find text containing both "holy" and "good" in the content and saved it to a file named `common_files.txt`. (I found this command on Stack Overflow, and with some alterations, it worked for me.)  
```grep -rl "holy" | xargs grep "good" > common_files.txt ```
After opening common_file.txt I got two file names -> MoonBloom and MistVeil
Since there were only two files with that name, I manually completed the remaining three steps to get 'LnnmknnlLhrsdhk'. 
The I Navigated to the BossFight Script using ```tree``` and then I defeated the boss using the above code to get the amulet code.

## Part 3: Unlocking Chests
I switched to Dark realm 1 and Dark realm 2 using,
```git checkout <branch-name> ```
then Armed with the amulet code, I searched for chests in both these branches using the `tree` command:
```bash
tree
```
Once I located the chests, I used the amulet code to unlock them, revealing new codes. Each chest gave me a separate code.

## Part 4
I went ahead and joined the codes from parchment,light book and dark book 1 and dark book 2 to finally get a link encoded by base64
aHR0cHM6Ly9naXRodWIuY29tL2FtYW5zeGNhbGlidXIvVGVybWluYWwtQ2hhb3MtR29kU3VpdGU=
then i used this command in termianl 
```echo "aHR0cHM6Ly9naXRodWIuY29tL2FtYW5zeGNhbGlidXIvVGVybWluYWwtQ2hhb3MtR29kU3VpdGU=" | base64 --decode```
to get the final output
https://github.com/amansxcalibur/Terminal-Chaos-GodSuite
After getting the link I went ahead and cloned the repository.

## Part 5
I went through all the commits of a file Scripture.txt in the GodSuite Repository and found ```aHR0cHM6Ly9naXRodWIuY29tL2FuZ3JlemljaGF0dGVyYm94L1RvLXRoZS1zdGFycy1hbmQtcmVhbG1zLXVuc2Vlbg==``` code hidden within one of the commits.
Next I again used the terminal to decode the base64 using ```echo "aHR0cHM6Ly9naXRodWIuY29tL2FuZ3JlemljaGF0dGVyYm94L1RvLXRoZS1zdGFycy1hbmQtcmVhbG1zLXVuc2Vlbg==" | base64 --decode```
to get the next link ```https://github.com/angrezichatterbox/To-the-stars-and-realms-unseen```

## Part 6
Finally I cloned the repository and ran `victory.py`.
```bash
git clone https://github.com/angrezichatterbox/To-the-stars-and-realms-unseen
python3 victory.py
```
**All programs were run in the terminal, and all the decoding was also done in the terminal.**

