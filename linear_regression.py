import pandas as pd;
import matplotlib.pyplot as plt;
import collections
import statsmodels.api as sm;

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

headers = ['Amount.Requested', 'Amount.Funded.By.Investors', 'Interest.Rate', 'Loan.Length', 'Loan.Purpose', 'Debt.To.Income.Ratio', 'State', 'Home.Ownership', 'Monthly.Income', 'FICO.Range', 'Open.CREDIT.Lines', 'Revolving.CREDIT.Balance', 'Inquiries.in.the.Last.6.Months', 'Employment.Length']

loan_length = loansData['Loan.Length'];

interest_iter = loansData['Interest.Rate'].iteritems();
interest_map = map(lambda x: x[1].replace('%', '', ), interest_iter)
loansData.loc[:, 'Interest.Rate'] = pd.Series(interest_map, loansData.index)

length_iter = loan_length.iteritems();
length_map = map(lambda x : int(x[1].split(' ')[0]), length_iter);
print 'Length_map:'
loansData.loc[:, 'Loan.Length'] = pd.Series(length_map, loansData.index)

FICO = loansData['FICO.Range'];
fico_iter = FICO.iteritems()
y = map(lambda x : int(x[1].split('-')[0]), fico_iter);
print y;

loansData.loc[:, 'FICO.Score'] = pd.Series(y, loansData.index);
print loansData.loc[:, 'FICO.Score'];
print loansData['Interest.Rate'];
print FICO.index[0];
print length_map;


loan_length_cleaned = loansData['Loan.Length'];
interest_rate_cleaned = loansData['Interest.Rate']
FICO_score_cleaned = loansData['FICO.Score']

FICO_score_cleaned.hist();

count = collections.Counter(FICO_score_cleaned)
print count;
#
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

#plt.show();

#you can just map on colums direclty
F = FICO.map(lambda x : 'toots');
print F;

print len(loansData.values[0])
print len(list(loansData));







#.index is going to give you a list of the index labels
