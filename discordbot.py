from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice

    channel = voice_state.channel

    await channel.connect()

    voice_client = ctx.message.guild.voice_client


    await ctx.message.attachments[0].save("tmp.mp3")

    ffmpeg_audio_source = discord.FFmpegPCMAudio("tmp.mp3")
    voice_client.play(ffmpeg_audio_source)

    await ctx.send("再生しました。")

    await voice_client.disconnect()


bot.run(token)
