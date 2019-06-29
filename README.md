# Rosable: Discord Community programming in O5AB1E!

Example server: https://discord.gg/HrSuRB5

This will be up a few days after submission (6/28/19).

## Initiative:

This bot was created on the last day of Discord Hack week out of laziness.

Out of love for the Esoteric programming/code golf language [O5AB1E][1],
I decided to make a fun bot me and my community can enjoy while making use of the compressed nature of O5AB1E.

This was originally going to be a command for my main community bot, [Miss Rosebud][2],
but made it its own thing when I found out about hack week. This is where the name originates. I still plan on adding the
command to Rosy soon as well, along with a microservices-esque api she'll be querying to for processing the code for the 
sake of it.

## Installation:

Main hurdle: O5AB1E. You can follow the instructions on how to install on its page.
Requires the following to function:
- Erlang VM
- Elixir
- [O5AB1E][1] itself
- 'osabie' command installed somewhere in your PATH. you may want to modify the parameters for the 
subprocess.run call in `def osabie` to suit your setup.

Other requirements:

- python 3ish (I used 3.7 to make this)
- discord>=1.0.1

You bot key should replace `bot_key = None` at the top of the script, otherwise it should be in key.cfg as

```
[DEFAULT]
key = asnodufhbnqw9urno4wbfqweo
```

You can run the bot via `python rosable.py`.

## Usage:

This bot has one command, `,,o`. It expects input in the form of 

`,,o ```code text``` optional input`

It will ignore anything between command invocation and the code itself, so you can add comments like

`,,o this or whatever idk ```"P cool imo``` ` 

If input is blank, the message sent before command invocation will be treated as input. One last quirk
is that rosable removes the first character of input if its a space and give by the command itself.
You can bypass this behavior by putting input in the previous message. Have fun.

It also works as an O5AB1E wrapper for python, so you can import `osable(code, data, timeout)` from
it if you want ig.

## Examples:

` ,,o ```"Hello``` `

` ,,o run this after someone says something funny ```=``` `

`,,o ```=``` Or create the input yourself`

`,,o ```áÇ32%ðý``` some text string` [source][3]


[1]: https://github.com/Adriandmen/05AB1E
[2]: https://github.com/eliatlarge/miss_rosebud
[3]: https://codegolf.stackexchange.com/questions/165809/alphabet-position-finder
