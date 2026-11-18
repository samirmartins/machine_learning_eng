# Machine Learning Applied to Engineering

Slides, notebooks, and assignments for an undergraduate Electrical Engineering course offered at the Federal University of São João del-Rei (UFSJ), taught by Samir A. M. Martins. The course covers mathematical foundations and Python applications in data analysis, classification, regression, dynamic system identification, and recommender systems.

[Syllabus](SYLLABUS.md) · [Lectures](#lectures) · [Applications](#applications-and-case-studies) · [Data](#data-and-execution) · [Assignments](#course-assignments)

## Lectures

| Lecture | Topics | Code | Slides |
| --- | --- | --- | --- |
| 01 | Introduction, basic Python, Anaconda, Jupyter, and Spyder | [Notebook](lesson_01_python_basics/code_lesson_01.ipynb) | [PDF](lesson_01_python_basics/lesson_01_ml.pdf) |
| 02 | Conda, pip, package installation, and environment export | - | [PDF](lesson_02_conda_environments/lesson_02_ml.pdf) |
| 03 | NumPy, Matplotlib, and Pandas | [NumPy](lesson_03_numpy_pandas_matplotlib/code_numpy.ipynb), [Pandas](lesson_03_numpy_pandas_matplotlib/code_pandas.ipynb), [Matplotlib](lesson_03_numpy_pandas_matplotlib/code_matplotlib.py) | [PDF](lesson_03_numpy_pandas_matplotlib/lesson_03_ml.pdf) |
| 04 | Descriptive statistics, correlation, probability, and Bayes' theorem | [Notebook](lesson_04_statistics_probability/statistics_probability.ipynb) | [PDF](lesson_04_statistics_probability/lesson_04_ml.pdf) |
| 05 | Files, data sources, and APIs | [Notebook and data - ZIP](lesson_05_data_with_python/lesson_05_data_with_python.zip) | [PDF](lesson_05_data_with_python/lesson_05_ml.pdf) |
| 06 | Modeling, underfitting/overfitting, bias/variance, and signal features | [Notebook](lesson_06_bias_variance/lesson_06_machine_learning.ipynb) | [PDF](lesson_06_bias_variance/lesson_06_ml.pdf) |
| 07 | Classification and classifier evaluation | [Notebook](lesson_07_classification/lesson_07_classification_techniques.ipynb) | [PDF](lesson_07_classification/lesson_07_ml.pdf) |
| 08 | Regression, residuals, and metrics | [Notebook](lesson_08_regression/lesson_08_regression_techniques.ipynb) | [PDF](lesson_08_regression/lesson_08_ml.pdf) |
| 09 | KNN, distances, scaling, and cross-validation | [Notebook](lesson_09_knn/lesson_09_knn_classification.ipynb) | [PDF](lesson_09_knn/lesson_09_ml.pdf) |
| 10 | Simple and multiple linear regression; time-series forecasting | [Notebook](lesson_10_linear_regression/lesson_10_linear_regression.ipynb) | [PDF](lesson_10_linear_regression/lesson_10_ml.pdf) |
| 11 | Logistic regression, class imbalance, and decision thresholds | [Notebook](lesson_11_logistic_regression/lesson_11_logistic_regression.ipynb) | [PDF](lesson_11_logistic_regression/lesson_11_ml.pdf) |
| 12 | Ridge, Lasso, Elastic Net, polynomial expansion, and temporal validation | [Notebook](lesson_12_regularized_regression/lesson_12_regularized_polynomial_regression.ipynb) | [PDF](lesson_12_regularized_regression/lesson_12_ml.pdf) |
| 13 | Decision trees, random forests, and SVM | [Notebook](lesson_13_trees_forests_svm/lesson_13_decision_trees_random_forests_svm.ipynb) | [PDF](lesson_13_trees_forests_svm/lesson_13_ml.pdf) |
| 14 | SysIdentPy: system identification, NARX, NAR, FROLS, and BIC | [Notebook](lesson_14_sysidentpy/lesson_14_sysidentpy.ipynb) | [PDF](lesson_14_sysidentpy/lesson_14_ml.pdf) |
| 15 | Recommender systems, collaborative filtering, and Precision@K | [Notebook](lesson_15_recommender_systems/lesson_15_recommender_systems.ipynb) | [PDF](lesson_15_recommender_systems/lesson_15_ml.pdf) |

## Applications and case studies

### External datasets

| Application and data | Approach | Lectures |
| --- | --- | --- |
| Electrical grid stability - simulations | KNN, trees, forests, and SVM; scaling, cross-validation for k, and metrics | [09](lesson_09_knn/lesson_09_knn_classification.ipynb), [13](lesson_13_trees_forests_svm/lesson_13_decision_trees_random_forests_svm.ipynb) |
| Combined-cycle power plant net output - operational measurements | Simple/multiple static regression, Ridge/Lasso/Elastic Net, and polynomial expansion; feature selection and metrics | [10](lesson_10_linear_regression/lesson_10_linear_regression.ipynb), [12](lesson_12_regularized_regression/lesson_12_regularized_polynomial_regression.ipynb) |
| Residential active power - measurements | Linear regression, lags, moving averages, and hour encoding; temporal split, one-step-ahead, and free-run prediction | [10](lesson_10_linear_regression/lesson_10_linear_regression.ipynb) |
| Predictive maintenance failures | Logistic regression and KNN; class imbalance and cost-based threshold selection on validation data | [11](lesson_11_logistic_regression/lesson_11_logistic_regression.ipynb) |
| Monthly airline passengers - historical time series | Regularized regression, lags, trend, and seasonality; time-series cross-validation, one-step-ahead, and free-run prediction | [12](lesson_12_regularized_regression/lesson_12_regularized_polynomial_regression.ipynb) |
| F-16 structural vibration - experimental | Polynomial NARX, FROLS/BIC, and free-run prediction | [14](lesson_14_sysidentpy/lesson_14_sysidentpy.ipynb) |
| DC motor-generator - experimental | NARX, scaling, FROLS/BIC, and free-run prediction | [14](lesson_14_sysidentpy/lesson_14_sysidentpy.ipynb) |
| Hospital demand in San Francisco | NAR, lags, BIC, and free-run prediction | [14](lesson_14_sysidentpy/lesson_14_sysidentpy.ipynb) |
| Movies - user ratings | Item-item collaborative filtering, cosine similarity in NumPy, popularity baseline, and offline Precision@K | [15](lesson_15_recommender_systems/lesson_15_recommender_systems.ipynb) |

### Synthetic examples

| Application | Concepts | Lectures |
| --- | --- | --- |
| Equipment and transformer load and temperature | Linear fit, residuals, polynomial Ridge, and random forest | [06](lesson_06_bias_variance/lesson_06_machine_learning.ipynb), [08](lesson_08_regression/lesson_08_regression_techniques.ipynb) |
| Noisy signal | Polynomial degree, underfitting/overfitting, and train/test error | [06](lesson_06_bias_variance/lesson_06_machine_learning.ipynb) |
| Normal/fault diagnosis | Constructed confusion matrix: accuracy, precision, recall, and F1; comparison with always predicting normal | [06](lesson_06_bias_variance/lesson_06_machine_learning.ipynb) |
| Normal and harmonic/noisy signals | RMS, crest factor, and THD using FFT | [06](lesson_06_bias_variance/lesson_06_machine_learning.ipynb) |
| Motor operating conditions | Logistic regression and KNN, decision boundaries, scaling, and cross-validation | [07](lesson_07_classification/lesson_07_classification_techniques.ipynb), [09](lesson_09_knn/lesson_09_knn_classification.ipynb) |
| Electrical resistance using Ohm's law | Regression without intercept, physical interpretation, and residuals | [10](lesson_10_linear_regression/lesson_10_linear_regression.ipynb) |
| Voltage deviation and load variation | RBF SVM and 2D decision boundary | [13](lesson_13_trees_forests_svm/lesson_13_decision_trees_random_forests_svm.ipynb) |

## Data and execution

The datasets used in the examples are available at the links below.

| Data | Sources and files |
| --- | --- |
| Electrical grid stability | [Electrical Grid Stability/UCI](https://archive.ics.uci.edu/dataset/471) |
| Combined-cycle power plant | [CCPP/UCI](https://archive.ics.uci.edu/dataset/294) |
| Residential power consumption | [Household Electric Power Consumption/UCI](https://archive.ics.uci.edu/dataset/235) |
| Predictive maintenance | [AI4I 2020/UCI](https://archive.ics.uci.edu/dataset/601) |
| Airline passengers | [AirPassengers/R](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/AirPassengers.html) · [CSV/Rdatasets](https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/AirPassengers.csv) |
| F-16 | [Original benchmark](https://www.nonlinearbenchmark.org/benchmarks/f-16-gvt) · [File/SysIdentPy](https://raw.githubusercontent.com/wilsonrljr/sysidentpy-data/refs/heads/main/datasets/f_16_vibration_test/f-16.txt) |
| DC motor-generator | [Experiment/SysIdentPy](https://sysidentpy.org/user-guide/tutorials/electromechanical-system-identification-overview/) · [Input](https://raw.githubusercontent.com/wilsonrljr/sysidentpy-data/refs/heads/main/datasets/generator/x_cc.csv) · [Output](https://raw.githubusercontent.com/wilsonrljr/sysidentpy-data/refs/heads/main/datasets/generator/y_cc.csv) |
| Hospital demand | [OpenEI/NREL](https://data.openei.org/submissions/153) · [Provenance via NeuralProphet/SysIdentPy](https://raw.githubusercontent.com/wilsonrljr/sysidentpy-data/main/data_sources.md) · [CSV](https://raw.githubusercontent.com/wilsonrljr/sysidentpy-data/refs/heads/main/datasets/san_francisco_hospital/SanFrancisco_Hospital.csv) |
| Movies | [MovieLens/GroupLens](https://grouplens.org/datasets/movielens/latest/) |
| Load curve | [ONS](https://dados.ons.org.br/dataset/curva-carga) |
| Generation capacity | [SIGA/ANEEL](https://dadosabertos.aneel.gov.br/dataset/siga-sistema-de-informacoes-de-geracao-da-aneel) |
| Brazilian states | [IBGE Locations API](https://servicodados.ibge.gov.br/api/docs/localidades) |
| Annualized Selic rate, 252-day basis | [SGS 1178/BCB](https://dadosabertos.bcb.gov.br/dataset/1178-taxa-de-juros---selic-anualizada-base-252) |

## Course assignments

| Assignment | Scope | Materials |
| --- | --- | --- |
| T1 - Real data analysis | Data acquisition and preparation in Python, exploratory/statistical analysis, plots, and proposal of an ML task | [Assignment](assignment1/assignment1_statement.ipynb) |
| T2 - Modeling and validation | Supervised continuation of T1: at least three models and three metrics, validation, and a technical paper | [Assignment](assignment2/assignment2_statement.pdf) · [LaTeX](assignment2/assignment2_latex/assignment2_machine_learning.tex) |

[Student project repositories - 2026/1 class](STUDENT_PROJECTS_2026_1.MD), listed by group and topic. Authorship remains with the respective groups.

## License

[BSD 3-Clause](LICENSE). Third-party data and materials remain subject to their respective terms.
