import pandas as pd
cleaned_reaction_types = pd.read_csv("ReactionTypes.csv")
cleaned_reaction_types.to_csv('cleaned_reaction_types.csv', index = False)