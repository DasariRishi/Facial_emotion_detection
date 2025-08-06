# Facial_emotion_detection
Facial Emotion Detection using CNN.
[Watch the video here](project_illustration.mp4)

We have implemented Machine Learning model on the FER2013 dataset to find the best performing model and deploy it in our application which 
classifies the emotions using 7 categories. After observing the performance of different models, we decided to implement CNN model as our main model for 
image classification. The train.py file in the folder makes use of the CNN model to perform classification
This file will help you understand how to run the .ipynb and GUI source code.

1. Running .ipynb files.

We have used google collab to run these algorithms on the dataset. Therefore, please open these .ipynb files in your Google Collab.
The dataset is uploaded on the Google Drive.
you can download the Dataset from the link https://www.kaggle.com/datasets/msambare/fer2013


Also make sure the GPU is enabled in the Google Collab. To enable the GPU please follow below mentioned steps:
Go to the notebook >> Click on 'EDIT' on the top >> Click on 'Notebook Settings' >> Click on 'Hardware Accelarator' and add GPU.

After the above step, please run .ipynb files. 


2. Running facial_expression_gui.py 

In order to run this program, please download the trained_facial_expression_model.h5 file. Open Cmd prompt in this folder's location and use the following command to run the file.
Since we were not able to access the web came. save a recorded mp4 file in the same folder as that of facial_expression_gui.py file rename the video as V5.mp4. Then run the program using following command.

Command: python facial_expression_gui.py
