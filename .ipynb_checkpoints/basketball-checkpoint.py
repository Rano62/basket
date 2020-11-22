
import pandas as pd
import numpy as np



all_teams_df = pd.read_csv('srcdata/shot_dist_compiled_data_2019_20.csv')

import plotly.express as px

fig = px.scatter(all_teams_df[all_teams_df.group == 'NOP'], x='min_mid', y='player', size='shots_freq', color='pl_pps')
fig.show()