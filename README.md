# Cooking Up A Storm

[Introduction](#introduction) | [Running the App](#running-the-app) | [Approach](#approach) | [Challenges](#challenges) | [Limitations](#limitations) | [Try to Beat Us](#try-to-beat-us)

## Introduction

This repo is our Makers Academy practice final project. For this week, working in teams, Makers students are given free reign to build **something** in one week. Cooking Up A Storm is an application built using Python, Ruby, jQuery (JavaScript), HTML, and CSS. It allows a user to input a series of ingredients, and receive a suggestion of the most suitable cuisine to cook with those ingredients. Using the current model, our algorithm has an accuracy of approximately 77%. This application was built using the dataset from Kaggle's [What's Cooking](https://www.kaggle.com/c/whats-cooking/data) challenge.


## Running the App

To run the application, clone or fork this repo and install its dependencies by running `bundle install`. If you do not have Bundler, you can install it from [here](http://bundler.io/). Then, run `rackup` and visit the correct port on the local server. With Sinatra, this is http://localhost:9292 by default.


## Approach

When we began this project, we knew nothing other than that we wanted to complete *some project* using machine learning. The starting point for this was to find a suitable dataset for the project. For this, we used Kaggle and simply browsed through until we found a dataset that we could use to solve some real-world problem that was achievable within the confines of the week that we had to complete this project. After settling on the *What's cooking* dataset, we had to learn how to work in Python, and paired on FizzBuzz to learn some of the basics of the language. An example of this can be seen [here](https://github.com/peterwdj/fizzbuzz_python).

After learning these basics, our approach to this challenge was simply to dive in with Python and various machine learning libraries built for the language, such as [scikit-learn](http://scikit-learn.org/stable/), and get our hands dirty with the language and the data. This entailed us identifying the defining features of the problem we were dealing with (a single-label, multi-class classification problem) in order to find suitable algorithms, and also led us to clean the dataset (see below).

After finding a suitable algorithm for our appliAccomplishing tasks in a memory-efficient waycation, the next step was to build a server and interface. Given the limits of this challenge, we opted to use Sinatra, a familiar technology to all of us, to create our application. jQuery UI is used on the front-end in order to auto-suggest ingredients to the user as they are typed.

## Challenges

This project brought with it several challenges, including:
 - Learning either Python or R
 - Learning to handle large datasets
 - Cleaning the data and finding the right parameters to use for each technique
 - Considering the computational efficiency of different tasks

As mentioned above, we paired on FizzBuzz and learned by doing in order to gain comfortability with Python. Much the same held true for learning how to handle large datasets, as we used tools from libraries such as [scikit-learn](http://scikit-learn.org/stable/) and [pandas](https://pandas.pydata.org/) to manipulate and change the data.

One of the problems we ran into when doing so was the fact that our dataset was muddied, with ingredients including brand names, or items such as '50% fat cheese' - an item not meaningfully different from 'cheese'. We took two approaches to tackle this issue. The first was to remove any instances of ingredients mentioned below a certain threshold (the 'limit'), dismissing them as statistically insignificant. The second technique we used was to make use of [NLTK](http://www.nltk.org/) to remove all words from ingredients that were not either singular or plural nouns, again below a certain threshold (the 'convert').

Armed with these two techniques, we needed to establish the optimal parameters for the convert and the limit. To do so, we wrote a short script that would take in parameters for the algorithm, and ranges for the limit and convert, and cycle through each combination of these parameters, and then return the best performing set of parameters. However, this is a computationally intensive task, and could take hours to run, depending on the algorithm and ranges for both the limit and the convert, making exhaustive tests impractical. The optimal parameters we found were a limit of 0, and a convert of 40 - which is the parameters for the dataset the current algorithm is trained on.


## Limitations

 The current implementation of this app has a few limitations. For example, the algorithm takes into account quantities of ingredients used to classify by cuisine. This means that the application works well with full ingredient sets, but for partial ingredient sets, results can be skewed. In addition to this, there also seems to be a bias regarding the size of the dataset for each cuisine, skewing results to cuisines such as Italian, which have more entries than cuisines such as Brazilian. For example, inputting just 'sake', a distinctly Japanese ingredient, often returns a guess of Italian, a cuisine which tends to have shorter ingredient lists. Any future implementations of this application should take these limitations into account and attempt to resolve them


## Try to Beat Us

Given the limited time we had to complete this project, it is unlikely that our results are the best they could be. Our current model, a [Logistic Regression](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) model trained on a convert of 40 and a limit of 0, has an accuracy score of 77.37%.

To attempt to beat us, you will first need to select a suitable machine learning algorithm to use. [Scikit Learn](http://scikit-learn.org/stable/index.html) might be a good place to start. Once you have selected an algorithm, import the function into `source/looper.py` at the top of the file in a format that will look something like this: `from sklearn.linear_model import LogisticRegression`. Then pass this in, with brackets, as an argument to `l = Looper()` on line 105.

You will then need to establish the optimum set of parameters for the limit and the convert (see above). You can do this with the looper file, which will cycle through the given algorithm with different values for the limit and the convert, and return the best performing parameters. This can be done by running `source/looper.py` in the command line. You can specify two arguments, `limit` and `convert`. For either of these, specify three values, separated by commas. These values will be, in order, the lower limit, the upper limit, and the step, for the given argument. If either argument is not given, these values will default to 0, 101, and 10 respectively. The command will look something like the following:

`python3 source/looper.py limit=30,60,5 convert=30,60,5`

This command will return the best-performing combination of parameters from the given values. If it is higher than 0.7736643620364551, then congratulations - you've beaten us!

To run this script, you will need to have [Python](https://www.python.org/), [Pandas](https://pandas.pydata.org/getpandas.html), and [Scikit Learn](http://scikit-learn.org/stable/install.html) installed. N.b. Running `source/looper.py` is a memory-intensive task. It is **strongly recommended** to run this script initially with high step values and a broad range, before narrowing down to find optimal parameters.

Once you have found the best set of values for your algorithm, to integrate it into the application you will need to recreate your dataset and retrain your model. This can be done in a single command in the command line. Run `python3 source/training.py` in the command line. Specify `limit=X` and `convert=Y` in your arguments, substituting X and Y for the best-performing values returned by `looper.py`. The full command will look something like the following:

`python3 source/training.py limit=42 convert=127`

Congratulations! You have just beaten us at our own game. Go forth, and cook some delicious food. 


Cooking Up A Storm was built by [Andrew](https://github.com/ajdavey8), [Ignacio](https://github.com/IPbianco), [Peter](https://github.com/peterwdj), and [Theo](https://github.com/somemarsupials).
