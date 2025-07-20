import pandas as pd

#Sample data
df = pd.DataFrame({
    'Name' : ['Anna','Ben','Clara'],
    'Score' : [72,48,91]
})

# Add a "Results" column, Pass if Score >=50
df['Results'] = df['Score'].apply(lambda x : "Pass" if x >=50 else "Fail")

#Add "Bonus" column = Score *0.1
df['Bonus'] = df['Score']*0.1

#Map names to students IDs
df['ID'] = df['Name'].map({'Anna':101,'Ben':102,'Clara':103})

print(df)