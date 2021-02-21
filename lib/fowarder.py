import socket
import re

from lib.packets import varint_pack, varint_unpack
from lib.prints import *
from lib.spy import *

debug = False

def foward(source, destination, direction):
    while 1:
        try:
            buf = b''
            _data = source.recv(1)
            if len(_data) > 0:
                buf += _data
                lenght, _ = varint_unpack(_data)
                _data = source.recv(lenght)
                buf += _data

                if direction: # client to server packet
                    packet_id, data = varint_unpack(_data)
                    packet_id = hex(packet_id)


                    packet_id, data = varint_unpack(_data[1:] if _data.startswith(varint_pack(0)) else _data)
                    packet_id = hex(packet_id)
                    
                    if packet_id == '0x1':
                        try:
                            lenght, message = varint_unpack(data)
                            message = message.decode('utf-8')
                            for regex in regexs:
                                if re.match(regex, message):
                                    print_success('got a match !!! \'%s\'' % message)
                                    break
                            else:
                                print_info('catched a message from client: \'%s\'' % message)
                        except:
                            pass

                destination.send(buf)
        except Exception as e:
            if debug:
                print_error(e)
            break

    source.close()
    destination.close()
    return

