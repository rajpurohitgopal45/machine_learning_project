# machine_learning_project

creating conda environment.
conda create -p venv python==3.7 -y
conda activate venv/

to add file
git add .

to check the git status
git status

to check all versions
git log

to crete version/commit 
git commit -m "message"

to check remote url
git remote -v

to send changes
git push origin main

to setup ci/cd pipeline in heroku we need below details
Heroku email = oggymafia@gmail.com
Heroku api_key =  
Heroku app name =  sim-ml-regression

to build docker image
docker build -t <image name>:<tagname> .
docker images
docker run -p 5000:5000 -e PORT:5000 <image id>
look running images   docker ps
to stop doker stop <container id>
