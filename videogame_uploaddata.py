import pandas as pd
import mysql.connector
# MySQL connection details
db_config = {
    'user': 'ugoeze',
    'password': 'Luchiegaezy07+',
    'host': 'localhost',
    'database': 'mytestdatabase'
}



def upload_csv_to_mysql(csv_file, table_name):
    # Read CSV file
    data = pd.read_csv(csv_file)
    
    # Establish a database connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    # Insert data into MySQL table
    
    video_game_columns = f"""
    INSERT INTO {table_name} (
                Game_Title, User_Rating, Age_Group_Targeted, Price, Platform, Requires_Special_Device, Developer, Publisher, 
                Release_Year, Genre, Multiplayer, Game_Length_Hours, Graphics_Quality, Soundtrack_Quality, Story_Quality,
                User_Review_Text, Game_Mode, Min_Number_of_Players
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                
    for _, row in data.iterrows():
        cursor.execute(video_game_columns, (
            row['Game Title'], row['User Rating'], row['Age Group Targeted'], row['Price'],
            row['Platform'], row['Requires Special Device'], row['Developer'], row['Publisher'],
            row['Release Year'], row['Genre'], row['Multiplayer'], row['Game Length (Hours)'], row['Graphics Quality'],
            row['Soundtrack Quality'], row['Story Quality'], row['User Review Text'], row['Game Mode'], row['Min Number of Players']
            ))
    # Commit and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Data uploaded successfully")
# Upload data from CSV to MySQL
upload_csv_to_mysql('video_game_1.csv', 'videogame')