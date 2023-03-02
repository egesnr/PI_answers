import pandas as pd
import numpy as np
import re 
data = {'Device_Type':['AXO145','TRU151'] ,
        'Stats_Acess_Link': ['<url>https://www.youtube.com</url>','<url>http://www.twitter.com</url>'] }
data_base = pd.DataFrame(data)
data_base

url = data_base.Stats_Acess_Link.str.extract( r'<url>(?:https?://)?([(?i)\w._]+)</url>')
url
