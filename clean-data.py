import pandas as pd

BAreviews = pd.read_csv('data_BA_reviews.csv')
reviews = BAreviews['reviews']
reviews.str.replace('Trip Verified', '')
reviews.str.replace('✅', '')
reviews.str.replace('Verified Review', '')