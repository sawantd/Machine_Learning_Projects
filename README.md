## Start Machine_Learning_Projects.

### Software and account Requirement.

1. [Github Account](https://github.com/)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)
5. [Git Documentation](https://git-scm.com/docs/gittutorial)


Creating Conda environment
```
conda create -p venv python==3.7 -y
```

To activate the environment
```
conda activate venv/
```
OR
```
conda activate venv
```

To install the libraries in requirements.txt file
```
pip install -r requirements.txt
```

To Add giles to git
```
git add .
```

OR
```
git add <file_name>
```

> Note : To ignore file/folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```

To check all versions maintained by git
```
git log
```

To check version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = darshanasawant1996@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression-app-d

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

> Note : Image name for docker must be in small case


```
python setup.py install
```

Install ipykernel
```
pip install ipykernel
```