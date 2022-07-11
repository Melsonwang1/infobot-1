import discord 
import os
import time
from keep_alive import keep_alive


client = discord.Client()
prefix = "pls "
my_secret = os.environ['TOKEN']


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="loona ptt"))
    print('we have logged in as{0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'rob'):
      time.sleep(1)
      await message.channel.send('stop robbing people')
    if message.content.startswith(prefix + 'beg'):
      time.sleep(1)
      await message.channel.send('stop begging')
    if message.content.startswith(prefix +'monthly'):
      time.sleep(1)
      await message.channel.send ('damn bro')
    if message.content.startswith (prefix +'daily'):
      time.sleep(1)
      await message.channel.send('stop doing daily no free money in the world')
    if message.content.startswith(prefix +'bankrob'):
     time.sleep(1)
     await message.channel.send('why you go rob people')
    if message.content.startswith("join heist"):
     await message.channel.send('bruh why you join ')
    if message.content.startswith(prefix + 'roast'):
     await message.channel.send('no you')
    if message.content.startswith(prefix +'bj'):
     await message.channel.send('stop gambling')
    if message.content.startswith(prefix +'rich'):
      await message.channel.send('if you stan loona you will be at the top of the leaderboard')
    if message.content.startswith('wendy'):
      #Below u can change values of title and description
      embed = discord.Embed(title="Wendy",description="Shon Seung-wan (Korean: 손승완; born February 21, 1994), known professionally as Wendy, is a South Korean singer. She is a member of the South Korean girl group Red Velvet. She made her solo debut in 2021 with Like Water.")
      embed.set_image(url="https://2.bp.blogspot.com/-XYsyVk3KDLg/XQa3FEYrKOI/AAAAAAAAD8Q/Rs3Ey4IWJsUy-23BwXBltBqFbiDygjcmwCKgBGAs/w217/wendy-red-velvet-really-bad-boy-uhdpaper.com-4K-23.jpg")
      await message.channel.send(embed=embed)
    
    if message.content.startswith('irene'):
      embed = discord.Embed(title="Irene",description="Bae Joo-hyun (Korean: 배주현; born March 29, 1991), known professionally as Irene, is a South Korean singer, rapper, and actress. She is the leader of the South Korean girl group Red Velvet and a member of its sub-unit Red Velvet - Irene & Seulgi.",url="https://redvelvet.fandom.com/wiki/Irene")
      embed.set_image(url="https://static.wikia.nocookie.net/redvelvet/images/a/ae/Irene_-_Our_Beloved_Boa_4_%28Milky_Way%29_Teaser_Photo.png/revision/latest?cb=20200818163045")
      await message.channel.send(embed=embed)
    if message.content.startswith('seulgi'):
      embed = discord.Embed(title="Seulgi",description="Kang Seul-gi (Korean: 강슬기; born February 10, 1994), known mononymously as Seulgi, is a South Korean singer and dancer. She is a member of South Korean girl group Red Velvet and its sub-unit Red Velvet - Irene & Seulgi.")
      embed.set_image(url="https://3.bp.blogspot.com/-PKJws113DLs/XQsms9aeaRI/AAAAAAAAHbs/kvW_vSGMVFYOy_F5o8_FLjpXJkTl5SkcwCKgBGAs/w0/red-velvet-zimzalabim-seulgi-uhdpaper.com-4K-111.jpg")
      await message.channel.send(embed=embed)
    if message.content.startswith('joy'): 
      embed = discord.Embed(title="Joy",description="Park Soo-young (born September 3, 1996), known by the stage name Joy, is a South Korean singer and actress. She is a member of South Korean girl group Red Velvet, and has had starring roles in the dramas The Liar and His Lover (2017) and Tempted (2018)")
      embed.set_image(url="https://images.wallpapersden.com/image/download/joy-red-velvet-milky-way_bGhobG2UmZqaraWkpJRmbmdlrWZlbWU.jpg")
      await message.channel.send(embed=embed)
    if message.content.startswith('yeri'):
      embed=discord.Embed(title="yeri",description="Kim Ye-rim (Korean: 김예림; born March 5, 1999), known by her stage name Yeri, is a South Korean singer and actress. She is a member of South Korean girl group Red Velvet.")
      embed.set_image(url="https://i.pinimg.com/originals/1f/a4/85/1fa4853fdfe87709cdded5d4ac384ff7.jpg")
      await message.channel.send(embed=embed)
    if message.content.startswith('red velvet'):
      embed=discord.Embed(title="red velvet",description="Red Velvet (Korean: 레드벨벳) is a South Korean girl group formed and managed by SM Entertainment. They originally debuted on August 1, 2014 with the digital single Happiness with the four-member line-up of Irene, Seulgi, Wendy and Joy. The fifth member, Yeri, joined the group in March 2015, following their first major release, Ice Cream Cake. Musically, the work of Red Velvet reflects their own group name: their predominantly-pop red side experiments occasionally with electronic, funk and hip hop, while their velvet side focuses on '90s-influenced R&B with elements of ballad and jazz.")
      embed.set_image(url="https://lh3.googleusercontent.com/-sk_H0RlqJdGdPTaydp8TdAPGD72SZ_HXXml4m921O-T01EhzuQxrtSnCoUi_IkLqyG7QiK7X0T_qlJfzwGt9t83MOtUdiyuoQ=w1200-h630-rj-pp-nu-e365")  
      await message.channel.send(embed=embed)
    if message.content.startswith('heejin'):
      embed=discord.Embed(title="heejin",description="HeeJin is the first single album by South Korean girl group Loona's member HeeJin and the first part of the group's pre-debut project. It was released on October 5, 2016, by Blockberry Creative and distributed by CJ E&M.The album contains two tracks, the single ViViD and its acoustic mix. Music Videos for both songs were released simultaneously on October 5.")
      embed.set_image                            (url="https://static.wikia.nocookie.net/loonatheworld/images/0/0e/1200_Promotional_Picture_HeeJin.png/revision/latest/scale-to-width-down/700?cb=20201001213707")
      await message.channel.send(embed=embed)
    if message.content.startswith('hyunjin'):
      embed=discord.Embed(title="hyunjin",description="HyunJin (Hangul: 현진)[1] is the second revealed member of LOONA and a member of its first sub-unit, LOONA 1/3.She was born as Kim Hyun-Jin (Hangul: 김현진) on November 15, 2000 in Sillim, Gwanak District, Seoul, South Korea.She debuted on October 28, 2016 as a member of LOONA and subsequently released her solo single album HyunJin on November 17, 2016.")
      embed.set_image                              (url="https://static.wikia.nocookie.net/loonatheworld/images/3/3b/1200_Promotional_Picture_HyunJin.png/revision/latest/scale-to-width-down/700?cb=20201001213728")
      await message.channel.send(embed=embed)
    if message.content.startswith('haseul'):
      embed=discord.Embed(title=".haseul",description="HaSeul (Hangul: 하슬) is the third revealed member of LOONA and a member of its first sub-unit, LOONA 1/3.She was born as Cho Ha-Seul (Hangul: 조하슬) on August 18, 1997, in Suncheon, South Jeolla Province, South Korea.She debuted on December 8, 2016 as a member and subsequently released her solo single album HaSeul on December 15, 2016.")
      embed.set_image                               (url="https://static.wikia.nocookie.net/loonatheworld/images/a/af/XX_Promotional_Picture_HaSeul.png/revision/latest/scale-to-width-down/700?cb=20200330200324")
      await message.channel.send(embed=embed)
    if message.content.startswith('yeojin'):
      embed=discord.Embed(title="yeojin",description="YeoJin (Hangul: 여진) is the fourth revealed member of LOONA as well as the maknae (youngest).She was born as Im Yeo-Jin (Hangul: 임여진) on November 11, 2002, in Suseong District, Daegu, South Korea.She debuted on January 4, 2017 as a member and subsequently released her solo single album YeoJin on January 16, 2017.")
      embed.set_image(url="https://static.wikia.nocookie.net/loonatheworld/images/f/f9/%26_Promotional_Picture_YeoJin_1.png/revision/latest?cb=20210603145625")
      await message.channel.send(embed=embed)
    if message.content.startswith("vivi"):
      embed=discord.Embed(title="vivi",description="ViVi (Hangul: 비비) is the fifth revealed member of LOONA and a member of its first sub-unit, LOONA 1/3.She was born as Wong Ka Hei (Cantonese: 黃珈熙)on December 9, 1996 in Tuen Mun District, New Territories, Hong Kong.She debuted on February 14, 2017 as a member and subsequently released her solo single album ViVi on April 17, 2017.")
      embed.set_image(url="https://static.wikia.nocookie.net/loonatheworld/images/a/a3/%26_Promotional_Picture_ViVi_1.png/revision/latest?cb=20210603150417")
      await message.channel.send(embed=embed)
    if message.content.startswith("kim lip"):
      embed=discord.Embed(title="kim lip",description="Kim Lip (Hangul: 김립)is the sixth revealed member of LOONA and a member of the second sub-unit, LOONA / ODD EYE CIRCLE.She was born as Kim Jung-Eun (Hangul: 김정은) on February 10, 1999, in Cheongju, North Chungcheong Province, South Korea.She debuted on May 15, 2017, as a member and subsequently released her solo single album Kim Lip on May 23, 2017.")
      embed.set_image(url="https://static.wikia.nocookie.net/loonatheworld/images/3/37/1200_Promotional_Picture_Kim_Lip.png/revision/latest?cb=20201001213837")
      await message.channel.send(embed=embed)
    if message.content.startswith("jinsoul"):
     embed=discord.Embed(title="jinsoul",description="JinSoul (Hangul: 진솔) is the seventh revealed member of LOONA and a member of its second sub-unit, LOONA / ODD EYE CIRCLE.She was born as Jung Jin-Sol (Hangul: 정진솔) on June 13, 1997 in Dongdaemun District, Seoul, South Korea.She debuted on June 13, 2017 as a member and subsequently released her solo single album JinSoul on June 26, 2017.")
     embed.set_image(url="https://static.wikia.nocookie.net/loonatheworld/images/0/00/XX_Promotional_Picture_JinSoul.png/revision/latest?cb=20200330200657")
     await message.channel.send(embed=embed)
    if message.content.startswith("choerry"):
      embed=discord.Embed(title="choerry",description="Choerry (Hangul: 최리)is the eighth revealed member of LOONA and a member of its second sub-unit, LOONA / ODD EYE CIRCLE.She was born as Choi Ye-Rim (Hangul: 최예림) on June 4, 2001 in Bucheon, South Korea.She debuted on July 12, 2017 as a member and subsequently released her solo single album Choerry on July 28, 2017.")
      embed.set_image(url="https://static.wikia.nocookie.net/loonatheworld/images/1/19/XX_Promotional_Picture_Choerry.png/revision/latest?cb=20200330201200")
      await message.channel.send(embed=embed)
    if message.content.startswith("yves"):
      embed=discord.Embed(title="yves",description="Yves(Hangul: 이브) is the ninth revealed member of LOONA and a member and leader of its third sub-unit, LOONA / yyxy.She was born as Ha Soo-Young (Hangul: 하수영) on May 24, 1997 in Busan, South Korea.She debuted on November 14, 2017 as a member of LOONA and subsequently released her solo single album Yves on November 28, 2017.")
      embed.set_image(url="https://i.pinimg.com/originals/3e/5a/85/3e5a85e4e0741d8137aa5fc00f8fed6a.jpg")
      await message.channel.send(embed=embed)
    if message.content.startswith("chuu"):
     embed=discord.Embed(title="chuu",description='Chuu (Hangul: 츄) is the tenth revealed member of LOONA and a member of its third sub-unit, LOONA / yyxy.She was born as Kim Ji-Woo (Hangul: 김지우) on October 20, 1999 in Chungju, North Chungcheong, South Korea.She debuted on December 14, 2017 as a member and subsequently released her solo single album Chuu on December 28, 2017.')
     embed.set_image(url="https://preview.redd.it/wezy7i0bd8371.jpg?width=1500&format=pjpg&auto=webp&s=dd64f233a9174a2d66ebc75fb77ccaa2aad9159f")
     await message.channel.send(embed=embed)
    if message.content.startswith("gowon"):
     embed=discord.Embed(title='gowon',description='Go Won (Hangul: 고원) is the eleventh revealed member of LOONA and a member of its third sub-unit, LOONA / yyxy.She was born as Park Chae-Won (Hangul: 박채원) on November 19, 2000, in Jung District, Incheon, South Korea.She debuted on January 15, 2018 as a member and subsequently released her solo single album go won on on January 30,2018.')
     embed.set_image(url="https://static.wikia.nocookie.net/loonatheworld/images/3/37/%26_Promotional_Picture_Go_Won.png/revision/latest?cb=20210604150535")
     await message.channel.send(embed=embed)
    if message.content.startswith('olivia hye'):
     embed=discord.Embed(title='olivia hye',description='Olivia Hye (Hangul: 올리비아 혜)is the twelfth and last revealed member of LOONA and a member of its third sub-unit, LOONA / yyxy.She was born as Son Hye-Ju(Hangul: 손혜주) on November 13, 2001 in Uijeongbu, Gyeonggi Province, South Korea.She debuted on March 17, 2018 as a member and subsequently released her solo single album Olivia Hye on March 30, 2018.')
     embed.set_image(url="https://static.wikia.nocookie.net/loonatheworld/images/4/49/Hash_Promotional_Picture_Olivia_Hye.png/revision/latest?cb=20200125032110")
     await message.channel.send(embed=embed)

  

keep_alive()
client.run(os.getenv('TOKEN'))