.. _developer-guide:

Developer\'s Guide
******************

.. toctree::
    :hidden:

This section gives function and class definitions used in the development of 
OrgoChemVisualizer. 

If you are a first-time contributer:
- Go to https://github.com/cjcrowder1/OrgoChemVisualizer
- Click on the 'Fork' button in the top right of the screen
  This creates your own copy of the project
-Go to your own Github repository and you will see a repository named OrgoChemVisualizer
 Click into this repository and make a local copy of it by hitting the clone button
 Copy the URL shown

--If using Visual Studio Code:
  Open Source control and push Clone Repository, this will open a window to type in the repository name
  Type in the repository name and select the repository
  If prompted to, sign into Github and return to VS Code
  -Remember, push requests must be fulfilled to push changes to Github
   When you make changes and save the file, Source Code will show an alert that there is a pending change
   Navigate to Source Code, select the wanted changes, add a comment in the top textbox, and press the check button
   Then hit the arrow button in the blue bottom section of VS Code to fulfill the push requests
  -To have the latest changes of the software from other contributers, press the same arrow button to pull the changes

--For general use (not using VS code):
  Clone the project to your local computer using the copied URL
  Change the directory using: cd numpy
  Add the upstream repository: git remote add upstream [repository website]
  Now git remote -v will show two remote repositories named: origin and upstream
  -Pull latest changes:
   Use: git checkout master, and git pull upstream master
   Create a branch for the feature you want to work on: git checkout -b [branch name]
  -Push changes
   Use: git push origin [branch name]

   To add new chemicals/molecules for a reaction:
   -Navigate to the folder chemanim.py
   -Follow the format below for creating molecules:
   
   class CO2(Chemical):
    def __init__(self):
        super(CO2, self).__init__()

        pos = self.get_positions()
        adj = self.get_edges()
        sym = [strToSym("O"), strToSym("C"), strToSym("O")]

        self.setData(pos=pos, adj=adj, pxMode=False,
                     symbol=sym, antialias=True)

    def get_positions(self):
        return np.array([
                        [-1, 13],
                        [0, 13],
                        [1, 13],
                        ], dtype=float)

    def get_edges(self):
        return np.array([
                        [0, 1],
                        [1, 2],
                        ])

** similar formats are used for arrows and textboxes, these are also found in the chemanim.py file
- Add the chemical/molecule created to the __main__.py file using the format:
#self.mol2 = ca.CO2()
and 
#self.addItem(mol2)

 To create the animations:
 -Navigate to the __main__.py file
 -Make sure the chemical(s)/molecule(s) wanted for the animation and/or reaction have been added to the file
 -Follow the format for the reaction sequences (from the other reactions 1-3)
 *Naming the animation follows the format:
 Example from Reaction 2
 self.R2S1
 Where R2 stands for Reaction 2, and S1 indicates that it is the first chemical/molecule in the reaction

 **Textboxes and arrows are animated in similar ways