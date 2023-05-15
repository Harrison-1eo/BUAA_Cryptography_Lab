
message1 =  b'Tod \x08 \x08 \x08ay is a good da \x08 \x08 \x08 \x08y to lear \x08 \x08n \x08 cryptographic h \x08 \x08ash fu \x08 \x08 \x08 \x08 \x08ncti \x08 \x08 \x08on \x08 \x08 \x08 \x08 \x08 \x08'
message2 =  b'To \x08  \x08 \x08 \x08 \x08 \x08 \x08 \x08 \x08 \x08\x08 \x08 \x08 \x08 \x08 \x08  \x08\x08day is a \x08 \x08 good  \x08 \x08 \x08day to learn cryp \x08tograp \x08hic ha \x08 \x08 \x08  \x08 \x08 \x08\x08 \x08 \x08sh functi \x08 \x08 \x08 \x08  \x08 \x08 \x08 \x08\x08on'

message3 =  b'I am attempting L\x08au\x08 second order birthdayL\x08L\x08 aA\x08A\x08t4\x084\x08tack on SHC\x08C\x08A oneJ\x08N\x08'
message4 =  b'I am attempting a second order birthda0\x080\x08y attack on SH*\x08*\x08A one'

message1 = b'To-day is a good day to +learn cryptographic hash function/'
message2 = b'Tod*ay is// a good .//day to learn-, cryptog+*ra++ph//-,-ic+ **h++as--h, func**//t+ion'

message3 = b'I am attempting a second order birthday attack on S,HA one'
message4 = b'I am attempti,,ng .a s**econd order birt..hday *attack on S-+HA one'

message5 = b'It- is evid--ent .that I ha--.ve now success/**/f,ully* f*++ound- -three pairs of messa+,,ges that implement +th--e birthday++ attack on SHA one'
message6 = b'It is evident th**at I ha*ve now successfu+lly-// fou//nd three/ pairs ..o,,f m/essag*es that implement the. birt*/hday attack on SHA one'


message1 = b'My final grade for the cryptography laboratory course is 92.22785262315037'
message2 = b'My final grade for the cryptography laboratory course is 71.88002528899806'

message3 = b'My balance in the Bank of China Industrial and Commercial Bank is 1.325280572445008 * 10 ^ 233814 RMB.'
message4 = b'My balance in the Bank of China Industrial and Commercial Bank is 1.121420144942678 * 10 ^ 840931 RMB.'

message5 = b'I still have many opportunities to find a suitable girlfriend, and have 611107 more girlfriends in the future.'
message6 = b'I still have many opportunities to find a suitable girlfriend, and have 346842 more girlfriends in the future.'


def sha1(msg: bytes) -> bytes:
    import hashlib
    return hashlib.sha1(msg).digest()

msg = [message1, message2, message3, message4, message5, message6]
for m in msg:
    # print(sha1(m).hex())
    print(m.decode('utf-8'))