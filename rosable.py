#!/usr/bin/python3
from discord.ext.commands import Bot
import os
import subprocess
from asyncio import get_running_loop as get_loop
from tempfile import NamedTemporaryFile as tempf
from configparser import ConfigParser as cfg

bot_key = None  # TODO REPLACE ME

rosy = Bot(",,")

default_timeout = 10


@rosy.command()
async def o(ctx):
    channel = ctx.channel
    try:
        _, code, data = ctx.message.content.split("```", maxsplit=2)
    except ValueError as e:
        return await channel.send(
            "usage: ,,o \```[o5ab1e code]``` {input}\n\nEmpty input uses the previous message as input."
        )

    if not data:
        try:
            data = [m.content async for m in channel.history(limit=2)][1]
        except IndexError:
            pass
    elif data[0] == " ":
        data = data[1:]

    print(
        f"Running in ({channel.guild}){channel.name}:\n"
        f"{code}\n" + f"+++++ With input: +++++\n{data}\n\n"
        if data
        else "\n\n"
    )

    result = get_loop().run_in_executor(None, osable, code, data, default_timeout)
    result_message = await channel.send("...")

    try:
        await result_message.edit(content=(await result))
    except TimeoutError:
        await result_message.edit(content="Program timed out.")
    except subprocess.CalledProcessError as e:
        await result_message.edit(content=f"Error running:\n\n{e}")
    # await ctx.channel.send(f"code: {code}, input: {data}")


@rosy.event
async def on_ready():
    print(f"Logged in as {rosy.user.name}\n==============")


codepath = os.getcwd()
# compiles osabie
def osable(code, data="", timeout=10):
    with tempf("w+", dir=codepath, suffix=".abe") as codef, tempf(
        "w+", dir=codepath, suffix=".txt"
    ) as inpf:
        codef.write(code)
        inpf.write(data)
        codef.flush()
        inpf.flush()
        # If it fails, bubbles up TimeoutError + CalledProcessError
        codef.seek(0)
        output = subprocess.run(
            f'osabie "{codef.name}" < "{inpf.name}"',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            shell=True,
            encoding="UTF-8",
        )
    return output.stdout


if __name__ == "__main__":
    if not bot_key:
        cf = cfg()
        cf.read("key.cfg")
        bot_key = cf["DEFAULT"]["key"]
    try:
        rosy.run(bot_key)
    except KeyboardInterrupt:
        print("Received exit, exiting")
