### Iris Flower Predictor Project
This is a mini project where I learned how to make a machine learning model work like a real app. It predicts what type of flower is it,

### What I Did ??
I learned a lot in just few days. Now, my goal is to master these concepts, Here's a quick look:

- Trained a Model: I trained model on RandomForestClassifier model.
- Saved the Model: I saved my trained program as a .pkl file so I can use it later as a brain of my app.
- Made a Web API: I built a simple web api (using Flask) 
- Learned POST Requests: This is how you send information to the web API to get a prediction.
- Dockerized It: I packed my app into a Docker container. Think of it as a self-contained box that allowed to runs my app anywhere. 
   - made a Dockerfile: i made a file, which will be instructions for the box and a .dockerignore file. The .dockerignore file helps keep the box small and tidy by removing extra file. 
   - Used Docker Compose: This helps run my app and other tools (like Redis) together easily with one command.
   - Added Redis: This is like a super-fast cache which helps to get and set prediction for my app to use.
   - Used Volumes: This gives my app permission to save data permanently, even if I restart later. 
 - Added Environment Variables & Health Checks: I added ways to easily change settings for my app and to make sure it's always working properly.

### How to Run It
You'll need Docker Desktop installed first.

### Get the project: Download my project files
Go to the project folder: Open your command line and go to where you saved the files.

Start it up: Type this command in bash:

***Bash***

```
docker compose up --build -d

This will build and run everything in the background.
