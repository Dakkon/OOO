import abc
from datetime import datetime

class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self,fname):
        self.fname = fname

    def write_line(self, message):
        f = open(self.fname,'w+')
        f.write(message)
        f.close()


class LogFile(WriteFile):

    def write(self,message):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('%s    %s' % (date_str, message))

class DelimFile(WriteFile):

    def __init__(self,filename, delim):
        super(DelimFile,self).__init__(filename)
        self.delim = delim

    def write(self,message):
        line = self.delim.join(message)
        self.write_line(line)



#the parent class to both LogFile and DelimFile, does work that is common between them.   Not intended to be instantiated.

#WriteFile:
	#•	is not designed to be instantiated (constructed)
	#•	is the parent class of both LogFile and DelimFile
	#•	handles tasks that both classes need

log = LogFile('log.txt')                  # passes the filename to write to
mydelim = DelimFile('data.csv', ',')      # passes the filename to write to
                                          # and a delimeter

log.write('this is a log message')        # writes a message to the file
log.write('this is another log message')  # same

mydelim.write(['a', 'b', 'c', 'd'])       # writes a list of values separated
                                          # by comma to the file
mydelim.write(['1', '2', '3', '4'])       # same