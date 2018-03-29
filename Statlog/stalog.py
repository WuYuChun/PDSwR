import csv
import pandas as pd


df = pd.read_table('german.data.txt',header=None,delim_whitespace=True)
df.rename(index = int,columns={0:'Status.of.existing.checking.account',
                               1:'Duration.in.month',
                               2:'Credit.history',
                               3:'Purpose',
                               4: 'Credit.amount',
                               5:'Savings.account.bonds',
                               6:'Present.employment.since',
                               7:'Installment.rate.in.percentage.of.disposable.income',
                               8:'Personal.status.and.sex',
                               9:'Other.debtors.guarantors',
                               10:'Present.residence.since',
                               11: 'Property',
                               12:'Age.in.years',
                               13:'Other.installment.plans',
                               14:'Housing',
                               15:'Number.of.existing.credits.at.this.bank',
                               16:'Job',
                               17:'Number.of.people.being.liable.to.provide.maintenance.for',
                               18:'Telephone',
                               19: 'foreign.worker',
                               20:'Good.Loan'},inplace=True)

df.replace( ['A11', 'A12', 'A13', 'A14', 'A30', 'A31', 'A32', 'A33', 'A34', 'A40', 'A41', 'A42'
, 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49', 'A410', 'A61', 'A62', 'A63'
, 'A64', 'A65', 'A71', 'A72', 'A73', 'A74', 'A75', 'A91', 'A92', 'A93', 'A94', 'A95', 'A101', 'A102', 'A103', 'A121'
, 'A122', 'A123', 'A124', 'A141', 'A142', 'A143', 'A151', 'A152', 'A153', 'A171', 'A172', 'A173', 'A174', 'A191'
, 'A192', 'A201'
, 'A202' ],['... < 0 DM','0 <= ... < 200 DM','... >= 200 DM / salary assignments for at least 1 year',
 'no checking account',
 'no credits taken/all credits paid back duly',
 'all credits at this bank paid back duly',
 'existing credits paid back duly till now',
 'delay in paying off in the past',
 'critical account/other credits existing (not at this bank)',
 'car (new)',
 'car (used)',
 'furniture/equipment',
 'radio/television',
 'domestic appliances',
 'repairs',
 'education',
 '(vacation - does not exist?)',
 'retraining',
 'business',
 'others',
 '... < 100 DM',
 '100 <= ... < 500 DM',
 '500 <= ... < 1000 DM',
 '.. >= 1000 DM',
 'unknown/ no savings account',
 'unemployed',
 '... < 1 year',
 '1 <= ... < 4 years',
 '4 <= ... < 7 years',
 '.. >= 7 years',
 'male : divorced/separated',
 'female : divorced/separated/married',
 'male : single',
 'male : married/widowed',
 'female : single',
 'none',
 'co-applicant',
 'guarantor',
 'real estate',
 'if not A121 : building society savings agreement/life insurance',
 'if not A121/A122 : car or other, not in attribute 6',
 'unknown / no property',
 'bank',
 'stores',
 'none',
 'rent',
 'own',
 'for free',
 'unemployed/ unskilled - non-resident',
 'unskilled - resident',
 'skilled employee / official',
 'management/ self-employed/highly qualified employee/ officer',
 'none',
 'yes, registered under the customers name',
 'yes',
 'no'                                                                  ],inplace=True)

print(df['Purpose'].value_counts())

groub1 = df.groupby(['Purpose','Good.Loan'])
print(groub1.size())


###################这个是下面的输出############################
# radio/television       280
# car (new)              234
# furniture/equipment    181
# car (used)             103
# business                97
# education               50
# repairs                 22
# domestic appliances     12
# others                  12
# retraining               9
# Name: Purpose, dtype: int64
# Purpose              Good.Loan
# business             1             63
#                      2             34
# car (new)            1            145
#                      2             89
# car (used)           1             86
#                      2             17
# domestic appliances  1              8
#                      2              4
# education            1             28
#                      2             22
# furniture/equipment  1            123
#                      2             58
# others               1              7
#                      2              5
# radio/television     1            218
#                      2             62
# repairs              1             14
#                      2              8
# retraining           1              8
#                      2              1
# dtype: int64