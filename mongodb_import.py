import pymongo
import pandas as pd
import json
client=pymongo.MongoClient("mongodb://localhost:27017")
df=pd.read_csv("predictions.csv")
df.head()
data=df.to_dict(orient="records")
db=client["Facial_Emotion_Model_Predictions"]
print(db)
db.Images_Predictions.insert_many(data)
