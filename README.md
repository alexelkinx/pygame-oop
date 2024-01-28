## Pygame

This is a small game project created using pygame.

### Dependencies

To run the project on a local machine, you need to have the following software installed:

* Python ver. 3.11 or higher
* Pygame ver. 2.5.2

### Installing

1. Open the CLI and change the current working directory to the location where you want the cloned directory.
2. Clone the repository to your local machine:
  ```
  git clone https://github.com/kot-alex/pygame-oop.git
  ```
3. Make sure that Python is installed on your system by running the command `python --version` OR `python3 --version` for Mac. If Python is installed, it will output the version, otherwise, you'll need to install it on your system.
4. Run `pip install -r requirements.txt` to install additional packages from the given requirements file.

### Executing program

1. First, open your CLI.
2. Navigate to the project folder.
3. Run the program by typing `python main.py`.

## For collaborators

* Stick to lowercase for branch names and use hyphens to separate words. For instance, `feature/new-login` or `bugfix/header-styling`.
  
* Create **new** branches for each task. For example, if you are working on the "authorization" feature, create a `feature/auth` branch.
  ```
  git checkout -b feature/auth             // create a new branch based on your currently checked out (HEAD) branch
  ```
* Push your local repository to GitHub.
  ```
  git push -u origin feature/auth
  ```
* Periodically, changes made to `main` (if any) should be merged back into your feature branch.
  ```
  git checkout feature/auth                // switch to feature/auth branch
  git merge main                           // merges changes from main into feature branch
  ```
* When development of the feature is complete, your should merge changes into main.
  ```
  git checkout main                        // switch to main branch
  git merge feature/auth                   // merge “feature/auth” to “main”
  ```
* Then delete local and remote branches.
  ```
  git branch -d feature/auth               // deleting local branches
  git push origin --delete feature/login   // deleting remote branches
  ```
