
 # Task: Credit Card Routing for Online Purchase via Predictive Modelling

### structure

$ pwd
/Users/kata/Desktop/GitHub/credit_card_routing

$ ls
|- notebooks/
   |- EDA.ipynb
   |- 02-second-logical-notebook.ipynb
   |- prototype-notebook.ipynb
   |- archive/
      |- no-longer-useful.ipynb
|- credt_card_routing_project/          <- all things refactored out of notebooks
   |- __init__.py                       <- import functions and variables into our notebooks and scripts 
   |- config.py                         <- special paths and variables used across the project
   |- setup.py                          <- file for the custom Python package (called credt_card_routing_project)
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
|- brainsorming



 ### aim
 Help the business to automate the credit card routing via a predictive model. Such a model should increase the payment success rate by finding the best possible PSP for each transaction and at the same time keep the transaction fees low.

 ### steps:
 1, Structure the project via the CRISP-DM or Team DS methodologies and give a recommendation of how a git repository for the project could look like.
 
 2, Assess the quality of the provided data set. Prepare and visualize your findings of the initial data analysis in order that business stakeholders can understand them in a clear and easy way.
 
 3, Provide a baseline model as well as an accurate predictive model, which fulfils business requirements, i.e. increase credit card success rate and keep fees low.
 
 4, In order that the business places confidence in your model, discuss the importance of the individual features and make the results of the model interpretable. Moreover, a sophisticated error analysis is very important for the business to understand the drawbacks of your approach.
 
 5, give a proposal of how your model could be used by the business in everyday work, for instance, via a graphical user interface (GUI).



 ### list of PSPs (=payments service providers) and service fees:

 | name      | fee_success | fee_failure |
 |-----------|-------------|-------------|
 | Moneycard | 5 Euro      | 2 Euro      |
 | Goldcard  | 10 Euro     | 5 Euro      |
 | UK_Card   | 3 Euro      | 1 Euro      |
 | Simplecard| 1 Euro      | 0.5 Euro    |



### column description
 – tmsp: timestamp of transaction
 – country: country of transaction
 – amount: transaction amount
 – success: is 1 if payment is successful
 – PSP: name of payments service provider
 – 3D_secured: is 1 if customer is 3D identified (i.e. more secure online credit card payments)
 – card: credit card provider (Master, Visa, Diners)


 ### additional info
 Many transactions fail at the first try. Therefore, customers try several times to transfer the money. If two transactions are within one minute, with the same amount of money and from the same country, it is (for a decent number of tries) safe to assume that they are payment attempts of the same purchase. Consider this possibility of several payment attempts of the same purchase in your machine learning model!
