from settings import *
from functions import *
import settings

START = f'🙋‍♂ Хуш омадед ба  боти "Xcoin".Ман барои он сохта шудаам, ки ба шумо дар гирифтани пайравони мутақобила ба канали худ кӯмак расонам. Пеш аз оғози истифодаи бот, ҳатман каме хонед [дастур оид ба истифодаи бот ва инчунин қоидаҳо]({LINK_TO_INTRODUCTION_AND_RULES})'

UPDATE = 'Салом боз!'

LITTLE_SUBCOIN_1 = f'❗️❕Барои гирифтани подписчик бояд баланси шумо  {LITTLE_SUBCOIN_TO_GET_SUBS} Xcoin зиёд бошад ❗️❕'

LITTLE_SUBCOIN_2 = '🪫Баланси шумо Кофӣ нест!'

SEND_YOUR_CHANNEL = '❕Барои гирифтани подписчик:\n__1) Ботро дар канал админ монед\n2) @username - и каналро нависед|масалан: @xcoinchannel.__'

def SEND_SUB_COUNT_1(m):
    send_sub_count  = f' 💻 Оли! Акнун чи кадар подписчик мехохед.\n*🔋Дастрас:* {user_balance(m.from_user.id)}'
    return send_sub_count
    
def NEW_REFERAL(argument):
    new_referal = f'💸Табрик шумо дусти худро даъват кардед !\nДустони шумо: {referals(argument)}'
    return new_referal
    
def PROFILE(m):
    profile = f'👤 Ном: {m.from_user.first_name}\n🗄 ID: `{m.from_user.id}`\n💰 Баланс: {user_balance(m.from_user.id)} Xcoin\n📈 Обуна шудаед: {alltime_subs(m.from_user.id)}\n📊 Подписчик гирифтед: {alltime_get_subs(m.from_user.id)}\n⚠️ Ҷарима карда шуд: {fine_count(m.from_user.id)} Xcoin\n👣 Шумораи дустон: {referals(m.from_user.id)}'
    return profile
    
    
GIVE_CHANNEL_LINK = '''❕*Барои оғози гирифтани подписчик:*

1) Ботро ба канал аъзо кунед (Канали шумо бояд ҷамъиятӣ бошад);_
2) _@username-и каналро нависед. Масалан:_ @XCoinChannel'''

CANCEL_TEXT = '🎳 Бекор кардан'

BOT_NOT_IN_CHANNEL = '''❗️❗️❗️Шумо ботро админи канал накардед. Аввал ботро админ кунед❗️❗️❗️\n\n*@username-и каналро нависед!*'''

THIS_IS_NOT_CHANNEL = '''😡 *Ин канал нест!*\n@username-и каналро нависед!'''

THIS_IS_NOT_TEXT = '''⚠️ *Ин username-и канал нест!⚠️*\n\n@username-и каналро нависед!'''

def CONFIRM_ADDING_CHANNEL(username, subcount, price):
    confirm_adding_channel = f'''Тасдиқ кунед:\n\n📻 Канал: @{username}\n\n📲 Шумораи подписчик: {subcount}\n\n💳 Цена: {price} Xcoin'''
    return confirm_adding_channel
    
CHANNEL_ON_PROMOTION = "❗️Ба ин канал подписчик равно кардаед!"

CHANNEL_ON_PROMOTION_2 = '❌ Ба чунин канал аллакай подписчик равон кардед! То ба охир расидани он интизор шавед ва баъд бори дигар кӯшиш кунед.\nБа дигара канал подписчик равон кунед:'

CHANNEL_SUCCESSFULLY_ADED = '👍 Канал успешно добавлен на продвижение.'

SUBSCRIBE_ON_THIS_CHANNEL = '''Ба ин канал аъзо шавед:\n1️⃣ Ба канал гузаред👇, Аъзо шавед ✔️ Боло равед  ва 🔝👁 (5-10 постро) хонед.\n2️⃣ Ба бот баргардед ва xcoin-и худро гиред.'''

NO_HAVE_CHANNELS_FOR_SUBSCRIBE = f"😔 Дар айни хол ягон канал нест!!\n\nШумо метавонед ба канали мо аъзо шавед: {LINK_TO_CHAT_OF_BOT}"

def CHANNEL_WAS_DEL_FROM_CHANNEL(id, link_to_rules):
    message =f'❗️Ба шумо паём.\n\nШумо ботро аз канал баровардед ё аз админ баровадед (id канал: `{id}`)\n😡Ҳамчун ҷарима барои вайрон кардани [қоидаҳо]({link_to_rules}),пешбурди канал қатъ карда шуд ва танҳо нисфи Онҳое, Ки Барои пешбурди Ин Канали Xcoin истифода нашудаанд, ба тавозуни шумо баргардонида шуданд.\n Тафтиши корбар барои сабти ном низ қатъ карда шудааст.'
    return message
    
def SUBSCRIBE_IS_SUCCESSFULLY(username):
    message = f'👍 Шумо ба канал айзо шудед: @{username}\nБа шумо 3-xcoin дода шуд💠.'
    return message
    
def YOU_ARE_LATE_FOR_SUBS(username):
    message = f'☹️ Пеш аз ба охир расидани таблиғи он шумо барои обуна шудан ба канал вақт надоштед.\nШумо метавонед аз ин канал бароед: @{username}'
    return message
    
YOU_DONT_COMPLETE_SUBS = '😡 Шумо ба ин канал аъзо нашудаед'
    
def PARTNER_PROGRAM(username_of_bot, user_id, ref_count):
    message = f'|🔋|- Бо даъват кардани дӯстон ба ин бот тавассути истиноди муроҷиати худ шумо барои ҳар як 5 Xcoin мегиред.\n|📉|- Шумо даъват кардаед: {ref_count}\n|📌|-Ссылкаи шумо барои даъват: https://t.me/{settings.botname}?start={user_id}'
    return message
    
SELECT_ADMIN_MENU_BUTTON = '🛠 Интихоб кунед:'
    
START_COLLECT_STAT = '⏱ Огози чамъовари статистикаи бот...'

def STATISTICS(all, die):
    alive = all - die
    message = f'😅 Общий: {all}\n\n😵 Бекора: {die}\n\n🤠 Активнихо: {alive}'
    return message
   
SEND_MESSAGE_FOR_SEND = '🖋  _текст/фото/видео/gif/файл_ Нависед барои реклама.'

def MAILING_END(all, die):
    alive = all - die
    message = f'✅ Реклама тамом шуд.\n\n🤠 Муваккатан кабул кардан: {alive}\n\n😢 Реклама кабул нашуд: {die}'
    return message
    
SEND_USER_FOR_UBAN = '❓Барои рондан аз бот :\n\n<Id уро нависед> 0- нависед\n\n❓Барои боз даъват кардан:\n\n<Id уро нависта> 1- нависед'

NOT_INTEGER = 'Факат ракам'
        
LITTLE_VALUE = '😡 Бо пробел нависед аз хамдигар !'

YOU_WAS_BANNED = '🥳 Администратор шуморо аз ин бот ронд!.'

YOU_WAS_HACK_ME = '🤭 Шумо админи бот нестед'

SEND_USER_FOR_CHANGE_BALANCE = '''❗️Барои дигар кардани баланс:\n\n 
<id - уро нависед >пробел<Бо ракам ба чанд мехохед дигар кунед>'''

def SUBSCRIPTION_VIOLATION(username,  count_of_fine):
    message = f'😡 Шумо аз канали @{username} баромадед !\n\nҲамчун ҷарима аз тавозуни шумо хориҷ карда шуд{count_of_fine} Xcoin 💠.'
    return message
    
YOU_DID_THIS = '🙂 Шумо ба ин канал аъзо хастед!'

    


