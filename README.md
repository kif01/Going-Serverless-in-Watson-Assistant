# Going-Serverless-in-Watson-Assistant
This repo contains assets for a webinar that shows how to build a Watson Assistant chatbot integrated with IBM Cloud Functions.

# Architecture Flow
<img width="609" alt="Screen Shot 2020-07-20 at 3 28 39 AM" src="https://user-images.githubusercontent.com/15332386/122041699-48104800-cdea-11eb-804c-7667f094ea04.png">


# Instructions
1- Log in to your [IBM Cloud Account](https://ibm.biz/BdfFsS) <br>
2- Create a Watson Assistant service <br>
3- Import the **dialog.json** file from this repo <br>
4- Create a Cloud Object Storage Instance  <br>
5- Create a bucket in this COS instance  <br>
6- Upload the **plans.csv** file in the bucket <br> 
7- Create an action in Cloud Functions <br>
8- Insert the code that you have in the **cf-action.py** file <br>
8- Change the parameters values to the values you have in your COS credentials <br>
9- Copy the public endpoint of this action and put it in the Watson Assistant Webhook under Options <br>

**Click [Here](https://khalil-faraj.gitbook.io/go-serverless-with-watson-assistant/) for the complete detailed step-by-step instructions** 


