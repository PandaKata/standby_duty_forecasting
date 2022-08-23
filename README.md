
 # Task: Automation of Standby Duty Planning for Rescue Drivers via a Forecasting Model

### structure


```bash
$ pwd
/Users/kata/Desktop/GitHub/credit_card_routing
$ ls
|- notebooks/
   |- EDA.ipynb                         <- exploratory data analysis
   |- feature_engineering.ipynb         <- create new columns, encode, etc.
   |- archive/  
      |- no-longer-useful.ipynb
|- standby_project/                     <- all things refactored out of notebooks
   |- __init__.py                       <- import functions and variables 
   |- config.py                         <- special paths and variables used across the project
   |- setup.py                          <- file for the custom Python package
|- README.md                            <- top-level README for all developers
|- data/
   |- raw/                              <- raw data
   |- feature_engineered/               <- data with encoded variables, new columns, etc.
|- src/ 
   |- archive/
      |- no-longer-useful.py   
   |- models                            <- scripts to train models
      |- baseline_model.py              <- evaluates baseline
      |- intermediate_model.py          <- predicts calls
      |- final_model.py                 <- predicts final sby_need
|- brainstorming                        <- space for ideas that do not fit anywhere else
   |- intermediate_model.md 
   |- final_model.md

```

- - -
structure is based on "How to organize your Python data science project
" by [Eric Ma](https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510#file-ds-project-organization-md) and [Cookiecutter Data Science
](http://drivendata.github.io/cookiecutter-data-science/).

more info: https://github.com/SaundaryaB/Forecasting-Resources-Requirement/blob/master/final.ipynb
- - -
