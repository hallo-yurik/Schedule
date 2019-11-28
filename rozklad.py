import telebot
import time
import datetime

bot = telebot.TeleBot('935162754:AAFvxAxL4oi3UUGNE3G4Jqf46ufIg_vIIEo')

#сьогоднішня дата==============================================
now = datetime.datetime.now()

#потрібний формат дати ========================================
this_date = now.strftime("%A,%m,%d,%Y,%H:%M:%S,%W")
this_date = this_date.split(",")

#якщо 0 - чисельник, якщо 1 - знаменник =======================
is_numerator_denominator = int(this_date[5])%2

#понеділок=====================================================
Monday = [
[],
[],
["3 (початок 12:10)\nФізичне виховання\nПрактична"]
]
#вівторок======================================================
Tuesday = [
[["1 (початок 8:30)\nТранспортна логістика\nКобилюх О.Я.\n426в IV н.к.\nЛабораторна"],[""]], 
[["2 (початок 10:20)\nОпераційний менеджмент\nБохонко І.В.\n427(1) IV н.к.\nЛабораторна"], [""]], 
["3 (початок 12:10)\nФінанси підприємства\nЛюльчак З.С.\n417 IV н.к.\nЛекція"]
]
#середа========================================================
Wednesday = [
[["1 (початок 8:30)\nТранспортна логістика\nКобилюх О.Я.\n405 IV н.к.\nЛабораторна"],[""]],
["2 (початок 10:20)\nТехнологія зовнішньоекономічних операцій\nГригор'єв О.Ю.\n527 IV н.к.\nЛекція"],
["3 (початок 12:10)\nСтрахування в логістиці\nТаранський І.П.\n425 IV н.к.\nЛекція"],
["4 (початок 14:15)\nОпераційний менеджмент\nСорочак О.З.\n515 IV н.к.\nЛекція"],
[["5 (початок 16:00)\nОпераційний менеджмент\nГербут М.В.\n420 IV н.к.\nПрактична"],["5 (початок 16:00)\nМіжнародний бізнес\nКалиновський А.О.\n527 IV н.к.\nПрактична"]]
]
#четвер========================================================
Thursday = [
[],
["2 (початок 10:20)\nФінанси підприємства\nРикованова І.С.\n401а IV н.к.\nПрактична"],
["3 (початок 12:10)\nТранспортна логістика\nГринів Н.Т.\n401а IV н.к.\nЛекція"],
["4 (початок 14:15)\nСтрахування в логістиці\nРикованова І.С.\n201 IV н.к.\nПрактична"],
[["5 (початок 16:00)\nТранспортна логістика\nКобилюх О.Я.\n203 I н.к.\nПрактична"],[""]]
]
#п'ятниця======================================================
Friday = [
[[""],["1 (початок 8:30)\nТехнологія зовнішньоекономічних операцій\n528 IV н.к.\nПрактична"]],
["2 (початок 10:20)\nМіжнародний бізнес\nБала Р.Д.\n527 IV н.к.\nЛекція"],
[["3 (початок 12:10)\nТехнологія зовнішньоекономічних операцій\nДруга підгрупа\nДвуліт З.П.\n308 IV н.к.\nЛабораторна"],["3 (початок 12:10)\nТехнологія зовнішньоекономічних операцій\nПерша підгрупа\nДвуліт З.П.\n308 IV н.к.\nЛабораторна"]],
["4 (початок 14:15)\nМіжнародний бізнес\nБала Р.Д.\n212 I н.к.\nПрактична"]
]

Saturday = ""

Sunday = ""
print(this_date)
Week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]

schedule_start = ["8:30", "10:20", "12:10", "14:15", "16:00", "17:40"]
schedule_finish = ["10:05", "11:55", "13:45", "15:50", "17:35", "19:15"]

hours = "----------------------------------------\n\
|       1      |   8:30 - 10:05    |\n\
----------------------------------------\n\
|       2      |  10:20 - 11:55   |\n\
----------------------------------------\n\
|       3      |  12:10 - 13:45   |\n\
----------------------------------------\n\
|       4      |  14:15 - 15:50   |\n\
----------------------------------------\n\
|       5      |  16:00 - 17:35   |\n\
----------------------------------------\n\
|       6      |  17:40 - 19:15   |\n\
----------------------------------------"

def ua_week(day):
	if day == "Monday":
		return "понеділок"
	elif day == "Tuesday":
		return "вівторок"
	elif day == "Wednesday":
		return "середа"
	elif day == "Thursday":
		return "четвер"
	elif day == "Friday":
		return "пятниця"

#приймає this_date[0]==========================================
def into_var(day):
	if day == "Monday":
		return Monday
	elif day == "Tuesday":
		return Tuesday
	elif day == "Wednesday":
		return Wednesday
	elif day == "Thursday":
		return Thursday
	elif day == "Friday":
		return Friday
	elif day == "Saturday":
		return Saturday
	elif day == "Sunday":
		return Sunday

#приймає перемінну-день або into_var(this_date[0])=============
def actual(var_day):
	send = ""
	if var_day == Saturday or var_day == Sunday:
		send += "Вихідний"
	else:
		for lection in var_day:
			if len(lection) == 0:
				continue
			elif len(lection) == 1:
				send += "\n--------------------------------------------------\n" + lection[0]
			else:
				if is_numerator_denominator:
					if len(lection[1][0]):
						send += "\n--------------------------------------------------\n" + lection[1][0]
					else:
						continue
				else:
					if len(lection[0][0]):
						send += "\n--------------------------------------------------\n" + lection[0][0]
					else:
						continue
		send += "\n--------------------------------------------------\n"
	return send
"10:20", "12:10", "14:15", "16:00", "17:40"

#time = now ====================================
def into_index(time):
	if time < time.replace(hour=8, minute=30, second=0, microsecond=0):
		return 0
	elif time < time.replace(hour=10, minute=20, second=0, microsecond=0) and time > time.replace(hour=8, minute=30, second=0, microsecond=0):
		return 1
	elif time < time.replace(hour=12, minute=10, second=0, microsecond=0) and time > time.replace(hour=10, minute=20, second=0, microsecond=0):
		return 2
	elif time < time.replace(hour=14, minute=15, second=0, microsecond=0) and time > time.replace(hour=12, minute=10, second=0, microsecond=0):
		return 3
	elif time < time.replace(hour=16, minute=0, second=0, microsecond=0) and time > time.replace(hour=14, minute=15, second=0, microsecond=0):
		return 4
	elif time < time.replace(hour=17, minute=40, second=0, microsecond=0) and time > time.replace(hour=16, minute=0, second=0, microsecond=0):
		return 5
	else:
		return 6

#num приймає into_index(now)
#var_day приймає into_var(this_date[0])
#when приймає "Сьогодні\n"
def find_next(num, var_day, when):
	pair = num
	for lection in var_day:
		if var_day.index(lection) >= pair:
			if len(lection) == 0:
				pair += 1
			elif len(lection) == 1:
				return "--------------------------------------------------\n" + when + lection[0] +"\n--------------------------------------------------"
			else:
				if is_numerator_denominator:
					if len(lection[1][0]):
						return "--------------------------------------------------\n" + when + lection[1][0] +"\n--------------------------------------------------"
					else:
						pair += 1
				else:
					if len(lection[0][0]):
						return "--------------------------------------------------\n" + when + lection[0][0] +"\n--------------------------------------------------"
					else:
						pair += 1

	if var_day == Sunday:
		return find_next(0, Monday, "Понеділок\n")
	elif Week[Week.index(var_day)+1] == Saturday or Week[Week.index(var_day)+1] == Sunday:
		return find_next(0, Monday, "Понеділок\n")
	else:
		return find_next(0, Week[Week.index(var_day)+1], "Завтра\n")

def tomorrow():
	if this_date[0] == "Sunday":
		return actual(Monday)
	else:
		return actual(Week[Week.index(into_var(this_date[0]))+1])

@bot.message_handler(content_types=['text'])
def handle_text(message):

	if message.text.find(",,,") == 0:

		written = message.text.lower()[3:]

		if written == "сьогодні":
			bot.send_message(message.chat.id, actual(into_var(this_date[0])))

		elif written == "завтра":
			bot.send_message(message.chat.id, tomorrow())

		elif written == "наступна":
			bot.send_message(message.chat.id, find_next(into_index(now), into_var(this_date[0]), "Сьогодні\n"))

		elif written == "години":
			bot.send_message(message.chat.id, hours)

		elif written == "понеділок":
			bot.send_message(message.chat.id, actual(into_var("Monday")))

		elif written == "вівторок":
			bot.send_message(message.chat.id, actual(into_var("Tuesday")))

		elif written == "середа":
			bot.send_message(message.chat.id, actual(into_var("Wednesday")))

		elif written == "четвер":
			bot.send_message(message.chat.id, actual(into_var("Thursday")))

		elif written == "пятниця":
			bot.send_message(message.chat.id, actual(into_var("Friday")))

		elif written == "команди":
			bot.send_message(message.chat.id, '",,,сьогодні" - показає актуальний розклад на сьогодні\n\
",,,завтра" - показає актуальний розклад на завтра\n\
",,,наступна" - (через пробіл) показує інформацію про наступні пару та час до її початку\n\
",,,години" - показує розклад початку та закінчення пар відповідно до їх порядку\n\
",,,понеділок" - показає актуальний розклад на понеділок цього тижня\n\
",,,вівторок" - показає актуальний розклад на вівторок цього тижня\n\
",,,середа" - показає актуальний розклад на середу цього тижня\n\
",,,четвер" - показає актуальний розклад на четвер цього тижня\n\
",,,пятниця" - (без апострофа) показає актуальний розклад на п\'ятницю цього тижня')

		else:
			bot.send_message(message.chat.id, 'Даної команди не існує.\nДля отримання списку команд напишіть ",,,команди". \nПісля ",,," не повинно бути пробілів або інших знаків.')

#@bot.message_handler(content_types=['voice'])
#def handle_audio(message):
	#my_voice = message.voice
	#print(message.voice)
	#print(message)
	#bot.send_voice(message.chat.id, print(message.voice)

bot.polling()