# Project Step 3

Team name: Rock Doves

# Task 8 (4 points):

*Some of the attributes may be redundant or irrelevant. How do you plan to preprocess the 2 training sets in 3 ways that are thoughtful and reasonable for this problem? In your pdf state clearly in your own words what each kind of preprocessing does and why you think it would be effective.*  
*(150 word minimum)*

First, we plan to drop **SEQN**, **SDDSRVYR**, **RIDSTATR** and **HIQ032B-D-F-H-I**. This first one is an assigned numerical identifier that doesn’t give any useful information to our model. The second two are identical across all features in our data set, so we cannot learn anything from them. The last five are non-mutually exclusive answers to the same question, but are missing so many instances that it’s hard to imagine them being useful. **INDFMMPC** and **INQ300** are repeats of other features and can be dropped. Finally, **WTINT2YR** and **WTMEC2YR** are population weights and the model doesn’t need to see them.

Next, we should convert categorical data to numerical. We will do this using 1-hot encoding (splitting the feature into several Boolean features to record a categorical value as a number without implying a numerical relationship) for the features that do not have any clear numerical ranking of their categories: **RIAGENDR, RIDRETH1, DMQMILIZ, DMDBORN4, DMDMARTZ, INQ300, HIQ210, HIQ032A, HIQ011, ALQ151,** and **ALQ111**.

We will use ordinal encoding (converting the feature to an integer while preserving the order of the ranking of categories) for **IND310, INDFMMPC, ALQ170, ALQ130, DMDEDUC2,** and **DMDYRUSR**. These features are already in an ordinal format, but with placeholders (implausible values) used to indicate missing answers, and occasional values out of order. We must therefore remove these placeholders, fix the order, and then scale them to match the scale of our 1-hot values so that they do not get undue weight for larger numbers.

Some features like **RIDAGEYR** are numerical but capped. Luckily, we are given the average of the capped bin and can replace all capped values with that average to keep our distribution similar to the sample. We must also scale these values.

Finally, since we have missing values in most of our features, we must impute. We can use a “most common” imputation strategy (replace each missing value with the most common value) for our categorical features, while our numerical features can be replaced with the average value. This should be done before the other processing listed above.

We cannot say on the face of it whether any features will be relevant to only cholesterol or only blood pressure. We will process the data the same way for both features (though obviously excluding the target values, which we handle by converting them to categorical values as required), and rely on the model to learn which are relevant for each one.

402 words

 

# Task 9 (3 points):

*Identify 3 metrics you plan to use to evaluate the performance of the 3 algorithms you chose in Task 7\. In your pdf state clearly in your own words what each hyperparameter does, why you chose it, and how you are going to find values for it.*  
*(150 word minimum)*

We plan to use F1 (macro), accuracy, and recall as our metrics. Recall is particularly important because, for predicting potentially serious but easily testable medical conditions like high blood pressure and high cholesterol, sensitivity is more important than accuracy and false negatives should be avoided at all cost. F1 makes sure that we are not ignoring precision, and accuracy will help us compare models.

## BP

We intend to use AdaBoost, SVC, and SGD as our models for blood pressure, because they performed best on the tests in Step 2 between the two of us, and thus have great potential for hyperparameter tuning. Hyperparameters we intend to tune include the various regularization parameters for all models, kernel type for SVC, type and number of predictors in the AdaBoost ensemble, and step size schedule and the underlying model (loss type) for SGD. We intend to use a grid search cross validation to find effective values for these hyperparameters.

The SVC Kernel is a transformation of the hypothesis space into a higher dimension, the shape of which allows non-linearly separable data to be classified by our support vector machine. Different types of transformations will produce different results. Cross validation will help ensure that we do not overfit to the training data.

AdaBoost is an ensemble learner, and the constituent learners can be various types (generally simple ones, to reduce computational complexity), and their number can be changed. We will try fewer more sophisticated models vs more simpler models to see where the best performance lies. The learning rate parameter decides how much weight each classifier will have, and will be grouped together with the number of classifiers (not grid searched with it) as there is an inherent trade-off between these values.

Step size in SGD can allow it to learn much faster (in this case allowing it to get closer to the optimum in the limited number of steps we’ll have to train it) but can impede learning if set too high. We will grid search different step size scheduling functions (different methods of choosing and changing the step size, which ideally is decreased when approaching a minimum). The loss type parameter for SGD determines which type of model is trained.  

## CHOL

For CHOL, we’ll tune three different models. We plan to use DecisionTreeClassifier, KNeighborsClassifier, and RandomForestClassifier. 

We plan to use DecisionTreeClassifier because it’s an interpretable multiclass model that can reveal to us which features separate the normal, borderline, and high categories. We plan to tune the following hyperparameters:  max\_depth, min\_samples\_leaf, and min\_samples\_split (regularization; controls complexity and prevents overfitting, especially on rare categories).

We plan to also use KNeighborsClassifier because it’s a local, instance-based method that can work well if similar survey/measurement profiles correspond with similar cholesterol categories. Distance-weighting might also help minority classes. We plan to tune the following hyperparameters: n\_neighbors, weights (“uniform” and “distance” can help with the aforementioned minority-class votes), and metric. 

We also choose to use RandomForestClassifier because it’s a variance-reduced tree ensemble that’s typically more stable than a single tree on noisy coded features. Using RandomForestClassifier, we can also improve minority-class recall with proper regularization and weighting. Hyperparameters we’ll tune include n\_estimators, max\_features, min\_samples\_leaf, and class\_weight. 

We also use these three models because they performed best out of both our plans on the held-out data on Gradescope for CHOL (in step 2).

(555 words)

# Task 10 (6 points): 

*In your pdf describe your learning scheme, that is, how you intend to design your training and testing to see if those algorithms, with that preprocessing and parameter tuning, are actually effective as measured by those metrics.*

Our training scheme will be as follows:

* We’ll follow the preprocessing from Task 8\.  
* Then we’ll use our metrics to tune the hyperparameters listed in Task 9, followed by model training.   
* For practical reasons, the number of training iterations and size of the grid search area might be smaller for cholesterol, because it has three categories (while blood pressure is binary), and will therefore be more computationally expensive to train the classifiers on.  
* We will also compare a dummy classifier to create a baseline for model performance and report on the same metrics.  
* We’ll also perform ANOVA to see if any of the model performances across CV folds exceed it on any metrics.  
* After selecting the best pipeline per target, we’ll fit it once on the full training set and evaluate on the (unseen) test set.

(136 words)