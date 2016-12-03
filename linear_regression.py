import pandas as pd;
import matplotlib.pyplot as plt;
import collections
import statsmodels.api as sm;
import numpy as np;

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

headers = ['Amount.Requested', 'Amount.Funded.By.Investors', 'Interest.Rate', 'Loan.Length', 'Loan.Purpose', 'Debt.To.Income.Ratio', 'State', 'Home.Ownership', 'Monthly.Income', 'FICO.Range', 'Open.CREDIT.Lines', 'Revolving.CREDIT.Balance', 'Inquiries.in.the.Last.6.Months', 'Employment.Length']

loan_length = loansData['Loan.Length'];

interest_iter = loansData['Interest.Rate'].iteritems();
interest_map = map(lambda x: x[1].replace('%', '', ), interest_iter)
loansData.loc[:, 'Interest.Rate'] = pd.Series(interest_map, loansData.index)
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x : round(float(x) / 100.0, 4));

length_iter = loan_length.iteritems();
length_map = map(lambda x : int(x[1].split(' ')[0]), length_iter);
loansData.loc[:, 'Loan.Length'] = pd.Series(length_map, loansData.index)

FICO = loansData['FICO.Range'];
fico_iter = FICO.iteritems()
y = map(lambda x : int(x[1].split('-')[0]), fico_iter);
loansData.loc[:, 'FICO.Score'] = pd.Series(y, loansData.index);


loan_length_cleaned = loansData['Loan.Length'];
interest_rate_cleaned = loansData['Interest.Rate']
FICO_score_cleaned = loansData['FICO.Score']

#Histogram
#FICO_score_cleaned.hist();

#just a counter for fun
count = collections.Counter(FICO_score_cleaned)

#These scatter matrices are cool
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
# b = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

#plt.show();

# Column Headers
# print list(loansData);
# ['Amount.Requested', 'Amount.Funded.By.Investors', 'Interest.Rate', 'Loan.Length', 'Loan.Purpose', 'Debt.To.Income.Ratio', 'State', 'Home.Ownership', 'Monthly.Income', 'FICO.Range',
# 'Open.CREDIT.Lines', 'Revolving.CREDIT.Balance', 'Inquiries.in.the.Last.6.Months', 'Employment.Length', 'FICO.Score']
#.index is going to give you a list of the index labels


intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

#matrix makes a matrix object; it seems like columns form pandas are turned into a matrix with one row, n columns
#the tranpose will make an n X 1 matrix
y = np.matrix(intrate).transpose();
x1 = np.matrix(loanamt).transpose();
x2 = np.matrix(fico).transpose();

#will make a m x 2 matrix
x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
print f.summary()
