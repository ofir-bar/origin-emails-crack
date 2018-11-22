# Origin Emails Cracker

## Abstract
Origin is a company selling video games, similar to Steam. You can browse and purchase different
video games. Popular games include "Battlefield 4", and many more.

## Script Target
The script target is to find real Origin user e-mails and write it to a local DB. </br>

## Assumptions
I assume that inside a big database of users that has Origin,
there will be a percentage of users that will use the same user name as their email. </br>

Example: I have origin account and I purchased "Battlefield 4". my in-game name is "hatzil".
Therefore, I assume it is possible that the user email address will be "hatzil@gmail.com", "hatzil@hotmail.com" or similar.
</br>
Assuming, for example, that "hatzil@gmail.com" really is an Origin-related email address, I also need a way to confirm it.

## How the script works
First, the script needs a database of user profile names.
* The script goes to "bf4stats.com" which is a website hosting user ranking for "Battlefield 4" </br>
Inside the website, there are the in-game names for players playing "Battlefield 4" - a game purchasable only in Origin. </br>
* The script extract only the usernames, and store it to a local text file. The amount of usernames extracted is depend on how much you ask the script to extract. You will be promoted to enter a number, 1 = 49 usernames, 2 = 98 usernames, etc.
* The script reads the creates database of users. It then goes to Origin website and tries to register a new Account.
for each username in the text file, it adds "@gmail.com", "@hotmail.com", etc.

There are 2 states:
If Origin allows to create an account - there is no such username, therefore it is useless.
If Origin says account can't be created because email is already in-use - it is highly probable that this email account belongs to this user, and therefore this email own "Battlefield 4". Therefore the script output that to a local text file.

Example:
Battlefield username: ofir1997

Script will try to register the following email addresses:
ofir1997@gmail.com
ofir1997@hotmail.com
ofir1997@yahoo.com

The script found that ofir1997@hotmail.com is registered in origin, therefore it is written to a local database.



