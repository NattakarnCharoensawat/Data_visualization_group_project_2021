import pandas as pd   
import plotly          
import plotly.express as px
import dash            
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
from jupyter_dash import JupyterDash
import plotly.graph_objs as go
import numpy as np
import datetime
import calendar
import altair as alt 
from vega_datasets import data


#GRAPH 1
#import csv file 
#monthly
df_graph1_monthly = pd.read_csv('overall_df_graph1_2.csv')
df_graph1_monthly = df_graph1_monthly.drop(columns =['Unnamed: 0'])
df_graph1_monthly['fan_by_platform'] = df_graph1_monthly.groupby(['platform','month'])['fan'].transform('sum') 
df_graph1_monthly['Total_fan'] = df_graph1_monthly.groupby(['month'])['fan'].transform('sum')
df_graph1_monthly['Pct_fan'] = (df_graph1_monthly['fan_by_platform']/df_graph1_monthly['Total_fan'] )*100
df_graph1_monthly = df_graph1_monthly.sort_values(["month"])
df_graph1_monthly['month'] = df_graph1_monthly['month'].apply(lambda x: calendar.month_name[x])

#import csv file 
#daily
df_graph1_daily= pd.read_csv('overall_df_breakdown_graph1_2.csv')
df_graph1_daily = df_graph1_daily.drop(columns =['Unnamed: 0'])
df_graph1_daily['fan_by_platform_date'] = df_graph1_daily.groupby(['platform','created_date'])['fan'].transform('sum') 
df_graph1_daily['Total_fan_date'] = df_graph1_daily.groupby(['created_date'])['fan'].transform('sum')
df_graph1_daily['Pct_fan_date'] = (df_graph1_daily['fan_by_platform_date']/df_graph1_daily['Total_fan_date'] )*100
df_graph1_daily = df_graph1_daily.sort_values(["created_date"])
df_graph1_daily['month'] = df_graph1_daily['month'].apply(lambda x: calendar.month_name[x])
df_graph1_daily['created_date'] = pd.to_datetime(df_graph1_daily['created_date'])




#export csv file
df_graph1_monthly.to_csv('df_graph1_monthly.csv',index = False)
df_graph1_daily.to_csv('df_graph1_daily.csv',index = False)


#GRAPH 2 

#import csv file 
#monthly
overall_df_graph2 = pd.read_csv('overall_df_graph1_2.csv')
overall_df_graph2 = overall_df_graph2.drop(columns =['Unnamed: 0'])
#filter Facebook
filter_graph2_FB = overall_df_graph2['platform'] == 'Facebook'
overall_df_graph2_FB = overall_df_graph2.loc[filter_graph2_FB]
#filter Facebook tier beginner
filter_graph2_FB_begin = overall_df_graph2_FB['influencer_tier'] == 'Beginner'
overall_df_graph2_FB_begin = overall_df_graph2_FB.loc[filter_graph2_FB_begin]
overall_df_graph2_FB_begin = overall_df_graph2_FB_begin.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_FB_begin = overall_df_graph2_FB_begin.groupby('month').head(10)
overall_df_graph2_FB_begin['reactions_per_fan_by_account'] = overall_df_graph2_FB_begin.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Facebook tier nano
filter_graph2_FB_nano = overall_df_graph2_FB['influencer_tier'] == 'Nano'
overall_df_graph2_FB_nano = overall_df_graph2_FB.loc[filter_graph2_FB_nano]
overall_df_graph2_FB_nano = overall_df_graph2_FB_nano.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_FB_nano = overall_df_graph2_FB_nano.groupby('month').head(10)
overall_df_graph2_FB_nano['reactions_per_fan_by_account'] = overall_df_graph2_FB_nano.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Facebook tier micro
filter_graph2_FB_Micro = overall_df_graph2_FB['influencer_tier'] == 'Micro'
overall_df_graph2_FB_micro = overall_df_graph2_FB.loc[filter_graph2_FB_Micro]
overall_df_graph2_FB_micro = overall_df_graph2_FB_micro.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_FB_micro = overall_df_graph2_FB_micro.groupby('month').head(10)
overall_df_graph2_FB_micro['reactions_per_fan_by_account'] = overall_df_graph2_FB_micro.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Facebook tier mid
filter_graph2_FB_Mid = overall_df_graph2_FB['influencer_tier'] == 'Mid-tier'
overall_df_graph2_FB_mid = overall_df_graph2_FB.loc[filter_graph2_FB_Mid]
overall_df_graph2_FB_mid = overall_df_graph2_FB_mid.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_FB_mid = overall_df_graph2_FB_mid.groupby('month').head(10)
overall_df_graph2_FB_mid['reactions_per_fan_by_account'] = overall_df_graph2_FB_mid.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Facebook tier macro
filter_graph2_FB_macro = overall_df_graph2_FB['influencer_tier'] == 'Macro'
overall_df_graph2_FB_macro = overall_df_graph2_FB.loc[filter_graph2_FB_macro]
overall_df_graph2_FB_macro = overall_df_graph2_FB_macro.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_FB_macro = overall_df_graph2_FB_macro.groupby('month').head(10)
overall_df_graph2_FB_macro['reactions_per_fan_by_account'] = overall_df_graph2_FB_macro.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Facebook tier mega
filter_graph2_FB_mega = overall_df_graph2_FB['influencer_tier'] == 'Mega'
overall_df_graph2_FB_mega = overall_df_graph2_FB.loc[filter_graph2_FB_mega]
overall_df_graph2_FB_mega = overall_df_graph2_FB_mega.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_FB_mega = overall_df_graph2_FB_mega.groupby('month').head(10)
overall_df_graph2_FB_mega['reactions_per_fan_by_account'] = overall_df_graph2_FB_mega.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
df_graph2_FB = pd.concat([overall_df_graph2_FB_begin,overall_df_graph2_FB_nano,overall_df_graph2_FB_micro,overall_df_graph2_FB_mid,overall_df_graph2_FB_macro,overall_df_graph2_FB_mega])
#filter Twitter
filter_graph2_TW = overall_df_graph2['platform'] == 'Twitter'
overall_df_graph2_TW = overall_df_graph2.loc[filter_graph2_TW]
#filter Twitter tier beginner
filter_graph2_TW_begin = overall_df_graph2_TW['influencer_tier'] == 'Beginner'
overall_df_graph2_TW_begin = overall_df_graph2_TW.loc[filter_graph2_TW_begin]
overall_df_graph2_TW_begin = overall_df_graph2_TW_begin.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_TW_begin = overall_df_graph2_TW_begin.groupby('month').head(10)
overall_df_graph2_TW_begin['reactions_per_fan_by_account'] = overall_df_graph2_TW_begin.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Twitter tier Nano
filter_graph2_TW_nano = overall_df_graph2_TW['influencer_tier'] == 'Nano'
overall_df_graph2_TW_nano = overall_df_graph2_TW.loc[filter_graph2_TW_nano]
overall_df_graph2_TW_nano = overall_df_graph2_TW_nano.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_TW_nano = overall_df_graph2_TW_nano.groupby('month').head(10)
overall_df_graph2_TW_nano['reactions_per_fan_by_account'] = overall_df_graph2_TW_nano.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Twitter tier Micro
filter_graph2_TW_Micro = overall_df_graph2_TW['influencer_tier'] == 'Micro'
overall_df_graph2_TW_micro = overall_df_graph2_TW.loc[filter_graph2_TW_Micro]
overall_df_graph2_TW_micro = overall_df_graph2_TW_micro.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_TW_micro = overall_df_graph2_TW_micro.groupby('month').head(10)
overall_df_graph2_TW_micro['reactions_per_fan_by_account'] = overall_df_graph2_TW_micro.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Twitter tier Mid
filter_graph2_TW_Mid = overall_df_graph2_TW['influencer_tier'] == 'Mid-tier'
overall_df_graph2_TW_mid = overall_df_graph2_TW.loc[filter_graph2_TW_Mid]
overall_df_graph2_TW_mid = overall_df_graph2_TW_mid.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_TW_mid = overall_df_graph2_TW_mid.groupby('month').head(10)
overall_df_graph2_TW_mid['reactions_per_fan_by_account'] = overall_df_graph2_TW_mid.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Twitter tier Macro
filter_graph2_TW_macro = overall_df_graph2_TW['influencer_tier'] == 'Macro'
overall_df_graph2_TW_macro = overall_df_graph2_TW.loc[filter_graph2_TW_macro]
overall_df_graph2_TW_macro = overall_df_graph2_TW_macro.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_TW_macro = overall_df_graph2_TW_macro.groupby('month').head(10)
overall_df_graph2_TW_macro['reactions_per_fan_by_account'] = overall_df_graph2_TW_macro.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Twitter tier Mega
filter_graph2_TW_mega = overall_df_graph2_TW['influencer_tier'] == 'Mega'
overall_df_graph2_TW_mega = overall_df_graph2_TW.loc[filter_graph2_TW_mega]
overall_df_graph2_TW_mega = overall_df_graph2_TW_mega.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_TW_mega = overall_df_graph2_TW_mega.groupby('month').head(10)
overall_df_graph2_TW_mega['reactions_per_fan_by_account'] = overall_df_graph2_TW_mega.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
df_graph2_TW = pd.concat([overall_df_graph2_TW_begin,overall_df_graph2_TW_nano,overall_df_graph2_TW_micro,overall_df_graph2_TW_mid,overall_df_graph2_TW_macro,overall_df_graph2_TW_mega])
#filter Instagram
filter_graph2_IG = overall_df_graph2['platform'] == 'Instagram'
overall_df_graph2_IG = overall_df_graph2.loc[filter_graph2_IG]
#filter Instagram tier Beginner
filter_graph2_IG_begin = overall_df_graph2_IG['influencer_tier'] == 'Beginner'
overall_df_graph2_IG_begin = overall_df_graph2_IG.loc[filter_graph2_IG_begin]
overall_df_graph2_IG_begin = overall_df_graph2_IG_begin.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_IG_begin = overall_df_graph2_IG_begin.groupby('month').head(10)
overall_df_graph2_IG_begin['reactions_per_fan_by_account'] = overall_df_graph2_IG_begin.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Instagram tier Nano
filter_graph2_IG_nano = overall_df_graph2_IG['influencer_tier'] == 'Nano'
overall_df_graph2_IG_nano = overall_df_graph2_IG.loc[filter_graph2_IG_nano]
overall_df_graph2_IG_nano = overall_df_graph2_IG_nano.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_IG_nano = overall_df_graph2_IG_nano.groupby('month').head(10)
overall_df_graph2_IG_nano['reactions_per_fan_by_account'] = overall_df_graph2_IG_nano.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Instagram tier Micro
filter_graph2_IG_Micro = overall_df_graph2_IG['influencer_tier'] == 'Micro'
overall_df_graph2_IG_micro = overall_df_graph2_IG.loc[filter_graph2_IG_Micro]
overall_df_graph2_IG_micro = overall_df_graph2_IG_micro.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_IG_micro = overall_df_graph2_IG_micro.groupby('month').head(10)
overall_df_graph2_IG_micro['reactions_per_fan_by_account'] = overall_df_graph2_IG_micro.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Instagram tier Mid
filter_graph2_IG_Mid = overall_df_graph2_IG['influencer_tier'] == 'Mid-tier'
overall_df_graph2_IG_mid = overall_df_graph2_IG.loc[filter_graph2_IG_Mid]
overall_df_graph2_IG_mid = overall_df_graph2_IG_mid.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_IG_mid = overall_df_graph2_IG_mid.groupby('month').head(10)
overall_df_graph2_IG_mid['reactions_per_fan_by_account'] = overall_df_graph2_IG_mid.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Instagram tier Macro
filter_graph2_IG_macro = overall_df_graph2_IG['influencer_tier'] == 'Macro'
overall_df_graph2_IG_macro = overall_df_graph2_IG.loc[filter_graph2_IG_macro]
overall_df_graph2_IG_macro = overall_df_graph2_IG_macro.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_IG_macro = overall_df_graph2_IG_macro.groupby('month').head(10)
overall_df_graph2_IG_macro['reactions_per_fan_by_account'] = overall_df_graph2_IG_macro.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Instagram tier Mega
filter_graph2_IG_mega = overall_df_graph2_IG['influencer_tier'] == 'Mega'
overall_df_graph2_IG_mega = overall_df_graph2_IG.loc[filter_graph2_IG_mega]
overall_df_graph2_IG_mega = overall_df_graph2_IG_mega.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_IG_mega = overall_df_graph2_IG_mega.groupby('month').head(10)
overall_df_graph2_IG_mega['reactions_per_fan_by_account'] = overall_df_graph2_IG_mega.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
df_graph2_IG = pd.concat([overall_df_graph2_IG_begin,overall_df_graph2_IG_nano,overall_df_graph2_IG_micro,overall_df_graph2_IG_mid,overall_df_graph2_IG_macro,overall_df_graph2_IG_mega])
#filter Youtube
filter_graph2_YT = overall_df_graph2['platform'] == 'Youtube'
overall_df_graph2_YT = overall_df_graph2.loc[filter_graph2_YT]
#filter Youtube tier Beginner
filter_graph2_YT_begin = overall_df_graph2_YT['influencer_tier'] == 'Beginner'
overall_df_graph2_YT_begin = overall_df_graph2_YT.loc[filter_graph2_YT_begin]
overall_df_graph2_YT_begin = overall_df_graph2_YT_begin.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_YT_begin = overall_df_graph2_YT_begin.groupby('month').head(10)
overall_df_graph2_YT_begin['reactions_per_fan_by_account'] = overall_df_graph2_YT_begin.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Youtube tier Nano
filter_graph2_YT_nano = overall_df_graph2_YT['influencer_tier'] == 'Nano'
overall_df_graph2_YT_nano = overall_df_graph2_YT.loc[filter_graph2_YT_nano]
overall_df_graph2_YT_nano = overall_df_graph2_YT_nano.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_YT_nano = overall_df_graph2_YT_nano.groupby('month').head(10)
overall_df_graph2_YT_nano['reactions_per_fan_by_account'] = overall_df_graph2_YT_nano.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Youtube tier Micro
filter_graph2_YT_Micro = overall_df_graph2_YT['influencer_tier'] == 'Micro'
overall_df_graph2_YT_micro = overall_df_graph2_YT.loc[filter_graph2_YT_Micro]
overall_df_graph2_YT_micro = overall_df_graph2_YT_micro.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_YT_micro = overall_df_graph2_YT_micro.groupby('month').head(10)
overall_df_graph2_YT_micro['reactions_per_fan_by_account'] = overall_df_graph2_YT_micro.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Youtube tier Mid
filter_graph2_YT_Mid = overall_df_graph2_YT['influencer_tier'] == 'Mid-tier'
overall_df_graph2_YT_mid = overall_df_graph2_YT.loc[filter_graph2_YT_Mid]
overall_df_graph2_YT_mid = overall_df_graph2_YT_mid.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_YT_mid = overall_df_graph2_YT_mid.groupby('month').head(10)
overall_df_graph2_YT_mid['reactions_per_fan_by_account'] = overall_df_graph2_YT_mid.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Youtube tier Macro
filter_graph2_YT_macro = overall_df_graph2_YT['influencer_tier'] == 'Macro'
overall_df_graph2_YT_macro = overall_df_graph2_YT.loc[filter_graph2_YT_macro]
overall_df_graph2_YT_macro = overall_df_graph2_YT_macro.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_YT_macro = overall_df_graph2_YT_macro.groupby('month').head(10)
overall_df_graph2_YT_macro['reactions_per_fan_by_account'] = overall_df_graph2_YT_macro.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
#filter Youtube tier Mega
filter_graph2_YT_mega = overall_df_graph2_YT['influencer_tier'] == 'Mega'
overall_df_graph2_YT_mega = overall_df_graph2_YT.loc[filter_graph2_YT_mega]
overall_df_graph2_YT_mega = overall_df_graph2_YT_mega.groupby(["month"]).apply(lambda x: x.sort_values(["reactions_per_fan"], ascending = False)).reset_index(drop=True)
overall_df_graph2_YT_mega = overall_df_graph2_YT_mega.groupby('month').head(10)
overall_df_graph2_YT_mega['reactions_per_fan_by_account'] = overall_df_graph2_YT_mega.groupby(['account_id','month'])['reactions_per_fan'].transform('sum')
df_graph2_YT = pd.concat([overall_df_graph2_YT_begin,overall_df_graph2_YT_nano,overall_df_graph2_YT_micro,overall_df_graph2_YT_mid,overall_df_graph2_YT_macro,overall_df_graph2_YT_mega])

#----concat graph----#
df_graph2 = pd.concat([df_graph2_FB,df_graph2_TW,df_graph2_IG,df_graph2_YT])
df_graph2['no_of_platforms'] = df_graph2['no_of_platforms'].astype(str)
df_graph2 = df_graph2.sort_values(["month"])
df_graph2['month'] = df_graph2['month'].apply(lambda x: calendar.month_name[x])
#export csv file
df_graph2.to_csv('df_graph2.csv',index = False)


#import csv file 
#year
df_graph2_year = pd.read_csv('overall_df_graph2_by_year.csv')
df_graph2_year = df_graph2_year.drop(columns =['Unnamed: 0'])
#filter facebook and tier
filter_FB = df_graph2_year['platform'] == 'Facebook'
df_graph2_year_FB = df_graph2_year.loc[filter_FB]
filtter_year_FB_begin = df_graph2_year_FB['influencer_tier'] == 'Beginner'
df_graph2_year_FB_begin = df_graph2_year_FB.loc[filtter_year_FB_begin]
df_graph2_year_FB_begin = df_graph2_year_FB_begin.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_FB_begin['reactions_per_fan_by_account'] = df_graph2_year_FB_begin.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_FB_begin =df_graph2_year_FB_begin.head(10)

filtter_year_FB_nano = df_graph2_year_FB['influencer_tier'] == 'Nano'
df_graph2_year_FB_nano = df_graph2_year_FB.loc[filtter_year_FB_nano]
df_graph2_year_FB_nano = df_graph2_year_FB_nano.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_FB_nano['reactions_per_fan_by_account'] = df_graph2_year_FB_nano.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_FB_nano =df_graph2_year_FB_nano.head(10)

filtter_year_FB_Micro  = df_graph2_year_FB['influencer_tier'] == 'Micro'
df_graph2_year_FB_micro = df_graph2_year_FB.loc[filtter_year_FB_Micro]
df_graph2_year_FB_micro = df_graph2_year_FB_micro.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_FB_micro['reactions_per_fan_by_account'] = df_graph2_year_FB_micro.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_FB_micro =df_graph2_year_FB_micro.head(10)

filtter_year_FB_mid= df_graph2_year_FB['influencer_tier'] == 'Mid-tier'
df_graph2_year_FB_mid = df_graph2_year_FB.loc[filtter_year_FB_mid]
df_graph2_year_FB_mid = df_graph2_year_FB_mid.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_FB_mid['reactions_per_fan_by_account'] = df_graph2_year_FB_mid.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_FB_mid =df_graph2_year_FB_mid.head(10)

filtter_year_FB_Macro = df_graph2_year_FB['influencer_tier'] == 'Macro'
df_graph2_year_FB_macro = df_graph2_year_FB.loc[filtter_year_FB_Macro]
df_graph2_year_FB_macro = df_graph2_year_FB_macro.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_FB_macro['reactions_per_fan_by_account'] = df_graph2_year_FB_macro.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_FB_macro =df_graph2_year_FB_macro.head(10)

filtter_year_FB_Mega = df_graph2_year_FB['influencer_tier'] == 'Mega'
df_graph2_year_FB_Mega = df_graph2_year_FB.loc[filtter_year_FB_Mega]
df_graph2_year_FB_Mega = df_graph2_year_FB_Mega.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_FB_Mega['reactions_per_fan_by_account'] = df_graph2_year_FB_Mega.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_FB_Mega =df_graph2_year_FB_Mega.head(10)

overall_graph2_year_FB = pd.concat([df_graph2_year_FB_begin,df_graph2_year_FB_nano,df_graph2_year_FB_micro,df_graph2_year_FB_mid,df_graph2_year_FB_macro,df_graph2_year_FB_Mega])

#filter Twitter and tier
filter_TW = df_graph2_year['platform'] == 'Twitter'
df_graph2_year_TW = df_graph2_year.loc[filter_TW]
filtter_year_TW_begin = df_graph2_year_TW['influencer_tier'] == 'Beginner'
df_graph2_year_TW_begin = df_graph2_year_TW.loc[filtter_year_TW_begin]
df_graph2_year_TW_begin = df_graph2_year_TW_begin.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_TW_begin['reactions_per_fan_by_account'] = df_graph2_year_TW_begin.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_TW_begin =df_graph2_year_TW_begin.head(10)

filtter_year_TW_nano = df_graph2_year_TW['influencer_tier'] == 'Nano'
df_graph2_year_TW_nano = df_graph2_year_TW.loc[filtter_year_TW_nano]
df_graph2_year_TW_nano = df_graph2_year_TW_nano.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_TW_nano['reactions_per_fan_by_account'] = df_graph2_year_TW_nano.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_TW_nano =df_graph2_year_TW_nano.head(10)


filtter_year_TW_Micro  = df_graph2_year_TW['influencer_tier'] == 'Micro'
df_graph2_year_TW_micro = df_graph2_year_TW.loc[filtter_year_TW_Micro]
df_graph2_year_TW_micro = df_graph2_year_TW_micro.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_TW_micro['reactions_per_fan_by_account'] = df_graph2_year_TW_micro.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_TW_micro =df_graph2_year_TW_micro.head(10)

filtter_year_TW_mid= df_graph2_year_TW['influencer_tier'] == 'Mid-tier'
df_graph2_year_TW_mid = df_graph2_year_TW.loc[filtter_year_TW_mid]
df_graph2_year_TW_mid = df_graph2_year_TW_mid.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_TW_mid['reactions_per_fan_by_account'] = df_graph2_year_TW_mid.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_TW_mid =df_graph2_year_TW_mid.head(10)

filtter_year_TW_Macro = df_graph2_year_TW['influencer_tier'] == 'Macro'
df_graph2_year_TW_macro = df_graph2_year_TW.loc[filtter_year_TW_Macro]
df_graph2_year_TW_macro = df_graph2_year_TW_macro.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_TW_macro['reactions_per_fan_by_account'] = df_graph2_year_TW_macro.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_TW_macro =df_graph2_year_TW_macro.head(10)

filtter_year_TW_Mega = df_graph2_year_TW['influencer_tier'] == 'Mega'
df_graph2_year_TW_Mega = df_graph2_year_TW.loc[filtter_year_TW_Mega]
df_graph2_year_TW_Mega = df_graph2_year_TW_Mega.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_TW_Mega['reactions_per_fan_by_account'] = df_graph2_year_TW_Mega.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_TW_Mega =df_graph2_year_TW_Mega.head(10)
overall_graph2_year_TW = pd.concat([df_graph2_year_TW_begin,df_graph2_year_TW_nano,df_graph2_year_TW_micro,df_graph2_year_TW_mid,df_graph2_year_TW_macro,df_graph2_year_TW_Mega])

#filter Instagram and tier
filter_IG = df_graph2_year['platform'] == 'Instagram'
df_graph2_year_IG = df_graph2_year.loc[filter_IG]
filtter_year_IG_begin = df_graph2_year_IG['influencer_tier'] == 'Beginner'
df_graph2_year_IG_begin = df_graph2_year_IG.loc[filtter_year_IG_begin]
df_graph2_year_IG_begin = df_graph2_year_IG_begin.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_IG_begin['reactions_per_fan_by_account'] = df_graph2_year_IG_begin.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_IG_begin =df_graph2_year_IG_begin.head(10)

filtter_year_IG_nano = df_graph2_year_IG['influencer_tier'] == 'Nano'
df_graph2_year_IG_nano = df_graph2_year_IG.loc[filtter_year_IG_nano]
df_graph2_year_IG_nano = df_graph2_year_IG_nano.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_IG_nano['reactions_per_fan_by_account'] = df_graph2_year_IG_nano.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_IG_nano =df_graph2_year_IG_nano.head(10)

filtter_year_IG_Micro  = df_graph2_year_IG['influencer_tier'] == 'Micro'
df_graph2_year_IG_micro = df_graph2_year_IG.loc[filtter_year_IG_Micro]
df_graph2_year_IG_micro = df_graph2_year_IG_micro.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_IG_micro['reactions_per_fan_by_account'] = df_graph2_year_IG_micro.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_IG_micro =df_graph2_year_IG_micro.head(10)

filtter_year_IG_mid= df_graph2_year_IG['influencer_tier'] == 'Mid-tier'
df_graph2_year_IG_mid = df_graph2_year_IG.loc[filtter_year_IG_mid]
df_graph2_year_IG_mid = df_graph2_year_IG_mid.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_IG_mid['reactions_per_fan_by_account'] = df_graph2_year_IG_mid.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_IG_mid =df_graph2_year_IG_mid.head(10)

filtter_year_IG_Macro = df_graph2_year_IG['influencer_tier'] == 'Macro'
df_graph2_year_IG_macro = df_graph2_year_IG.loc[filtter_year_IG_Macro]
df_graph2_year_IG_macro = df_graph2_year_IG_macro.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_IG_macro['reactions_per_fan_by_account'] = df_graph2_year_IG_macro.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_IG_macro =df_graph2_year_IG_macro.head(10)

filtter_year_IG_Mega = df_graph2_year_IG['influencer_tier'] == 'Mega'
df_graph2_year_IG_Mega = df_graph2_year_IG.loc[filtter_year_IG_Mega]
df_graph2_year_IG_Mega = df_graph2_year_IG_Mega.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_IG_Mega['reactions_per_fan_by_account'] = df_graph2_year_IG_Mega.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_IG_Mega =df_graph2_year_IG_Mega.head(10)
overall_graph2_year_IG = pd.concat([df_graph2_year_IG_begin,df_graph2_year_IG_nano,df_graph2_year_IG_micro,df_graph2_year_IG_mid,df_graph2_year_IG_macro,df_graph2_year_IG_Mega])


#filter Youtube and tier
filter_YT = df_graph2_year['platform'] == 'Youtube'
df_graph2_year_YT = df_graph2_year.loc[filter_YT]
filtter_year_YT_begin = df_graph2_year_YT['influencer_tier'] == 'Beginner'
df_graph2_year_YT_begin = df_graph2_year_YT.loc[filtter_year_YT_begin]
df_graph2_year_YT_begin = df_graph2_year_YT_begin.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_YT_begin['reactions_per_fan_by_account'] = df_graph2_year_YT_begin.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_YT_begin =df_graph2_year_YT_begin.head(10)

filtter_year_YT_nano = df_graph2_year_YT['influencer_tier'] == 'Nano'
df_graph2_year_YT_nano = df_graph2_year_YT.loc[filtter_year_YT_nano]
df_graph2_year_YT_nano = df_graph2_year_YT_nano.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_YT_nano['reactions_per_fan_by_account'] = df_graph2_year_YT_nano.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_YT_nano =df_graph2_year_YT_nano.head(10)


filtter_year_YT_Micro  = df_graph2_year_YT['influencer_tier'] == 'Micro'
df_graph2_year_YT_micro = df_graph2_year_YT.loc[filtter_year_YT_Micro]
df_graph2_year_YT_micro = df_graph2_year_YT_micro.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_YT_micro['reactions_per_fan_by_account'] = df_graph2_year_YT_micro.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_YT_micro =df_graph2_year_YT_micro.head(10)

filtter_year_YT_mid= df_graph2_year_YT['influencer_tier'] == 'Mid-tier'
df_graph2_year_YT_mid = df_graph2_year_YT.loc[filtter_year_YT_mid]
df_graph2_year_YT_mid = df_graph2_year_YT_mid.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_YT_mid['reactions_per_fan_by_account'] = df_graph2_year_YT_mid.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_YT_mid =df_graph2_year_YT_mid.head(10)

filtter_year_YT_Macro = df_graph2_year_YT['influencer_tier'] == 'Macro'
df_graph2_year_YT_macro = df_graph2_year_YT.loc[filtter_year_YT_Macro]
df_graph2_year_YT_macro = df_graph2_year_YT_macro.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_YT_macro['reactions_per_fan_by_account'] = df_graph2_year_YT_macro.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_YT_macro =df_graph2_year_YT_macro.head(10)

filtter_year_YT_Mega = df_graph2_year_YT['influencer_tier'] == 'Mega'
df_graph2_year_YT_Mega = df_graph2_year_YT.loc[filtter_year_YT_Mega]
df_graph2_year_YT_Mega = df_graph2_year_YT_Mega.sort_values(["reactions_per_fan"], ascending = False)
df_graph2_year_YT_Mega['reactions_per_fan_by_account'] = df_graph2_year_YT_Mega.groupby(['account_id'])['reactions_per_fan'].transform('sum')
df_graph2_year_YT_Mega =df_graph2_year_YT_Mega.head(10)
overall_graph2_year_YT = pd.concat([df_graph2_year_YT_begin,df_graph2_year_YT_nano,df_graph2_year_YT_micro,df_graph2_year_YT_mid,df_graph2_year_YT_macro,df_graph2_year_YT_Mega])
#--------#
#----concat graph----#
overall_graph2_year = pd.concat([overall_graph2_year_FB,overall_graph2_year_TW,overall_graph2_year_IG,overall_graph2_year_YT])
overall_graph2_year['no_of_platforms'] = overall_graph2_year['no_of_platforms'].astype(str)
#export csv file
overall_graph2_year.to_csv('overall_graph2_year.csv',index = False)


#graph insght influencer
#import csv file 
df_graph2_1 = pd.read_csv('overall_df_graph1_2.csv')
df_graph2_1 = df_graph2_1.drop(columns =['Unnamed: 0'])

df_graph2_1 = df_graph2_1.sort_values(["month"])
df_graph2_1 = df_graph2_1.round({'reactions_per_fan': 2})
df_graph2_1 = df_graph2_1.loc[df_graph2_1['reactions_per_fan'] > 0]

#export csv file
df_graph2_1.to_csv('df_graph2_1.csv',index = False)


#GRAPH 3 
#import csv file 
df_graph3 = pd.read_csv('overall_df_graph3.csv')
df_graph3 = df_graph3.drop(columns =['Unnamed: 0'])

df_graph3=df_graph3.set_index('day_of_week')
dayNameIndex = {'Sunday':0,'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6}
df_graph3 = df_graph3.sort_index(key = lambda x : x.to_series().map(dayNameIndex))
df_graph3=df_graph3.reset_index()
df_graph3 = df_graph3.round({'pct_reactions': 2})
df_graph3['month'] = df_graph3['month'].apply(lambda x: calendar.month_name[x])

#export csv file
df_graph3.to_csv('df_graph3.csv',index = False) 


df1 = pd.read_csv('df_graph1_monthly.csv')
platform_G1 = df1['platform'].unique()
platform_G1_default = df1['platform'][0]
df1_1 = pd.read_csv('df_graph1_daily.csv')

df2 = pd.read_csv('df_graph2.csv')
month_G2 = df2['month'].unique() 
month_G2_default = df2['month'][0]
platform_G2 = df2['platform'].unique() 
tier_G2 = df2['influencer_tier'].unique()
df2['no_of_platforms'] = df2['no_of_platforms'].astype(str)

overall_graph2_year = pd.read_csv("overall_graph2_year.csv")
platform_G2_year = overall_graph2_year['platform'].unique() 
tier_G2_year = overall_graph2_year['influencer_tier'].unique()
overall_graph2_year['no_of_platforms'] = overall_graph2_year['no_of_platforms'].astype(str)

df_graph2_1 = pd.read_csv('df_graph2_1.csv')
account = df_graph2_1['account_name'].unique()
account_defult = account[0]
platform1 = df_graph2_1['platform'].unique()
platform1_default = df_graph2_1['platform'][0]

df3 = pd.read_csv('df_graph3.csv')
month = df3['month'].unique()
month_default = df3['month'][0]
platform = df3['platform'].unique()
platform_default = df3['platform'][0]
df3_default = df3[(df3['month']==month_default)]

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#BA001F',
    'color': 'white',
}



app = JupyterDash(__name__,external_stylesheets = [dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True,meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.9, minimum-scale=0.5'}])
server = app.server

#change to layout = for multipages
app.layout = html.Div( children=[

    # Row1: Navigation Bar
    dbc.Navbar(
        dbc.Container(dbc.Row(
            [dbc.Col(
                html.Img(src="./assets/Wisesight-Logo.png", height="40px"),
                width={"size": 3, "order": "first"}
            ),
            dbc.Col(html.Div(
                [
                    html.Div("Access code used to build this dashboard to update data",
                             style={"color":"black", "padding-right":"15px" ,"display":"inline-block"}),
                    dbc.Button("GITHUB", 
                               href="https://github.com/NattakarnCharoensawat/Data_visualization_group_project_2021",
                               external_link=True,
                               style={'backgroundColor': '#BA001F'}
                              )
                ]
                    ),
                width="auto")
            ],
            align="center",
            style={"width": "100%"},
            justify="between"),
        )
    ,style={"padding-top":"30px", "padding-bottom":"30px"}),
#------------Body------------
    # Row2: Heading
    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.Div(children=
                         [html.H1('Thailand Social Media Performance at a Glance',
                                  style={"color":"#BA001F", "font-weight":"bold",'padding-top':'45px' ,"padding-bottom":"10px", "letter-spacing":"2px"}),
                          html.P('Visualising social media data (2020) in Thailand across platforms - Facebook, Twitter, Instagram, and Youtube',style={"font-size":"16px"})]),
                align="left",
                style={"margin-top": '77px', 'margin-bottom': '77px'}
            )
        )
    ]),

    # Row3: Menu
#                     dbc.NavItem(style={"padding-left":"70px"}),

    dbc.Container([
        dbc.Row(
            dbc.Col(dbc.Tabs([
        dbc.Tab(label="Overview", tab_id="tab_graph1",label_style={"color": "white",'backgroundColor':'grey'},active_label_style= tab_selected_style,tab_style={"margin-right":"5px"}),
        dbc.Tab(label="Top 10 Influencers", tab_id="tab_graph2",label_style={"color": "white",'backgroundColor':'grey'},active_label_style= tab_selected_style,tab_style={"margin-right":"5px"}),
        dbc.Tab(label="Search Influencer", tab_id="tab_graph2_2",label_style={"color": "white",'backgroundColor':'grey'},active_label_style= tab_selected_style,tab_style={"margin-right":"5px"}),
        dbc.Tab(label="Best Time to Post", tab_id="tab_graph3",label_style={"color": "white",'backgroundColor':'grey'},active_label_style= tab_selected_style)
    ],
        id="TAB_ALL",active_tab="tab_graph1")))]),
    dbc.Row([
        dbc.Col([html.Div(id="content")])
    ]),


    #Footer
    html.Footer(
        dbc.Container(
            dbc.Row(children=[
                dbc.Col(children=[
                    html.Img(src="./assets/chula_logo.png", height="50px",alt="Chula Logo"),
                    html.Div("© MSc Data Science 2021", style={"font-size":"10px","padding-top":"10px"})
                ]),
                dbc.Col(children=[
                    html.Div("Data Visualization Project By:"),
                    html.Div("น.ส. ณัฐชยา  มหาวิริยะกุล (6480419426)"),
                    html.Div("น.ส. ธมลวรรณ ประสพบูชาธรรม (6480429726)"),
                    html.Div("น.ส. ปิ่นอุษา ตระกูลไพบูลย์ผล (6480450826)"),
                    html.Div("น.ส. ณัฐกรรณ์ เจริญสวัสดิ์ (6480418826)")
                ],width="auto", style={"font-size":"10px"})
                ],
                justify="between",
                align="center"
            )
        ),
        style={'backgroundColor':'#111820', "height":"120px", "color":'white',"padding-top":"21.5px","padding-bottom":"21.5px"}
    )
])
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                    callback layout tab g1
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------#    
@app.callback(Output('content', 'children'),
              Input('TAB_ALL', "active_tab"))
def render_content(active_tab):
    if active_tab == 'tab_graph1':
        return dbc.Container(html.Div([
        html.Div([
            html.H1('Platform Performance')],style={'display': 'inline-block','color' : '#CD2626','padding-top':'45px'}),
        html.Div([
            html.P('Insight on social media platform and their share of audience over the year (2020)')],style={'display': 'block','font-size': '16px'}),
            html.P(''),
        html.Div([
            html.Div([
            html.H5('Select Platform')],style={'color' : '#CD2626','padding-top':'30px'}),
            html.Div([
                dcc.Dropdown(
                    id='platform_G1', 
                    options=[{'label': x, 'value': x} for x in platform_G1],
                     value=['Instagram', 'Youtube', 'Twitter', 'Facebook'], 
                     multi=True)],
            style={'display': 'inline-block','width': '48%'}),
            html.Div([
        html.P('Hover over a dot on the monthly graph to view daily performance of the selected month.')],style={'display': 'block','font-size': '18px','padding-top':'25px',"padding-bottom":"25px",'color':'black'}),
            dbc.Row([
                dbc.Col([
            html.Div([
                html.H6('Monthly'),
                dcc.Graph(id='linechart_G1', figure={})
            ])], xs=12, sm=12, md=5, lg=6, xl=6),
                dbc.Col([html.Div([
                html.H6('Daily'),
               dcc.Graph(id = 'linechart_hover',figure={})    
            ])], xs=12, sm=12, md=5, lg=6, xl=6)
            ],justify='center'),
        ]),
            html.Div([html.H5('Definition'),
            html.Div([html.H6(['Number of fans: '],style={'display': 'inline-block'}),
             html.P(['Latest number of followers by the end of month.'],
                    style={'display': 'inline-block','font-size': '12px'})]),
            html.Div([html.H6(['% Share of fans: '],style={'display': 'inline-block'}),
             html.P(['Ratio of number of fans by platform over total number of fans.'],
                    style={'display': 'inline-block','font-size': '12px'})])], style={"padding-top":"45px"})
    ],style={"padding-bottom":"60px"}))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                    callback layout tab g2
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#    
    
    if active_tab == 'tab_graph2':
        return dbc.Container(html.Div([
        html.Div([html.H1('Top 10 Influencers by Platform and Tier')],style={'display': 'inline-block','color' : '#CD2626', 'padding-top':'45px'}),
        html.Div([
        html.P('Top influencers can be viewed by number of fans or rate of engagement (Average number of reaction per fan)')],style={'display': 'block','font-size': '16px'}),
        html.Div([
        html.H5('Select a Tab Below Yearly or Monthly View')],style={'display': 'block','padding-top':'30px'}),
        html.Div([
            html.Div([
            dcc.Tabs(id="tabs_Graph2", value='tab_YEAR', children=[
            dcc.Tab(label='YEAR (2020)', value='tab_YEAR',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'}),
            dcc.Tab(label='MONTH', value='tab_MONTH',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'})])]),
            html.Div(id='tabs_content_graph')
            ])
        ]))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                    callback layout tab insght influencer
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    if active_tab == 'tab_graph2_2':
        return dbc.Container(html.Div([
        html.Div([
        html.H1('Influencer Performance')],style={'display': 'inline-block','color' : '#CD2626','padding-top':'45px'}),
        html.Div([
            html.Div([
            html.P('Insight on influencer performance by accounts (2020)')],style={'display': 'block','font-size': '16px', "padding-bottom":"30px"}),
            dbc.Row([
                dbc.Col([html.Div([
                html.Div([html.H5('Search Infleuncer by Account Name')],style={'color' : '#CD2626'}),
                html.Div([ 
                    dcc.Dropdown(id='Ac_filter',
                                 options=[{'label': ac, 'value':ac} for ac in account],
                                 value= 'ลงทุนแมน',
                                 searchable=True)
                ])])], xs=10, sm=5, md=5, lg=6, xl=5),
                dbc.Col([html.Div([
                html.Div([html.H5('Select Platform')],style={'color' : '#CD2626'}),
                html.Div([ 
                    dcc.Dropdown(
                        id='platform_break', 
                        options=[{'label': x, 'value': x} for x in platform1],
                        value=['Instagram', 'Youtube', 'Twitter', 'Facebook'], 
                        multi=True)])])], xs=10, sm=5, md=5, lg=6, xl=5)
            ]),
            dbc.Row([
                dbc.Col([html.Div([ 
                dcc.Graph(id = 'bar_all',figure={})
            ],style={'width': '100%', 'display': 'inline-block','align':"center"})])
            ]), 
            dbc.Row([
                dbc.Col([html.Div([
                html.Div([
                html.H4('FACEBOOK')],style={'color' : '#CD2626','text-align': 'center'}),
                dcc.Tabs([  #start tab facebook
                    dcc.Tab(label='Reactions & Fans',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='FB_react_fan',figure={},style={'width': '100%', 'display': 'inline-block'})]),
                    dcc.Tab(label='Reactions',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='FB_react',figure={},style={'width': '100%', 'display': 'inline-block'})]),
                    dcc.Tab(label='Fans',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='FB_fan',figure={},style={'width': '100%', 'display': 'inline-block'})])
                ])])], xs=10, sm=5, md=5, lg=6, xl=5), 
                dbc.Col([ html.Div([
                html.Div([
                html.H4('TWITTER')],style={'color' : '#CD2626','text-align': 'center'}),
                dcc.Tabs([  #start tab TW
                    dcc.Tab(label='Reactions & Fans',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='TW_react_fan',figure={},style={'width': '100%', 'display': 'inline-block'})]),
                    dcc.Tab(label='Reactions',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='TW_react',figure={},style={'width': '100%', 'display': 'inline-block'})]),
                    dcc.Tab(label='Fans',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='TW_fan',figure={},style={'width': '100%', 'display': 'inline-block'})])
                ])])], xs=10, sm=5, md=5, lg=6, xl=5), 
            ],justify='center'),

            dbc.Row([
                dbc.Col([html.Div([
                html.Div([
                html.H4('INSTAGRAM')],style={'color' : '#CD2626','text-align': 'center'}),
                dcc.Tabs([  #start tab IG
                    dcc.Tab(label='Reactions & Fans',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='IG_react_fan',figure={},style={'width': '100%', 'display': 'inline-block'})]),
                    dcc.Tab(label='Reactions',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='IG_react',figure={},style={'width': '100%', 'display': 'inline-block'})]),
                    dcc.Tab(label='Fans',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='IG_fan',figure={},style={'width': '100%', 'display': 'inline-block'})])
                ])])],xs=10, sm=5, md=5, lg=6, xl=5),
                dbc.Col([html.Div([
                html.Div([
                html.H4('YOUTUBE')],style={'color' : '#CD2626','text-align': 'center'}),
                dcc.Tabs([  #start tab YT
                    dcc.Tab(label='Reactions & Fans',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='YT_react_fan',figure={},style={'width': '100%', 'display': 'inline-block'})]),
                    dcc.Tab(label='Reactions',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='YT_react',figure={},style={'width': '100%', 'display': 'inline-block'})]),
                    dcc.Tab(label='Fans',selected_style=tab_selected_style,style={"color": "white",'backgroundColor':'grey'},children=[dcc.Graph(id='YT_fan',figure={},style={'width': '100%', 'display': 'inline-block'})])
                ])])], xs=10, sm=5, md=5, lg=6, xl=5), 
            ],justify='center')

        ]),
            html.Div([html.H5('Definition'),
                      html.H6('Reactions:'),
                      html.P('• FACEBOOK include Like, Love, Angry, Sad, Haha, Share, Comment'),
                      html.P('• TWITTER include Favorite, Retweet, Share, Reply'),
                      html.P('• YOUTUBE include Like, Dislike, Favourite, Comment, View, Share'),
                      html.P('• INSTAGRAM include Like, Comment, Share'),
                     html.Div([html.H6(['Number of fans: '],style={'display': 'inline-block'}),
             html.P(['Latest number of followers by the end of month.'],style={'display': 'inline-block','font-size': '12px'})]),
                      html.Div([html.H6(['Average number of reactions per fans: '],style={'display': 'inline-block'}),
             html.P(['Average number of reactions in each month by account and platform over the number of fans.'],
                    style={'display': 'inline-block','font-size': '12px'})])]
                     ,style={'display': 'block','font-size': '12.5px',"padding-top":"45px", "padding-bottom":"45px"})
    ]))
 #----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                    callback layout tab g3
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    if active_tab == 'tab_graph3':
        return dbc.Container(html.Div([
        html.Div([
                html.H1('Best Time to Post in Each Month')],style={'display': 'inline-block','color' : '#CD2626',"padding-top":"45px"}),
        html.Div([
        html.P('Find out when to share your content for optimal engagement (2020)')],style={'display': 'block','font-size': '16px'}),
        html.Div([
            html.Div([
                html.Div([
                    html.H5('Select Month')],style={'color' : '#CD2626', "padding-top":"30px"}),
                dcc.Dropdown(
                    id='month_G3',
                    options=[{'label':'January','value':'January'},
                                 {'label':'February','value':'February'},
                                 {'label':'March','value':'March'},
                                 {'label':'April','value':'April'},
                                 {'label':'May','value':'May'},
                                 {'label':'June','value':'June'},
                                {'label':'July','value':'July'},
                                 {'label':'August','value':'August'},
                                 {'label':'September','value':'September'},
                                 {'label':'October','value':'October'},
                                 {'label':'November','value':'November'},
                                 {'label':'December','value':'December'}],
                         value = 'January'
                ),
          
            ],
            style={'width': '60%', 'display': 'inline-block'}),
            html.Div([html.P('')]),
             html.Div([
                 html.Div([
                 html.H5('Select Platform')],style={'color' : '#CD2626', "padding-top":"15px"}),
                 dcc.RadioItems(
                     id='platform_G3',
                     options=[{'label': x, 'value': x} for x in platform],
                     value = 'Facebook',
                 inputStyle={"margin-right": "5px","margin-left": "10px"}, style={"padding-bottom":"50px"}),
             ]),
            dbc.Row([
                dbc.Col([dcc.Graph(id='heatmap_G3',  
            figure = {})],align="center")
            ],justify='center')
        ]),
            html.Div([html.H5('Definition'),
                      html.H6('Reactions:'),
                      html.P('• FACEBOOK include Like, Love, Angry, Sad, Haha, Share, Comment'),
                      html.P('• TWITTER include Favorite, Retweet, Share, Reply'),
                      html.P('• YOUTUBE include Like, Dislike, Favourite, Comment, View, Share'),
                      html.P('• INSTAGRAM include Like, Comment, Share')]
                     ,style={'display': 'block','font-size': '12.5px',"padding-top":"45px", "padding-bottom":"45px"})

  
    ])) 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                    callback content G1
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#    
@app.callback(
    Output(component_id='linechart_G1', component_property='figure'),
    Input(component_id='platform_G1', component_property='value'),
)
def update_graph(platform_chosen):
    dff_G1 = df1[df1.platform.isin(platform_chosen)]
    color_discrete_map = {'Facebook': '#002599', 'Instagram': '#ef81ee', 'Twitter': '#56f1ff','Youtube':'#c71e1d'}
    fig = px.line(data_frame=dff_G1, x='month', y='Pct_fan', color='platform',color_discrete_map=color_discrete_map,
                  custom_data=['platform','month'],title='Share of Fan by Platform in 2020',
                 labels=dict(month="Month", Pct_fan="% Share of Fan", platform="Platform")
                  ,hover_data={'Pct_fan':':.2f'})
    fig.update_traces(mode='lines+markers',line=dict(width=3),marker = dict(size = 8))
    fig.update_layout(plot_bgcolor="white",dragmode=False, title_font=dict(size=14),yaxis_ticksuffix = '%')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
    fig.update_layout(margin=dict(l=40, r=100, b=40, t=40))
    return fig

@app.callback(
    Output(component_id='linechart_hover', component_property='figure'),
    Input(component_id='linechart_G1', component_property='hoverData'))
def update_side_graph(hov_data):
    if hov_data is None:
        dff2 = df1_1[(df1_1.month == 'January')&(df1_1.platform == 'Facebook')]
        color_discrete_map = {'Facebook': '#002599', 'Instagram': '#ef81ee', 'Twitter': '#56f1ff','Youtube':'#c71e1d'}
        fig2 = px.line(data_frame=dff2, x='created_date', y='Pct_fan_date',color='platform',color_discrete_map=color_discrete_map
                       ,title='Facebook Share of Fan in January 2020',
                      labels=dict(created_date="Date", Pct_fan_date="% Share of Fan", platform="Platform")
                      ,hover_data={'Pct_fan_date':':.2f'})
        fig2.update_traces(mode='lines+markers',line=dict(width=2),marker = dict(size = 8),showlegend=False)
        fig2.update_layout(plot_bgcolor="white",dragmode=False, title_font=dict(size=14),yaxis_ticksuffix = '%')
        fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=0, tickformat="%d/%m")
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
        fig2.update_layout(margin=dict(l=40, r=100, b=40, t=40))

        return fig2
    else:
        hov_P = hov_data['points'][0]['customdata'][0]
        hov_month = hov_data['points'][0]['x']
        dff2 = df1_1[(df1_1.month == hov_month)&(df1_1.platform == hov_P)]
        color_discrete_map = {'Facebook': '#002599', 'Instagram': '#ef81ee', 'Twitter': '#56f1ff','Youtube':'#c71e1d'}
        fig2 = px.line(data_frame=dff2, x='created_date', y='Pct_fan_date',color='platform',color_discrete_map=color_discrete_map
                       ,title=f'{hov_P} Share of Fan in {hov_month} 2020',
                      labels=dict(created_date="Date", Pct_fan_date="% Share of Fan", platform="Platform")
                      ,hover_data={'Pct_fan_date':':.2f'})
        fig2.update_traces(mode='lines+markers',line=dict(width=2),marker = dict(size = 8),showlegend=False)
        fig2.update_layout(plot_bgcolor="white",dragmode=False, title_font=dict(size=14),yaxis_ticksuffix = '%') 
        fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=0,tickformat="%d/%m")
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
        fig2.update_layout(margin=dict(l=40, r=100, b=40, t=40))

        return fig2
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                    callback tab month year g2
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

    
#callback graph 2 tab
@app.callback(Output('tabs_content_graph', 'children'),
              Input('tabs_Graph2', 'value'))
def render_content(tab):
    if tab == 'tab_YEAR':
        return html.Div([
            html.Div([html.P('')]),
            html.Div([
                html.Div([html.H5('Select Platform')],style={'color' : '#CD2626'}),
                     dcc.RadioItems(
                         id='platform_year',
                         options=[{'label': x, 'value': x} for x in platform_G2_year],
                         value = 'Facebook',
                     inputStyle={"margin-right": "5px","margin-left": "10px"})],style={"padding-top":"15px"}),
            html.Div([html.P('')]),
            html.Div([html.Div([html.H5('Select Tier')],style={'color' : '#CD2626','padding-top':'15px'}),
                      html.Div([
                    html.P('Beginner : 0-1,000 fans        |        Nano : 1,000-10,000 fans        |        Micro : 10,000-50,000 fans        |        Mid-tier : 50,000-500,000 fans        |        Macro : 500,000-1,000,000 fans        |        Mega : over 1,000,000 fans')],style={'display': 'block','font-size': '12px'}),
                     dcc.RadioItems(
                         id='tier_year',
                         options=[{'label':'Beginner','value':'Beginner'},
                                 {'label':'Nano','value':'Nano'},
                                 {'label':'Micro','value':'Micro'},
                                 {'label':'Mid-tier','value':'Mid-tier'},
                                 {'label':'Macro','value':'Macro'},
                                 {'label':'Mega','value':'Mega'}],
                         value = 'Mega',
                     inputStyle={"margin-right": "5px","margin-left": "10px"})],style={"padding-bottom":"60px"}),
            dbc.Row([
                dbc.Col([html.Div([ 
                dcc.Graph(id = 'scatter_year',figure={})
            ],style={'width': '100%', 'display': 'inline-block','align':"center"})])
            ]),
            html.Div([html.H5('Definition'),
                      html.H6('Reactions:'),
                      html.P('• FACEBOOK include Like, Love, Angry, Sad, Haha, Share, Comment'),
                      html.P('• TWITTER include Favorite, Retweet, Share, Reply'),
                      html.P('• YOUTUBE include Like, Dislike, Favourite, Comment, View, Share'),
                      html.P('• INSTAGRAM include Like, Comment,Share'),
                     html.Div([html.H6(['Number of fans : '],style={'display': 'inline-block'}),
             html.P(['Latest number of followers by the end of month.'],style={'display': 'inline-block','font-size': '12px'})]),
                      html.Div([html.H6(['Average number of reactions per fans : '],style={'display': 'inline-block'}),
             html.P(['Average number of reactions in each month by account and platform over the number of fans.'],
                    style={'display': 'inline-block','font-size': '12px'})])],style={'display': 'block','font-size': '12.5px',"padding-bottom":"8px"}),
            html.P(['Source of influencer tier : https://mediakix.com/influencer-marketing-resources/influencer-tiers/ '],style={'display': 'block','font-size': '11px',"padding-bottom":"40px"})
        ])
    
        
 
    elif tab == 'tab_MONTH':
        return html.Div([
            html.Div([html.P('')]),
            html.Div([
                html.Div([html.H5('Select month')],style={'color' : '#CD2626'}),
                     dcc.Dropdown(
                        id='month',
                        options=[{'label': i, 'value': i} for i in month_G2],
                        value = 'January')],style={'width': '60%', 'display': 'inline-block'}),
            html.Div([html.P('')]),
            html.Div([html.Div([html.H5('Select Platform')],style={'color' : '#CD2626'}),
                     dcc.RadioItems(
                         id='platform',
                         options=[{'label': x, 'value': x} for x in platform_G2],
                         value = 'Facebook',
                     inputStyle={"margin-right": "5px","margin-left": "10px"})],style={"padding-top":"15px"}),
            html.Div([html.P('')]),
            html.Div([html.Div([html.H5('Select Tier')],style={'color' : '#CD2626'}),
                      html.Div([
                    html.P('Beginner : 0-1,000 fans  /   Nano : 1,000-10,000 fans  /   Micro : 10,000-50,000 fans   |   Mid-tier : 50,000-500,000 fans    |   Macro : 500,000-1,000,000 fans    |    Mega : over 1,000,000 fans')],style={'display': 'block','font-size': '12px'}),
                     dcc.RadioItems(
                         id='tier',
                         options=[{'label':'Beginner','value':'Beginner'},
                                 {'label':'Nano','value':'Nano'},
                                 {'label':'Micro','value':'Micro'},
                                 {'label':'Mid-tier','value':'Mid-tier'},
                                 {'label':'Macro','value':'Macro'},
                                 {'label':'Mega','value':'Mega'}],
                            value = 'Mega',
                     inputStyle={"margin-right": "5px","margin-left": "10px"})],style={"padding-bottom":"60px"}),
            dbc.Row([
                dbc.Col([html.Div([ 
                dcc.Graph(id = 'scatter_month',figure={})
            ],style={'width': '100%', 'display': 'inline-block','align':"center"})])
            ]),
            html.Br(),
            html.Div([html.H5('Definition'),
                      html.H6('Reactions:'),
                      html.P('• FACEBOOK include Like, Love, Angry, Sad, Haha, Share, Comment'),
                      html.P('• TWITTER include Favorite, Retweet, Share, Reply'),
                      html.P('• YOUTUBE include Like, Dislike, Favourite, Comment, View, Share'),
                      html.P('• INSTAGRAM include Like, Comment,Share'),
                     html.Div([html.H6(['Number of fans : '],style={'display': 'inline-block'}),
             html.P(['Latest number of followers by the end of month.'],style={'display': 'inline-block','font-size': '12px'})]),
                      html.Div([html.H6(['Average number of reactions per fans : '],style={'display': 'inline-block'}),
             html.P(['Average number of reactions in each month by account and platform over the number of fans.'],
                    style={'display': 'inline-block','font-size': '12px'})])],style={'display': 'block','font-size': '12px',"padding-bottom":"8px"}),
            html.P(['Source of influencer tier : https://mediakix.com/influencer-marketing-resources/influencer-tiers/ '],style={'display': 'block','font-size': '11px',"padding-bottom":"40px"})
        ])
        
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                    callback content G2
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#


#callback graph 2     

@app.callback(
    dash.dependencies.Output(component_id='scatter_year',component_property='figure'),
    [dash.dependencies.Input(component_id='platform_year',component_property='value'),
    dash.dependencies.Input(component_id='tier_year',component_property='value')])
    
def update_graph(platform_item,tier_item) :
    bar_data = overall_graph2_year[(overall_graph2_year['influencer_tier'] == tier_item)&(overall_graph2_year['platform'] == platform_item)][['reactions_per_fan','platform','fan','influencer_tier','account_name','no_of_platforms']]
    fig = px.scatter(bar_data, y="fan", x="reactions_per_fan",color='account_name',size_max=30,hover_name="account_name",
                    labels=dict(reactions_per_fan="Average number of reactions per fan", fan="Number of Fans", account_name="Account Name")
                     ,hover_data={'reactions_per_fan':':.2f','fan':':,.0f'},title = f"{platform_item}'s Top 10 {tier_item} Influencers")
    fig.update_layout(plot_bgcolor='white',height=650,dragmode=False,legend = dict(orientation = 'h',yanchor="top",y=-0.2,xanchor="right",x=1) )
    fig.update_traces(marker=dict(size=30,opacity=0.6))
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
    return fig

@app.callback(
    dash.dependencies.Output(component_id='scatter_month',component_property='figure'),
    [dash.dependencies.Input(component_id='month',component_property='value'),
    dash.dependencies.Input(component_id='platform',component_property='value'),
    dash.dependencies.Input(component_id='tier',component_property='value')])
    
def update_graph(month_dropdown,platform_item,tier_item) :
    bar_data = df2[(df2['month'] == month_dropdown)&(df2['influencer_tier'] == tier_item)&(df2['platform'] == platform_item)][['reactions_per_fan_by_account','platform','fan','influencer_tier','account_name','no_of_platforms']]
    fig = px.scatter(bar_data, y="fan", x="reactions_per_fan_by_account",color='account_name',size_max=30,hover_name="account_name",
                    labels=dict(reactions_per_fan_by_account="Average number of reactions per fan", fan="Number of Fans", account_name="Account Name")
                    ,hover_data={'reactions_per_fan_by_account':':.2f','fan':':,.0f'},title = f"{platform_item}'s Top 10 {tier_item} Influencers in {month_dropdown}")
    fig.update_layout(plot_bgcolor='white',height=650,dragmode=False,legend = dict(orientation = 'h',yanchor="top",y=-0.2,xanchor="right",x=1))  
    fig.update_traces(marker=dict(size=30,opacity=0.6))
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
    return fig

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                    callback content graph insight influencer 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#callback graph breakdown


@app.callback(
    Output("bar_all", "figure"), 
    [Input("Ac_filter", "value"),
    Input("platform_break", "value"),], 
)
def update_charts(account,platform):
    filtered = df_graph2_1[(df_graph2_1['account_name'] == account)]
    filtered = filtered[filtered.platform.isin(platform)]
    color_discrete_map = {'Facebook': '#002599', 'Instagram': '#ef81ee', 'Twitter': '#56f1ff','Youtube':'#c71e1d'}

    fig = px.bar(data_frame=filtered, x='month', y='reactions_per_fan', color='platform',barmode='group',
                 color_discrete_map=color_discrete_map,
                 labels=dict(reactions_per_fan="Average reactions per fan",month = 'Month'),
                hover_data={'reactions_per_fan':':.2f'},title=f'Average Reaction Per Fan of {account}')
    
    fig.update_layout(plot_bgcolor="white")
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
    fig.update_traces(marker_line_width=0)
    return fig

@app.callback(
    Output("FB_react_fan", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Facebook')]
    line = px.line(filtered_data, x="month", y=["fan", "reactions"],
                  labels=dict(reactions="Reactions", month="Month",fan = 'Fans'),
                  )
    line.update_layout(title=dict(x=0.5), plot_bgcolor="white",legend = dict(orientation = 'h',yanchor ='bottom',y=1),
                       font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers')
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',title = 'Total Number')
    newnames = {'reactions':'Reactions','fan':'Fans'}
    line.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                         legendgroup = newnames[t.name],
                                         hovertemplate = t.hovertemplate.replace(t.name,newnames[t.name])))
    return line

@app.callback(
    Output("FB_react", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Facebook')]
    line = px.line(filtered_data, x="month", y="reactions", 
                   labels=dict(reactions="Reactions", month="Month"),
                  hover_data={'reactions':':,.0f'})
    line.update_layout(title=dict(x=0.5), plot_bgcolor="white",font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers',line = dict(color='red'))
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
    return line

@app.callback(
    Output("FB_fan", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Facebook')]
    line = px.line(filtered_data, x="month", y="fan", 
                   labels=dict( month="Month",fan = 'Fans'),
                  hover_data={'fan':':,.0f'})
    line.update_layout(title=dict(x=0.5), plot_bgcolor="white",font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers')
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')    
    return line

@app.callback(
    Output("TW_react_fan", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data1 = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Twitter')]
    line = px.line(filtered_data1, x="month", y=["fan", "reactions"], 
                  labels=dict(reactions="Reactions", month="Month",fan = 'Fans'),
                  )
    line.update_layout(title=dict(x=0.5), plot_bgcolor="white",legend = dict(orientation = 'h',yanchor ='bottom',y=1.02),
                       font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers')
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',title = 'Total Number')
    newnames = {'reactions':'Reactions','fan':'Fans'}
    line.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                         legendgroup = newnames[t.name],
                                         hovertemplate = t.hovertemplate.replace(t.name,newnames[t.name])))
    return line

@app.callback(
    Output("TW_react", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data1 = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Twitter')]
    line = px.line(filtered_data1, x="month", y= "reactions", 
                   labels=dict(reactions="Reactions", month="Month"),
                  hover_data={'reactions':':,.0f'})
    line.update_layout(title=dict(x=0.5), plot_bgcolor="white",font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers',line = dict(color='red'))
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')   
    return line

@app.callback(
    Output("TW_fan", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data1 = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Twitter')]
    line = px.line(filtered_data1, x="month", y="fan", 
                   labels=dict( month="Month",fan = 'Fans'),
                  hover_data={'fan':':,.0f'})
    line.update_layout(title=dict(x=0.5), plot_bgcolor="white",font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers')
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')   
    return line


@app.callback(
    Output("IG_react_fan", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data2 = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Instagram')]
    line =  px.line(filtered_data2, x="month", y=["fan", "reactions"], 
                   labels=dict(reactions="Reactions", month="Month",fan = 'Fans'),
                   )
    line.update_layout(title=dict(x=0.5), plot_bgcolor="white",legend = dict(orientation = 'h',yanchor ='bottom',y=1.02),
                       font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers')
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',title = 'Total Number')
    newnames = {'reactions':'Reactions','fan':'Fans'}
    line.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                         legendgroup = newnames[t.name],
                                         hovertemplate = t.hovertemplate.replace(t.name,newnames[t.name])))
    return line

@app.callback(
    Output("IG_react", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data2 = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Instagram')]
    line =  px.line(filtered_data2, x="month", y= "reactions", 
                   labels=dict(reactions="Reactions", month="Month"),
                   hover_data={'reactions':':,.0f'})
    line.update_layout(title=dict(x=0.5), plot_bgcolor="white",font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers',line = dict(color='red'))
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')   
    return line

@app.callback(
    Output("IG_fan", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data2 = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Instagram')]
    line =  px.line(filtered_data2, x="month", y="fan", 
                   labels=dict( month="Month",fan = 'Fans'),
                   hover_data={'fan':':,.0f'})
    line.update_layout( plot_bgcolor="white",font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers')
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')   
    return line

@app.callback(
    Output("YT_react_fan", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data3 = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Youtube')]
    line =  px.line(filtered_data3, x="month", y=["fan", "reactions"], 
                   labels=dict(reactions="Reactions", month="Month",fan = 'Fans'))
    line.update_layout(plot_bgcolor="white",legend = dict(orientation = 'h',yanchor ='bottom',y=1.02),
                       font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers')
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',title = 'Total Number') 
    newnames = {'reactions':'Reactions','fan':'Fans'}
    line.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                         legendgroup = newnames[t.name],
                                         hovertemplate = t.hovertemplate.replace(t.name,newnames[t.name])))
    return line

@app.callback(
    Output("YT_react", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data3 = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Youtube')]
    line =  px.line(filtered_data3, x="month", y= "reactions", 
                   labels=dict(reactions="Reactions", month="Month"),
                   hover_data={'reactions':':,.0f'})
    line.update_layout(plot_bgcolor="white",font=dict(size=12,color="black"),dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers',line = dict(color='red'))
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')   
    return line

@app.callback(
    Output("YT_fan", "figure"),
    [Input("Ac_filter", "value")])
def update_charts(account):
    filtered_data3 = df_graph2_1[(df_graph2_1["account_name"] == account)&(df_graph2_1["platform"] == 'Youtube')]
    line =  px.line(filtered_data3, x="month", y="fan",
                   labels=dict( month="Month",fan = 'Fans'),
                   hover_data={'fan':':,.0f'})
    line.update_layout(title=dict(x=0.2),plot_bgcolor="white",font=dict(size=12,color="black"),
                       dragmode=False,legend_title_text = ' ')
    line.update_traces(mode='lines+markers')
    line.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey',tickangle=45,dtick = 1,ticktext=['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December'],tickvals=list(range(1,13)))
    line.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')   
    return line


#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                    callback content graph 3
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#callback graph 3
@app.callback(
    dash.dependencies.Output(component_id='heatmap_G3',component_property='figure'),
    [dash.dependencies.Input(component_id='month_G3',component_property='value'),
     dash.dependencies.Input(component_id='platform_G3',component_property='value')])
    

def update_graph(month_dropdown,platform_item):
    heatmap_data = df3[(df3['month'] == month_dropdown) & (df3['platform']==platform_item)][['day_of_week','hour','pct_reactions']]
    fig=go.Figure()
    fig.add_trace(go.Heatmap(
                x=heatmap_data['day_of_week'],
                y=heatmap_data['hour'],
                z=heatmap_data['pct_reactions'],
                hovertemplate='Day of week: %{x}<br>Hour: %{y}<br>% Reactions: %{z}<extra></extra>',
                xgap = 2,
                ygap = 2,
                colorscale='bluyl',
                colorbar={"title": '% Reactions'}))
    fig.update_layout(height=600,dragmode=False,title = dict(text =f"{platform_item}'s Share of Reaction in {month_dropdown}",x=0.5, font=dict(size=14))) 
    fig.update_xaxes(title = 'Days of Week')
    fig.update_yaxes(title = 'Hours of Day',ticktext=['00:00', '01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'],
                     tickvals=list(range(24)))
    return fig    
if __name__ == '__main__':
    app.run_server(debug=True)