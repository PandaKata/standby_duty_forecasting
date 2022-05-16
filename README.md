
 # Task: Automation of Standby Duty Planning for Rescue Drivers via a Forecasting Model

### structure


```bash
$ pwd
/Users/kata/Desktop/GitHub/credit_card_routing
$ ls
|- notebooks/
   |- EDA.ipynb
   |- 02-second-logical-notebook.ipynb
   |- prototype-notebook.ipynb
   |- archive/  
      |- no-longer-useful.ipynb
|- standby_project/                     <- all things refactored out of notebooks
   |- __init__.py                       <- import functions and variables into our notebooks and scripts 
   |- config.py                         <- special paths and variables used across the project
   |- setup.py                          <- file for the custom Python package (called standby_project)
|- README.md
|- data/
   |- raw/
   |- processed/
   |- cleaned/
|- scripts/ ??
   |- script1.py
   |- script2.py
   |- archive/
      |- no-longer-useful.py
|- models
   |- baseline_model.py
   |- final_model.py
|- brainstorming
   |- baseline_model.md
   |- final_model.md

```

- - -
structure is based on "How to organize your Python data science project
" by [Eric Ma](https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510#file-ds-project-organization-md) and [Cookiecutter Data Science
](http://drivendata.github.io/cookiecutter-data-science/).

more info: https://github.com/SaundaryaB/Forecasting-Resources-Requirement/blob/master/final.ipynb
- - -

 ### aim
 Help the HR department with planning to estimate the amount of daily standby rescue drivers via a prediction model more efficiently. Here, efficient means that the percentage of standbys being activated is higher than in the current approach of keeping 90 drivers on hold. It also means that situations with not enough standbys should occur less often than in the current approach. Note that the plan must be finished on the 15th of the current month for the upcoming month.

 ### steps:
 1, Structure the project via the CRISP-DM or Team DS methodologies and give a recommendation of how a git repository for the project could look like.
 
 2, Assess the quality of the provided data set. Prepare and visualize your findings of the initial data analysis in order that business stakeholders can understand them in a clear and easy way.
 
 3, Provide a baseline model as well as an accurate predictive model, which fulfils business requirements, i.e. increase credit card success rate and keep fees low.
 
 4, In order that the business places confidence in your model, discuss the importance of the individual features and make the results of the model interpretable. Moreover, a sophisticated error analysis is very important for the business to understand the drawbacks of your approach.
 
 5, give a proposal of how your model could be used by the business in everyday work, for instance, via a graphical user interface (GUI).


### column description
 – date: entry date
 – n_sick: number of drivers called sick on duty
 – calls: number of emergency calls 
 – n_duty: number of drivers on duty available
 – n_sby: number of standby resources available
 – sby_need: number of standbys, which are activated on a given day
 – dafted: number of additional drivers needed due to not enough standbys


 ### additional info
 As colleagues from the planning claim, there are seasonal patterns - for instance, during winter months more rescue drivers call sick – which are not incorporated into the current approach. Moreover, sometimes there are not enough rescue drivers even when all 90 standby-bys are activated, so that drivers are called for work even on their days off.

 Business claims, that having a daily fixed number of standbys (n_sby = 90) is not efficient because there are days with too many standbys followed by days with not enough standbys. The business aims at a more dynamical standby allocation, which takes seasonal patterns into account.
 The model should minimize dates with not enough standby drivers at hand!