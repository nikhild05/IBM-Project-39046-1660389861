<br>
<div align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg"  align="center" alt="drawing" width="200" />
  <h2 align="center"> Smart Solution for Railways <br></h2>

  </div>
 <br> 
 <h3>IBM-Project-39046-1660389861</h3>  
   

## Team Members
 - [Team Lead - Nikhil Dhaka (718019Z334)](https://github.com/nikhild05)
 - [Member 1 - Niranjan S (718019Z335)](https://github.com/niran1412)
 - [Member 2 - Rohit Sonar (718019Z342)](https://github.com/Rohit-2001-Sonar)
 - [Member 3 - Vasanthan M (718019Z359)](https://github.com/Vasanthan916)
 
## Abstract
Next to airways, trains are one of the fastest modes of transportation. Being the preferred choice among vast majority of middle class and impoverished people, it attracts for its amenities. But, passengers in trains are increasingly at risk from thefts and accidents. The most common forms of these hazards include chain snatching, derailment, and fire accidents. People no longer want to travel in trains alone or at night because they believe they are unsafe. The rail accidents are
documented by the National Crime Bureau. As a result, the federal government has implemented new security measures that mandate 2 to 5 RPF in train at all times. It can be used as starting point, however, it falls short in certain situations. We give a solution to address these problems by providing an application which the user can access after booking. With a single click, this app addresses the most urgent train issues, such as fire incidents, the prevalence of unreserved passengers in reserved compartments, and chain snatching. Hereby, a text message will be sent to the TC and RPF as an alert notification. Our project uses the Node-Red service,
app development, and IBM cloud platform to store passenger data.
## Ideation Phase
 - [Problem Statement](https://github.com/IBM-EPBL/IBM-Project-39046-1660389861/blob/main/Pre-Development%20Phase/Project%20Planning/ProblemStatement-SmartSolutionForRailways-PNT2022TMID12653.pdf)
 - [Empathy Map](https://app.mural.co/invitation/mural/ibm06765/1663722824795?sender=u456599987bbb7a87edd88416&key=2b27581c-8311-44c9-ba0f-ed6c46e3df1f)
 - [Litrature Review](https://github.com/IBM-EPBL/IBM-Project-39046-1660389861/blob/main/Pre-Development%20Phase/Project%20Planning/Literature%20Survey-SmartSolutionForRailways-PNT2022TMID12653.pdf)
 - [Brainstorming & Ideation Map](https://app.mural.co/invitation/mural/ibm06765/1663720067648?sender=u456599987bbb7a87edd88416&key=255e2a72-c50e-4e4b-b334-064908996a86)

### Objectives
- Gain knowledge of Watson IoT Platform.
- Connecting IoT devices to the Watson IoT platform and exchanging the sensor data.
- Gain knowledge on IBM Cloudant DB
- Explore Python client libraries of Watson IoT Platform.
- Explore Python library for integrating OpenCV for accessing the Live Camera Input
- Scan the QR code in live streaming and retrieve the QR code details
- Gain knowledge on web application development.
- Gain knowledge of storing the data in Cloudant DB
- Generating QR codes with the required data.

### Project Flow
- Using the Web application, a user books a ticket based on the availability of the seats by giving the general required information.
- Once a user clicks on the submit button, a QR code is generated with a Unique ID and the data is stored in the Cloudant DB with that Unique ID.
- Users can save the QR code for further process. 
- In python code, a Ticket collector can scan the QR code and extract the information from the QR  Code i.e., Unique ID. With that Unique ID, data is fetched from the Cloudant DB, if it is not found, then it displays Not a Valid Ticket.
- Also, the live location of the train will be published to IBM IoT platform using python code
- The train location can be tracked from a Web Application.
