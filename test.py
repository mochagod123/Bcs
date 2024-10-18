import discord
from discord.ext import commands
import os
import sys
import asyncio
import re

intents = discord.Intents().all()
intents.message_content = True

client =commands.Bot(command_prefix='b!', intents=intents)


client.remove_command('help')

@client.command()
async def help(ctx):
    await ctx.send(""">>> ヘルプを表示しています。\n
b!help 今表示してるやつだよ
b!youtube 開発者のYouTubeチャンネル表示
b!intro_bot このBOTの紹介ビデオを表示するよ！
b!server_list 公認サーバーのリストを表示
""")

@client.command()
async def youtube(ctx):
    await ctx.send('>>> 開発者ぶろりーのYouTubeドス！\nhttps://www.youtube.com/channel/UCbp2wAJ1JBYGwXeAQLICAUw?view_as=subscriber%60%60%60')

@client.command()
async def intro_bot(ctx):
    await ctx.send('>>> BROLIYSYSTEMの紹介動画です。\n-まだ無い..許してヒヤシンス-')

@client.command()
async def server_list(ctx):
    await ctx.send('>>> 公認サーバーのリストです。\nhttps://discord.gg/RGwTZzf\nhttps://discord.gg/92eH2U7\nhttps://discord.gg/tQG5GMC')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.channel.send(f"コマンドが正しくありません。\nb!helpを参照してください。")
    else:
        await ctx.channel.send(f"エラーが発生しました。\nエラー内容:{error}")

client.run("Token")