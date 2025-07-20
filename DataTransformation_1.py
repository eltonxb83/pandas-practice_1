import pandas as pd

data = {
    'Product' : ['Pen','Book','Laptop'],
    'Price' : [1.5, 12.0, 999.0],
    'Quantity' : [10,5,2]
}

df = pd.DataFrame(data)

# Add total column
df['total'] = df['Price']*df['Quantity']

#Add VAT colum (7%)
df['VAT'] = df['Price'].apply(lambda x : x*0.07)

#Add column to classify as expensive

df['Expensive'] = df['Price'].apply(lambda x : "Yes" if x > 100 else "No")

df['EXPENSIVE'] = df['Price']>100

print(df)
