This section of the repository refers to the Mock server that could provide the information toward to the user

At the body of the repo we could see the python file with the name of Mock.py. This python code was used for converting the results which taken from the simulator as well as  cleaning the results and send to the client

You could run this python code by: python Mock.py test.txt and see the result at 127.0.0.1:1235

I need to mention that Mock.py was implemented for making familiar with the concept of socket binding 

After I have done the Mock.py I have development the Flask server which you could see at Python_Flask_Server folder

at Python_Flask_Server we have main.py which is the main body of the Flask server and you could run it by typing python main.py inside the server we have sub-routins such as uploader which gives the chance to the user for upload the suitable file, the next sub-routin is file-download that return the converted json format of the inputed file. 

In order to see the Flask server you could simply write the browser 127.0.0.1:123456789 

all the required templated that are used for the Flask server is located at template folder
