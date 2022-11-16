#importing Sbopen class from mplsoccer to open the data
from mplsoccer import Sbopen
#Use a parser Sbopen available in mplsoccer.
parser = Sbopen()

def breakline(s):
    print("\n" + "------------" + s + "-----------" + "\n")

breakline("Competition Data")

#Opening data using competition method
df_competition = parser.competition()
#view the structure of the data
df_competition.info()

breakline("Match Data")

#Opening data using match method using competition_id and season_id
df_match = parser.match(competition_id = 72, season_id = 30)
#view the structure of the data
df_match.info()

breakline("Lineup Data")

#Opening data using lineup method using game_id
df_lineup = parser.lineup(69301)
#view the structure of the data
df_lineup.info()

breakline("Event Data")

#Opening data using lineup method using game_id

#df_event, df_related, df_freeze, df_tactics = parser.event(69301)

#parser.event(<game_id>) returns 4 dataframes:
#At index 0: The event data
df_event = parser.event(69301)[0]
#At index 1: information on events that were related to each other - for example ball pass and pressure applied
df_related = parser.event(69301)[1]
#At index 2: freezed frames with player position in the moment of shots
df_freeze = parser.event(69301)[2]
#At index 3: information about player position on the pitch
df_tactics = parser.event(69301)[3]

#view the structure of the data
df_event.info()
# #view the structure of the data
# df_related.info()
# #view the structure of the data
# df_freeze.info()
# #view the structure of the data
# df_tactics.info()

breakline("360 Data")

df_frame, df_visible = parser.frame(3788741)

# exploring the data
df_frame.info()
df_visible.info()
