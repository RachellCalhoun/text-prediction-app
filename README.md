# text-classification-eda
Supervised and Unsupervised learning for Text difficulty classification

### Set up

1. install python
    - check https://tutorial.djangogirls.org/en/installation/#python for more instructions on getting set up
2. Install A Code Editor if you don't have one already
    - https://tutorial.djangogirls.org/en/installation/#code-editor
2. create virtual environment in or outside of this folder:
    - some details here: https://tutorial.djangogirls.org/en/installation/#virtualenv
    - `python -m venv textvenv` 
    - (for windows) `textvenv\Scripts\activate`
4. Install Git
    - https://tutorial.djangogirls.org/en/installation/#git
5. Pull down code from github:
    - git pull origin main 
6. Install Requirements: 
    - (make sure your venv is activated, see step 3) `pip install -r requirements.txt`
    
    
 
 ### Making changes
 
 If you want to make changes, always do so on a different branch, not on the `main` branch. This will server to keep our workflow clean and manageable. 
 If you made a lot of changes but find yourself on the `main` branch, one way to fix this is to do the following: 
     - `git stash`
     - `git checkout -b newbranchname`
     - `git stash pop` 
 
 This will move your changes from the main branch to the new `newbranchname` branch. Reach out if you have problems with this. 
 
  #### Branch naming: 
     - it might be a good idea to keep our branching naming features standardized. 
         - `r1-initial-testing`, `l1-creativename`, `r2-blahblah` etc where "r" is for Rachell and "l" is for Lauren

#### Before making any changes update your local main branch
this is important to pull down any changes in the reposity that maybe someone else has done. 
1. `git status` (make sure you are in the right directory and are on the `main` branch) 
2. `git pull origin main` 
3. then proceed to checkout a branch etc. 


### Process to make changes
 1. Check out a new Branch 
     - on your system create a new branch (make sure to be in this directory `git status` will verify you are in the right place)
     - `git checkout -b name-of-new-branch`  this will create a new branch and place you in it. an example can be : `git checkout -b r-feature-exploration` 
 2. Make any changes you want
 3. add any files that should be ignored to `.gitignore`
 4. check the status: `git status` 
 5. add all the files: `git add --all`
 6. commit all the files: `git commit -m"some message here"
 7. push changes to github: `git push origin mybranchname` 
 8. Go to github.com and create a pull request
     
    
 ### Running the programs: 
 1. open the terminal and directory where these files are
 2. to run the script type this in the terminal: `python supervised_learning_trained.py`


### Running the jupyter notebook 
If you'd like to run the jupyter notebook locally:
1. open the terminal, make sure your venv in activated and you are correct directy and run: 
    - `jupyter notebook` 
    - this should open up the jupyter notebook in the browser



### Running Datasette Locally (https://docs.datasette.io/en/stable/)
- update dependencies: `pip install -r requirements.txt` to install requirements 
- download the csv from google collab called `Supervised_Cleaned.csv`
- to created the sqlite db file run the command `sqlite-utils insert supervised_cleaned.db supervised_readability Supervised_CleanData.csv --csv`
 - to publish new dataset (if new supervised cleaned has been created/updated): 
    - `datasette  publish heroku supervised_cleaned.db --title "Supervised Readability" -n supervised-text-readability --install datasette-vega`
    - (this is set up through heroku and currently on Rachell's account. If you are here and want to do this please let Rachell know and she can try to set you up on the heroku account) 

