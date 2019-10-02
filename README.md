# How to set up the PoP project
**PREREQUISITES:** Latest edition of python installed. client.py and server.py are pulled from git repo
**Definitions:** root directory - root of where you want your project contents (i.e. C:\Users\jeff\infosec)
## Setting up the server
1. Open terminal (cmd for windows or bash for mac) and navigate to desired root directory
2. **If you haven't ever run the server before,** from desired root directory, create virtual environment by running the command below. 
```python
py -m venv env
```
3. You should now have a folder venv (mine is ...\infosec\env). Activate the virtual environment from the root dir by running: 
```
env\Scripts\activate 
```
4. **If you haven't ever run the server before,** install Flask to this virtual environment by running the command below.
```python
pip install flask 
```
5. Set environment variable for the FLASK_APP to be the flask server we made:
```python
set FLASK_APP=server.py
```
5. Now, setup is done. Run the server by executing the command below. Make sure server.py is in your root directroy
```python
flask run
```
6. Stop execution by pressing CTRL+C in the cmd. Deactivate virtual environment by running 
```python
deactivate
```
