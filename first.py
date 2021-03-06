# import pandas as pd
import pandas as pd
 
# list of strings
lst = [['abc',22,1500],['bac',34,3000],['cab',40,2500],['bca',55,3600],['cab',48,3500],['bca',55,4000],['xyz',28,1506],['bax',39,3003],['caz',49,2507],['bcy',55,3500],
['cyb',56,3508],['ick',45,2390],['abc',39,1509],['bgc',39,3070],['eab',41,2565],['bka',54,3160],['cab',48,3514],['lbc',21,1506],['yac',34,3004],['aab',45,2506],
['bya',55,3600],['iab',38,3500],['bca',35,4000],['gyz',28,1506],['bex',36,3903],['kaz',48,2207],['bcy',55,3100],['alc',26,1420],['zac',34,3009],['bab',60,2508],
['cby',56,3508],['bik',35,2390],['abc',29,1509],['bag',39,3070],['bae',44,2550],['bck',59,3360],['cab',48,3210],['abl',29,1700],['cac',34,3035],['kab',30,2700],
['lyb',54,3548],['iok',45,2390],['ahc',39,1509],['bmc',39,3050],['kab',41,2525],['jka',54,1160],['tab',48,3510],['lbc',29,1506],['yic',34,3004],['aob',45,2506],
['bga',51,2300],['ilb',38,3500],['bja',35,4000],['myz',28,1546],['blx',36,3993],['klz',48,2647],['kcy',55,3105],['alc',36,1420],['zkc',34,3009],['bmb',60,2508],
['cby',55,3808],['blk',35,2390],['ybc',29,1509],['bam',39,3080],['cue',54,2520],['buk',59,3260],['clb',48,3211],['abl',49,1700],['cjc',34,3035],['kay',30,2700],
['lyb',54,3548],['iok',45,2390],['ahc',39,1509],['amc',39,3050],['kab',21,2525],['joa',51,1160],['tab',48,2510],['lbc',39,1506],['yic',34,3204],['aub',43,2506],
['bga',51,2300],['ilb',38,3500],['bja',35,4000],['byz',28,1546],['blx',26,3993],['olz',45,2647],['kcy',55,2105],['alc',26,1420],['zkc',34,3029],['blb',26,2508],
['cby',55,3808],['blk',35,2390],['ybc',29,1509],['cam',39,3080],['cue',44,2520],['blk',59,3260],['clb',48,1211],['abl',59,1700],['cjc',34,3075],['kvy',32,2701]]
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst, columns=['Name', 'Age', 'Salary'])
df.index = df.index + 1
data = df.loc[(df['Salary'] > 3000)]
print("People getting salary greater than 3000.........")
print(data)
print("Mean Age............")
avg = data['Age'].mean()
print(avg)
#print(df)

