import mysql.connector as con
myserv = con.connect(host='localhost',user='root',passwd='admin')
cur = myserv.cursor()
cur.execute('create database aashaed')
cur.execute('use aashaed')
cur.execute('create table keymap(keyid int Primary key, keyname varchar(20), keygame int')
cur.execute('insert into keymap values(0,\'Enter\', 13')
cur.execute('insert into keymap values(1,\'1\', 49')
cur.execute('insert into keymap values(2,\'2\', 50')
cur.execute('insert into keymap values(3,\'3\', 51')

easy = ['absence','assist','assume','awful','call','conduct','consume','define','deviate','google','grant','lake','lively','loving','occur','pursue','random','real','require','restore','rigid','roam','social','state','tedious','tribute','wailing']

mid = ['attribute','business','contract','contrast','creativity','demanding','energising','epidemic','evaluate','exaggerate','greatness','identify','illustrate','integrate','negativity','prioritize','regulate','retaliate','rightful','tattered','toxicity','transfer']

diff = ['accomplishment','affectionately','circumference','comprehension','constitutional','demonstrate','encouragement','magnificence','microscopic','personification','questionnaire','representation','simplification','troublesome','truthfulness']

cur.execute('create table easy_word(word varchar(20)')
cur.execute('create table mid_word(word varchar(20)')
cur.execute('create table diff_word(word varchar(20)')

for i in easy:
    cur.execute(f'insert into easy_word values({i})')
for i in mid:
    cur.execute(f'insert into mid_word values({i})')
for i in diff:
    cur.execute(f'insert into diff_word values({i})')

myserv.commit()