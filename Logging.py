import os, platform, logging
import uuid

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print ('Logging to', logging_file)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s', filename = logging_file, filemode = 'w')
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")


print(platform.system())
print(uuid.uuid4())

f = lambda x:\
    x+1
print(f(1))

plus = lambda x, y : x + y
print(plus(1,2))