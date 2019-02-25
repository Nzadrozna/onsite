# Fundamentals Exercise 1: CLI

Perform the following tasks using the CLI and copy and paste
the commands and results below.

- Navigate to your home directory
- Create a new directory called CodingNomads. We will use this folder
to house materials for the course.
- Move into the CodingNomads folder
- Create new folder cli_testing
- Inside of folder cli_testing,
    a. print the directory path
    b. create 3 new .txt files all with different names (file1.txt,
    file2.txt, file3.txt)
    c. list the contents of the folder
    d. rename one of the files
- Inside of folder cli_testing, create a new folder
- Copy a file from cli_testing to the new folder
- Move a different file from cli_testing to the new folder
- Demonstrate removing:
    a. A file
    b. A folder


## vim

- Use `$ vim` to write some text inside a file
- Use `$ cat` print contents of file
- Use `$ grep` to search for a word inside file


## explore advanced CLI

- What is the difference between the two commands > and >>?
- Create a file hello.txt with the text "how?!", then append the text
    to another file called my_file.txt
- Overwrite the content of my_file.txt with "tell me"


Last login: Wed Feb 20 13:59:59 on ttys000
➜  ~ cd ~
➜  ~ pwd
/Users/nickzadrozna
➜  ~ ls
Desktop           Movies            TheAwsomeTutorial text5
Documents         Music             dir               virtual_test
Downloads         Pictures          pwd
Jagex             Public            test8.sh
Library           PycharmProjects   text4
➜  ~ mkdir CodingNomads1
➜  ~ ls
CodingNomads1     Library           PycharmProjects   text4
Desktop           Movies            TheAwsomeTutorial text5
Documents         Music             dir               virtual_test
Downloads         Pictures          pwd
Jagex             Public            test8.sh
➜  ~ cd CodingNomads1
➜  CodingNomads1 ls -al
total 0
drwxr-xr-x   2 nickzadrozna  staff    64 Feb 21 14:02 .
drwxr-xr-x+ 39 nickzadrozna  staff  1248 Feb 21 14:03 ..
➜  CodingNomads1 mkdir cli_testing
➜  CodingNomads1 cd cli_testing
➜  cli_testing ls
➜  cli_testing touch "hello" >> file1.txt
➜  cli_testing ls
file1.txt hello
➜  cli_testing ls -al
total 0
drwxr-xr-x  4 nickzadrozna  staff  128 Feb 21 14:05 .
drwxr-xr-x  3 nickzadrozna  staff   96 Feb 21 14:04 ..
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:05 file1.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:05 hello
➜  cli_testing rm -rf hello
➜  cli_testing ls -al
total 0
drwxr-xr-x  3 nickzadrozna  staff  96 Feb 21 14:06 .
drwxr-xr-x  3 nickzadrozna  staff  96 Feb 21 14:04 ..
-rw-r--r--  1 nickzadrozna  staff   0 Feb 21 14:05 file1.txt
➜  cli_testing rm -rf file1.txt
➜  cli_testing ls
➜  cli_testing ls- al
zsh: command not found: ls-
➜  cli_testing pwd
/Users/nickzadrozna/CodingNomads1/cli_testing
➜  cli_testing mkdir folder_d
➜  cli_testing ls -al
total 0
drwxr-xr-x  3 nickzadrozna  staff  96 Feb 21 14:07 .
drwxr-xr-x  3 nickzadrozna  staff  96 Feb 21 14:04 ..
drwxr-xr-x  2 nickzadrozna  staff  64 Feb 21 14:07 folder_d
➜  cli_testing cd folder_d
➜  folder_d mk file1.txt
zsh: command not found: mk
➜  folder_d touch file1.txt
➜  folder_d touch file2.txt
➜  folder_d touch file3.txt
➜  folder_d mv file3.txt file4.txt
➜  folder_d ls -al
total 0
drwxr-xr-x  5 nickzadrozna  staff  160 Feb 21 14:13 .
drwxr-xr-x  3 nickzadrozna  staff   96 Feb 21 14:07 ..
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:10 file1.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:11 file2.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:11 file4.txt
➜  folder_d cd..
zsh: command not found: cd..
➜  folder_d cd ..
➜  cli_testing mkdir cli_testing2
➜  cli_testing ls
cli_testing2 folder_d
➜  cli_testing cd ..
➜  CodingNomads1 ls- al
zsh: command not found: ls-
➜  CodingNomads1 ls -al
total 0
drwxr-xr-x   3 nickzadrozna  staff    96 Feb 21 14:04 .
drwxr-xr-x+ 39 nickzadrozna  staff  1248 Feb 21 14:16 ..
drwxr-xr-x   4 nickzadrozna  staff   128 Feb 21 14:15 cli_testing
➜  CodingNomads1 cd cli_testing
➜  cli_testing ls
cli_testing2 folder_d
➜  cli_testing cd folder_d
➜  folder_d ls -al
total 0
drwxr-xr-x  5 nickzadrozna  staff  160 Feb 21 14:13 .
drwxr-xr-x  4 nickzadrozna  staff  128 Feb 21 14:15 ..
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:10 file1.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:11 file2.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:11 file4.txt
➜  folder_d cp file1.txt
usage: cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file target_file
       cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file ... target_directory
➜  folder_d ls -al
total 0
drwxr-xr-x  5 nickzadrozna  staff  160 Feb 21 14:13 .
drwxr-xr-x  4 nickzadrozna  staff  128 Feb 21 14:15 ..
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:10 file1.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:11 file2.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:11 file4.txt
➜  folder_d pwd
/Users/nickzadrozna/CodingNomads1/cli_testing/folder_d
➜  folder_d cd ..
➜  cli_testing ls -al
total 0
drwxr-xr-x  4 nickzadrozna  staff  128 Feb 21 14:15 .
drwxr-xr-x  3 nickzadrozna  staff   96 Feb 21 14:04 ..
drwxr-xr-x  2 nickzadrozna  staff   64 Feb 21 14:15 cli_testing2
drwxr-xr-x  5 nickzadrozna  staff  160 Feb 21 14:13 folder_d
➜  cli_testing cd cli_testing2
➜  cli_testing2 pwd
/Users/nickzadrozna/CodingNomads1/cli_testing/cli_testing2
➜  cli_testing2 cd ..
➜  cli_testing cd folder_d
➜  folder_d cp file1.txt /Users/nickzadrozna/CodingNomads1/cli_testing/cli_testing2
➜  folder_d cd ..
➜  cli_testing cd cli_testing2
➜  cli_testing2 ls -al
total 0
drwxr-xr-x  3 nickzadrozna  staff   96 Feb 21 14:25 .
drwxr-xr-x  4 nickzadrozna  staff  128 Feb 21 14:15 ..
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:25 file1.txt
➜  cli_testing2 cd ..
➜  cli_testing cd ..
➜  CodingNomads1 ls -al
total 0
drwxr-xr-x   3 nickzadrozna  staff    96 Feb 21 14:04 .
drwxr-xr-x+ 39 nickzadrozna  staff  1248 Feb 21 14:25 ..
drwxr-xr-x   4 nickzadrozna  staff   128 Feb 21 14:15 cli_testing
➜  CodingNomads1 cd cli_testing
➜  cli_testing ls -al
total 0
drwxr-xr-x  4 nickzadrozna  staff  128 Feb 21 14:15 .
drwxr-xr-x  3 nickzadrozna  staff   96 Feb 21 14:04 ..
drwxr-xr-x  3 nickzadrozna  staff   96 Feb 21 14:25 cli_testing2
drwxr-xr-x  5 nickzadrozna  staff  160 Feb 21 14:13 folder_d
➜  cli_testing cd folder_d
➜  folder_d ls- al
zsh: command not found: ls-
➜  folder_d ls -al
total 0
drwxr-xr-x  5 nickzadrozna  staff  160 Feb 21 14:13 .
drwxr-xr-x  4 nickzadrozna  staff  128 Feb 21 14:15 ..
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:10 file1.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:11 file2.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:11 file4.txt
➜  folder_d


➜  folder_d vim
➜  folder_d cat test
hey how is it going?

➜  folder_d grep hey
clear
b8ytjt
"
""
^C
➜  folder_d grep "hey" test
hey how is it going?
➜  folder_d


To add text to a file you use >>. To overwrite the data currently in that file, you use >

➜  folder_d mkdir hello.txt
➜  folder_d ls -al
total 8
drwxr-xr-x  7 nickzadrozna  staff  224 Feb 21 14:49 .
drwxr-xr-x  4 nickzadrozna  staff  128 Feb 21 14:15 ..
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:10 file1.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:11 file2.txt
-rw-r--r--  1 nickzadrozna  staff    0 Feb 21 14:11 file4.txt
drwxr-xr-x  2 nickzadrozna  staff   64 Feb 21 14:49 hello.txt
-rw-r--r--  1 nickzadrozna  staff   22 Feb 21 14:35 test
➜  folder_d cd hello.txt
➜  hello.txt echo "how?\!" > hello.txt
➜  hello.txt cat hello.txt
how?!
➜  hello.txt echo "how?\!" > my_file.txt
➜  hello.txt cat my_file.txt
how?!
➜  hello.txt echo "tell me" >> my_file.txt
➜  hello.txt cat my_file.txt
how?!
tell me
➜  hello.txt echo "tell me" > my_file.txt
➜  hello.txt cat my_file.txt
tell me
➜  hello.txt
