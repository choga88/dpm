import os
import sys
import shutil
import commands
from datetime import datetime,timedelta
(exitstatus,outtext)=commands.getstatusoutput('ls -al')
print outtext
