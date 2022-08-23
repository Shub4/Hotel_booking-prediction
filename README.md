## Part 1

Q. Write a regex to extract all the numbers with orange color background from the below text in italics.

A. * pattern=r":(\d*)(}|,)"
   * result=re.findall(pattern, text)


## Part 2

Q. Train a machine learning model (preferably with a neural network) that 
predicts the customer who is going to be checked in. Once done, please test 
the prediction. Host/Deploy the results using any hosting service you want (streamlit/flask) 


A. Steps followed:
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

   6. Creating Interface using HTML and CSS.

   7. Creating App using Flask.

   8. Creating Git Repository, including Procfile, requirements.txt, app.py, and other dependencies.

   9. Connecting Git with Heroku and Deploying Master Branch.  
      https://hotel-booking-pred00.herokuapp.com/

      (*Model Deployed succeed in Heroku but app is not responding, trying to solve the issue, however it is working perfectly on local vpn)


## Part 3

Q. Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution).

A. I have changed my tech to Data Science and has no relevant industry exposure to real time challenges, since I am looking for an opportunity to start my career and working hard to achieve it. I have done lots of Projects and case studies given by companies and found that I have a good logical thinking. One Project which I would say challenges me is the NLP project on Fake News Detection, working with text data made me learn new things and solving issues related to its deployment has made me more confident towards real time projects. 


Q. Explain back propagation and tell us how you handle a dataset if 4 out of 30 parameters have null values more than 40 percentage.

A. 1. * BackProp is one of the several ways in which ANN can be trained. It is a supervised training scheme, which means, it learns form labeled training data (there is a supervisor to guide its learning).
      * In simple terms, BackProp is like "Learning from mistakes". The supervisor corrects ANN whenevr it makes mistakes.
      * Initially all the weights are randomly assigned. For every input in the training dataset, the ANN is activated and its output is observed. This output is compared with the desired output that we already know, and the error is propogated back to the previous layer. This error is noted and the weights are adjusted accordingly. This process is repeated untill the error is below predetermined threshold.

   2. * Since only 4 parameters out of 30 having more than 40% null values, so rows cannot be dropped, if the parameters contains 60-70% null values then columns can be dropped.
      * We can check the dependencies of parameters with each other using missingno module in python and categorize the features as MCAR, MNAR or MAR. We can work accordingly with Imputaion methods for the columns(like mean/median/mode replacement, frequent category imputation, Arbitrary Imputation, Random sample Imputation etc.)
      * We can use ML model which are robust to null values like knn, RandomForest, GradientBoosting etc.



      


