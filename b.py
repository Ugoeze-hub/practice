import pandas as pd
video = pd.read_csv("C:/Users/USER 16/Documents/video_game_reviews.csv")
video.to_csv('video_game_1.csv', index = False)