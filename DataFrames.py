import pandas as pd

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

df1 = pd.DataFrame(x)
x = df1[["ID"]]

print(x)

z = df1[['Department','Salary','ID']]
print(z)

students = {"Student": ["Aaron", "Derek", "Emily", "Evangeline"], 
            "Country": ["US", "UK", "Canada", "UAE"],
            "Course": ["Profiling", "Kicking doors down", "Slaying", "Delusionaling"],
            "Marks": ["100", "89", "92", "95"]}

df = pd.DataFrame(students)
print(df)

grades = df[["Marks"]]
print(grades)

c = df[["Country", "Course"]]
print(c)

print(df.iloc[0:2, 0:3])
print(df.loc[0:2, "Student":"Course"])