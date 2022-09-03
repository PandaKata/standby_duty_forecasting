# Task: Automation of Standby Duty Planning for Rescue Drivers via a Forecasting Model

This project is the final result of my course "Model Engineering" in the third semester of my master studies (Data Science).

The task was to find a way to redesign the deployment planning of the standby drivers of the Berlin Red Cross. Currently, the ambulance service operates in such a way that 90 standby drivers are on duty at any given time. This method does not always make sense, since most of the time none are needed and on other days several 100. We want to address this problem using a supervised regression algorithm.  

However, this project is not just about minimizing costs, but also about reducing the days when there are not enough drivers on duty and increasing the percentage of standby drivers activated. With the data currently available, there are 48 days where not enough standby drivers were scheduled. And on average only slightly more than 50 percent were activated. My goal wasto exceed this baseline.

### structure

```

|- notebooks/
   |- EDA.ipynb                         <- exploratory data analysis
   |- Baseline.ipynb                    <- baseline model
   |- final_model.ipynb                 <- final prediction model
|- grafics
|- sickness_table.csv                   <- data
|- roster2.csv                          <- table with final roster

```

