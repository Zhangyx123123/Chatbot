# HW1: Chatbot

## Author

Haoyu Yan, hy2574
Yuxuan Zhang, yz3377

## Frontend in S3
The endpoint for this project is: http://chatbotanniver.s3-website-us-west-2.amazonaws.com
Frontend:
Develop a user interface using JavaScript, CSS and Html. 

![image-20181017224332985](assets/image-20181017224332985.png)

Host the whole frontend into an AWS S3 bucket

![image-20181017224438225](assets/image-20181017224438225.png)

And then host the static website index.html. 
The endpoint for this project is: http://chatbotanniver.s3-website-us-west-2.amazonaws.com, which can be viewed in attributes of the bucket.


## Backend
Backend:
Import the swagger file into API gateway

![image-20181017224534192](assets/image-20181017224534192.png)

Create a lambda function for post method in the API which is **Generat_message** function for our case.

![image-20181017224621527](assets/image-20181017224621527.png)

And then incorporate the lambda function into post method to perform the chat operation:

![image-20181017224725636](assets/image-20181017224725636.png)Also, enable CORS on our API methods by enable CORS for methods and create the option method 

![image-20181017224744098](assets/image-20181017224744098.png)

Setup the API key for the API by adding new API key and use plan for the API:

![image-20181017225014821](assets/image-20181017225014821.png)

Generate SDK for our API, in our case, we choose JavaScript as our platform. And then move the zip file which is the package of SDK to the frontend project. Then follow the readme file in the SDK package to use the SDK in our project, and update the Frontend to call the API using the API key above.

![image-20181017224853852](assets/image-20181017224853852.png)




