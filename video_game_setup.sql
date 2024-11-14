CREATE DATABASE IF NOT EXISTS videodatabase;
 USE videodatabase;
 CREATE TABLE IF NOT EXISTS videogame (
     id INT AUTO_INCREMENT PRIMARY KEY,
     Game_Title VARCHAR(255),
     User_Rating INT,
     Age_Group_Targeted VARCHAR(20),
     Price INT,
     Platform VARCHAR(30),
     Requires_Special_Device VARCHAR(3),
     Developer VARCHAR(30),
     Publisher VARCHAR(20),
     Release_Year INT,
     Genre VARCHAR(20),
     Multiplayer VARCHAR(3),
     Game_Length_Hours VARCHAR(3),
     Graphics_Quality VARCHAR(7),
     Soundtrack_Quality VARCHAR(10),
     Story_Quality VARCHAR(10),
     User_Review_Text VARCHAR(50),
     Game_Mode VARCHAR(10),
     Min_Number_of_Players INT
 );