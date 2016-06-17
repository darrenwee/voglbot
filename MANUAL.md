# VOGLBot Manual

## Conventions
Please try to remember these!!!

### House Names
All references to houses are by **color only**, i.e. `black`, `purple`, `red`, `blue`, `orange`, `green`. This is to ensure zero ambiguity (I can't even remember all the OG names oops). As this bot does not face the freshies, we can bend the rules a little bit.

### Case
**All commands are case-insensitive** so it does not matter how you capitalize **except** for the command word (the one with the slash).

### Freshie Names
We will standardize how we represent freshie names so that we don't accidentally add the same person several times.

**Remember that these are loose guides and you can choose to not follow them as long as you can remember.**

#### Only use first names
We will only add the freshman's first name, ***unless*** there is another freshman with the same first name.

| Real Name                           | Name to Use                                                        |
|-------------------------------------|--------------------------------------------------------------------|
| Tan Jia Hao                         | `Jiahao`                                                           |
| Darren Wee                          | `Darren`                                                           |
| Ryan Paul Augustus Isabella Ken Lim | `Ryan`                                                             |
| Yash Rajesh Nair                    | `Yash`                                                             |
| Abhi Parikh                         | `Abhi`                                                             |
| Nguyen Dinh Viet Anh                | `Anh` (check with the student for which is the correct first name) |

In the event that some freshies have the same first name, you may append their last name.

## Commands
This list is not exhaustive as I haven't finished writing the program but it should provide basic functionality.

### `/help`
***The most important command.***

Usage: `/help`
This brings up the list of commands.

If you need help with a specific command, use `/help command`, e.g. `/help add`.

### `/add`
Usage: `/add house name`

`house` can only be `black`, `purple`, `red`, `blue`, `orange`, `green`. Anything else is rejected.

e.g. `/add black darren`
This adds a freshie called `darren wee` under `black` house.

e.g. `/add orange jiahao`
This adds a freshie called `jiahao tan` under `orange` house.

e.g. `/add green ryan paul augustus isabellerina lim`
This adds a freshie called `ryan paul augustus isabellarina lim` under `green` house.

e.g. `/add nox darren wee`
Command is rejected and no one is added. Do not use OG names.

### `/remove`
Usage: `/remove house name`

Similar to `/add` but does the opposite operation by removing someone instead.

The name and house must be an exact match. Use `/find` or `/enum` to get back the exact name.

e.g. There is a freshie called `john doe` in `green` house.
`/remove green john` will not work, but `/remove green john doe` will.

### `/enum`
Usage: `/enum house`

This gives you a list of everyone in `house` that are `present` or `absent`.

`house` can only be `black`, `purple`, `red`, `blue`, `orange`, `green` and `all`. Anything else is rejected.

e.g. `/enum black`
This gives you a list of all members of `black` who are `present`.

e.g. `/enum red`
This gives you a list of all members of `red` who are `absent`.

e.g. `/enum blue`
This gives you a list of all members of `blue` who are `present` or `absent`.

e.g. `/enum all`
This gives you a list of every freshie registered in VOGLBot. Try not to do this as the message can get very long and flood your phone.

The list is sorted by name.

### `/find`
Usage: `/find house searchpattern`

`house` can only be `black`, `purple`, `red`, `blue`, `orange`, `green` and `all`. Anything else is rejected.

This is like Google search for freshie names, where it looks for any name that contains `searchpattern`.
It will return freshies and their details such as house and present attendance.
This is for enabling you to check if someone has already been added.

e.g. `/find black and`
This returns a list of people in `black` house with `and` inside their name, e.g. you will get back `Andrea`, `Andy`, Anderson`, etc if they are in `black` house.

e.g. `/find black darren wee`
This returns a list of people in `black` house with `darren wee` inside the name (probably only 1 person called `darren wee`).

### `/vfind`
Usage is the same as `/find` but returns more details of the freshie, e.g. diet and medical info, who added this freshie.

### `/in` and `/out`
Usage: `/in house name` or `/out house name`

This changes the `status` of a freshie between `present` and `absent`. The commands should be self explanatory.

## If Something Breaks
If any commands or the bot misbehaves, e.g. it doesn't do what you want it to do, please note down:
1. what command you tried to give
2. what you wanted to do
3. what the bot actually did
4. the time that you tried to do this command (use the Telegram timestamp) so I can look at my log files.

**If the bot doesn't respond to any commands like `/help`, it might have crashed. Text me so I can reboot it.**

# Thanks everyone!
