import discord
from discord.ext import commands

#в command_prefix указывается префикс который нужно ввести перед командой к примеру help (.help), но если на вашем сервере есть бот который исользует подобный префикс, то лучше поставить другой
client = commands.Bot(command_prefix='.')

#Здесь мы указываем списки фраз на который сможет отвечать бот
hello_Words = ['hello', 'hi', 'привет', 'драсте', 'дратути', 'тевирп', 'ku', 'ку', 'qq', 'здарова', 'салам', 'шалом']
answer_Words = ['узнать информацию о сервере', 'какая инфа', 'какая информация', 'команды', 'команды серевра']
goodbye_Words = ['до связи', 'покеда', 'пока', 'гудбай', 'goodbye', 'прощайте']

@client.event

#эта функция показывает что бот готов к работе
async def on_ready():
	print('Bot ready')

@client.event

#здесь мы пишем ответы бота на ранее заданные фразы
async def on_message(message):
	await client.process_commands(message)
	msg = message.content.lower()
	if msg in hello_Words:
		await message.channel.send('Привет. Чо надо?')
	if msg in answer_Words:
		await message.channel.send('Пропиши в чат команду LG>help , и ты узришь истину')
	if msg in goodbye_Words:
		await message.channel.send('До связи!')

@client.command(pass_contex = True)

#Команда с помощью которой бот будет приветсвовать вас (.hello)
async def hello(ctx):
	author = ctx.message.author

	await ctx.send(f'{author.mention}Helo. I am a Logan!')

#Подключение
TOKEN = open('token.txt', 'r').readline()

client.run(TOKEN)
