import pandas as pd
import numpy as np

data = {'name'   : ['Janet', 'Nayd', 'Timothy', 'June', 'Amy'], 
        'year'   : [2012   , 2012 , 2013     , 2014  , 2014 ],
        'reports': [6      , 13   , 14       , 1     , 7    ]}

#this sets the names of the index for the dataframe later
index_names = ['Singapore', "Malaysia", 'Thailand', "Japan", 'Norway']

df = pd.DataFrame(data, index=index_names)
df
