from datetime import datetime
import time
now=datetime.now()
now3=time.time()
#time.sleep(1)
now2=datetime.now()
now4=time.time()
print(now2-now)
if(now4-now3>1):
    print(now4-now3)