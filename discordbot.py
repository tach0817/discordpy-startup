import discord
from discord.ext import commands
import os
import traceback
import time

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


#    @bot.event
#    async def on_command_error(ctx, error):
#        orig_error = getattr(error, "original", error)
#        error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#        await ctx.send(error_msg)


@bot.command()
async def fire(ctx):
#    await ctx.send('pong')
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("Fire.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(2)
#    await ctx.send("再生しました。")
    await voice_client.disconnect()


@bot.command()
async def yes(ctx):
#    await ctx.send('pong')
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("Yes.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(2)
#    await ctx.send("再生しました。")
    await voice_client.disconnect()


@bot.command()
async def f1(ctx):
#    await ctx.send('pong')
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("passing1.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(5)
#    await ctx.send("再生しました。")
    await voice_client.disconnect()


@bot.command()
async def f2(ctx):
#    await ctx.send('pong')
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("passing2.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(5)
#    await ctx.send("再生しました。")
    await voice_client.disconnect()


@bot.command()
async def thomas(ctx):
#    await ctx.send('pong')
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("thomas.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(5)
#    await ctx.send("再生しました。")
    await voice_client.disconnect()


@bot.command()
async def yobi(ctx):
#    await ctx.send('pong')
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("yobi.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(8)
#    await ctx.send("再生しました。")
    await voice_client.disconnect()


@bot.command()
async def yodobashi(ctx):
#    await ctx.send('pong')
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("yodobashi.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(8)
#    await ctx.send("再生しました。")
    await voice_client.disconnect()


@bot.command()
async def don(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("donkey.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(6)
    await voice_client.disconnect()


@bot.command()
async def kasasu(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("kasasu.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(5)
    await voice_client.disconnect()


@bot.command()
async def hokuto(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("hokuto.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(13)
    await voice_client.disconnect()


@bot.command()
async def gaia(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("gaia.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(7)
    await voice_client.disconnect()


@bot.command()
async def atu(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("atsumori.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(3)
    await voice_client.disconnect()


@bot.command()
async def syatu(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("syatu.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(16)
    await voice_client.disconnect()


@bot.command()
async def ultra(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("ultrasoul.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(8)
    await voice_client.disconnect()


@bot.command()
async def jojo(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("jojo.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(18)
    await voice_client.disconnect()


@bot.command()
async def suzaku(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("suzaku.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(3)
    await voice_client.disconnect()


@bot.command()
async def daiji(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("daiji.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(17)
    await voice_client.disconnect()


@bot.command()
async def romasaga(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("romasaga.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(8)
    await voice_client.disconnect()


@bot.command()
async def kame(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("kame.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(20)
    await voice_client.disconnect()


@bot.command()
async def potate(ctx):
    voice_client = ctx.message.guild.voice_client
    voice_state = ctx.author.voice
    channel = voice_state.channel
    await channel.connect()
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("potate.mp3")
    voice_client.play(ffmpeg_audio_source)
    time.sleep(6)
    await voice_client.disconnect()

bot.run(token)
