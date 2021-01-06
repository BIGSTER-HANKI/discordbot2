import discord
import openpyxl
import random
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("!bs 온라인")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!bs 온라인"):
        await message.channel.send("봇 온라인 완료")

    if message.content.startswith("!bs경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("rudrh.xlsx")
                if sheet["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    await message.channel.send("경고 2회 누적으로 서버에서 추방되었습니다.")

                else:
                    await message.channel.send("경고 1회(2회 누적시 무차별 추방)")
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고 1화")
                break
            i += 1


    if message.content.startswith("!팀나누기"):
        team = message.content[6:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send(person[i] + ">>>" + teamname[i])

    if message.content.startswith("!bs help"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="!bs 온라인", value="봇의 온라인여부를 알수있다.", inline=True)
        embed.add_field(name="!팀나누기 (예시: a a b b/1 1 2 2)", value="팀을 랜덤으로 나눌 수 있다.")
        await message.channel.send(embed=embed)

    if message.content.startswith("!bs sex"):
        await message.channel.send("어허 너 밴")

access_token = os.environ["BOT_TOKEN]
client.run(access_token)

