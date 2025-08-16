# Color-Changing Flask Application

A simple web application that displays a page with a randomly changing background color every 5 seconds.

## Features

- Random background color generation on each page refresh
- Full-screen color display
- Automatic refresh every 5 seconds
- Clean, responsive design
- Displays current color hex code

## Prerequisites

- Docker

## Installation

### Using Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/sarmadali77771/Python-Flask-MultiColors-App.git

2. Build Docker image:
   ```bash
   #To build image by single stage file name Dockerfile 
   docker build -t multicolors-app .
   
   #Now check image size run docker image ls
   
   OR
   
   #Implementing a multi-stage Dockerfile with a distroless image has dramatically reduced the overall container image size.
   #To run app with multi stage file name Dockerfile_multiStage
   docker build -f Dockerfile_multiStage -t multicolors-app-mini

   #Now check image size run docker image ls and compare

   

3. Run the container:
   ```bash
   docker run -d -p 5000:5000 --name colors multicolors-app

3. Access app in browser:
   ```bash
   http://localhost:5000

4. Troubleshooting:
   ```bash
   docker logs colors #Check container logs
   docker ps #Verify container is running
   netstat -tulnp | grep 5000 #Check port availability

Project Structure:
   ```bash
   multicolors-app/
   ├── Dockerfile
   ├── requirements.txt
   ├── app.py
   ├── templates/
   │   └── index.html
   └── static/
       └── style.css

License
MIT License

Author
Sarmad Ali - https://github.com/sarmadali77771/

  
