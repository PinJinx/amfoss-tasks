Here’s the corrected version of your markdown file:

# Terminal Chaos

I had a lot of fun with this task. Here is how I completed it:

## Part 1: Initial Exploration
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

## Part 2: Searching for Clues
To get the second part of the link, I switched to the light realm using the `git checkout` command:

```bash
git checkout The-Light-Realm
```

Next, I used `grep` with `xargs` to find text containing both "holy" and "good" and saved the results to a file named `common_files.txt`:

```bash
grep -rl "holy" | xargs grep "good" > common_files.txt
```

After opening `common_files.txt`, I found two file names: *MoonBloom* and *MistVeil*. Since there were only two files, I manually completed the remaining steps to get the string `LnnmknnlLhrsdhk`.

I then navigated to the boss fight script using `tree`:

```bash
tree
```

I defeated the boss using the string above and received the amulet code.

## Part 3: Unlocking Chests
I switched to Dark Realm 1 and Dark Realm 2 using:

```bash
git checkout <branch-name>
```

Armed with the amulet code, I searched for chests in both branches using the `tree` command:

```bash
tree
```

Once I located the chests, I used the amulet code to unlock them, revealing new codes. Each chest provided a separate code.

## Part 4: Combining the Codes
I joined the codes from the parchment, the Light Book, Dark Book 1, and Dark Book 2 to form a Base64-encoded link:

```
aHR0cHM6Ly9naXRodWIuY29tL2FtYW5zeGNhbGlidXIvVGVybWluYWwtQ2hhb3MtR29kU3VpdGU=
```

I then used the following command to decode the link:

```bash
echo "aHR0cHM6Ly9naXRodWIuY29tL2FtYW5zeGNhbGlidXIvVGVybWluYWwtQ2hhb3MtR29kU3VpdGU=" | base64 --decode
```

This gave me the final output:

```
https://github.com/amansxcalibur/Terminal-Chaos-GodSuite
```

After obtaining the link, I cloned the repository.

## Part 5: Hidden Commit Clue
I examined the commits in the GodSuite repository, specifically focusing on a file named `Scripture.txt`. There, I found another Base64-encoded string hidden in one of the commits:

```
aHR0cHM6Ly9naXRodWIuY29tL2FuZ3JlemljaGF0dGVyYm94L1RvLXRoZS1zdGFycy1hbmQtcmVhbG1zLXVuc2Vlbg==
```

I decoded it using:

```bash
echo "aHR0cHM6Ly9naXRodWIuY29tL2FuZ3JlemljaGF0dGVyYm94L1RvLXRoZS1zdGFycy1hbmQtcmVhbG1zLXVuc2Vlbg==" | base64 --decode
```

This led me to the next link:

```
https://github.com/angrezichatterbox/To-the-stars-and-realms-unseen
```

## Part 6: Victory
Finally, I cloned the repository and ran the `victory.py` script:

```bash
git clone https://github.com/angrezichatterbox/To-the-stars-and-realms-unseen
cd To-the-stars-and-realms-unseen
python3 victory.py
```

**All programs were run in the terminal, and all the decoding was done directly in the terminal.**
