import  os
import  socket
import  ctypes
import fcntl 
###
# 结构体封装

class ifreq(ctypes.Structure):
    _fields_ = [("ifr_ifrn", ctypes.c_char * 16),
                ("ifr_flags", ctypes.c_short)]
###
# 需要用到的枚举值

class FLAGS(object):
  # linux/if_ether.h
  ETH_P_ALL     = 0x0003 # all protocols
  ETH_P_IP      = 0x0800 # IP only
  # linux/if.h
  IFF_PROMISC   = 0x100
  # linux/sockios.h
  SIOCGIFFLAGS  = 0x8913 # get the active flags
  SIOCSIFFLAGS  = 0x8914 # set the active flags



class PromiscuousSocketManager(object): 
  def __init__(self):
    import fcntl # posix-only
    # htons: converts 16-bit positive integers from host to network byte order
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(FLAGS.ETH_P_ALL))
    ifr = ifreq()
    ifr.ifr_ifrn = b'en0' #写死了，可以通过参数传递进来
    fcntl.ioctl(s, FLAGS.SIOCGIFFLAGS, ifr) # get the flags
    ifr.ifr_flags |= FLAGS.IFF_PROMISC # add the promiscuous flag
    fcntl.ioctl(s, FLAGS.SIOCSIFFLAGS, ifr) # update
    self.ifr = ifr
    self.s = s
  
  def __enter__(self):
    return self.s

  def __exit__(self, *args, **kwargs):
    self.ifr.ifr_flags ^= FLAGS.IFF_PROMISC # mask it off (remove)
    fcntl.ioctl(self.s, FLAGS.SIOCSIFFLAGS, self.ifr) # update

def sniffer(count, bufferSize=65565):

    with PromiscuousSocketManager() as s:
      for i in range(count):
          package = s.recvfrom(bufferSize)
          print(package)


if __name__ == '__main__':
    sniffer(count=10) 