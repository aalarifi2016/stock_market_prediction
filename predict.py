# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
data = pd.read_csv('all-data.csv',  names=['sentiment', 'article'])


# %%
data


# %%
import scikit-learn


# %%
from sklearn.linear_model import LinearRegression


# %%
predictor = LinearRegression(n_jobs=-1)


# %%
data_set = pd.read_csv('all-data.csv', names=['sentiment', 'news'])


# %%
data_set.temp


# %%
y = data_set.sentiment


# %%
y


# %%
x = data_set.news
x


# %%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=4, stratify=y)


# %%
from sklearn.model_selection import train_test_split


# %%
x_train


# %%
from sklearn.linear_model import LinearRegression


# %%
model = LinearRegression().fit(x_train, y_train)


# %%
web.DataReader


# %%
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics


# %%
data_folder = 'dataset/'
dataset = load_files(data_folder, shuffle=False)
print("n_samples: %d" % len(dataset.data))


# %%
docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.25, random_state=None)


# %%
pipeline = Pipeline([('vect', TfidfVectorizer(min_df=3, max_df=0.95)),('clf', LinearSVC(C=1000)),])


# %%
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],}


# %%
grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1)


# %%
grid_search.fit(docs_train, y_train)


# %%



# %%
n_candidates = len(grid_search.cv_results_['params'])
for i in range(n_candidates):
    print(i, 'params - %s; mean - %0.2f; std - %0.2f' % (grid_search.cv_results_['params'][i],
                grid_search.cv_results_['mean_test_score'][i],
                grid_search.cv_results_['std_test_score'][i]))


# %%
count = 1
for index, row in df.iterrows():
    with open(f'dataset/positive/{str(count)}.txt', 'w') as f:
        f.write(row['news'])
    count += 1
    


# %%
y_predicted = grid_search.predict(docs_test)


# %%
y_test


# %%
y_predicted


# %%
print(metrics.classification_report(y_test, y_predicted, target_names=dataset.target_names))


# %%
cm = metrics.confusion_matrix(y_test, y_predicted)
print(cm)


# %%
import matplotlib.pyplot as plt
plt.matshow(cm)    # 
plt.show()


# %%



