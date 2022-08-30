## Part 1

Q. Write a regex to extract all the numbers with orange color background from the below text in italics.

A. Using regular exp pattern and findall
   * pattern=r":(\d*)(}|,)"
   * result=re.findall(pattern, text)
   
   code in regex.ipynb file


## Part 2

Q. Train a machine learning model (preferably with a neural network) that 
predicts the customer who is going to be checked in. Once done, please test 
the prediction. Host/Deploy the results using any hosting service you want (streamlit/flask) 


A. Steps followed: (code in hotel_bookings.ipynb file)
   1. Data Preprocessing
      * Null Value Check and handling.
      * Data Balance Check.
      * Handling Irregularities in Features.
      * Data Enrichment.

   2. Exploratory Data Analysis
   
   3. Working on Data
      * Dropping highly correlated Features.
      * Handling high cardinality in categorical features and one hot encoding.
      * Feature Selection.
      * Feature Scaling.
      * Splitting Dependent and Independent Feature.
   
   4. Model Selection and fitting.
   
   5. Prediction on test data and Metric Check.

   6. Creating Interface using HTML\CSS and App using Flask.

 




      


