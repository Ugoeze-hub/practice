import pandas as pd
cleaned_reaction_types = pd.read_csv("ReactionTypes.csv")
cleaned_reaction_types.index = range(1, (len(cleaned_reaction_types) + 1))
cleaned_reaction_types.to_csv('cleaned_reaction_types.csv')