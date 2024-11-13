import pandas as pd

df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02'],
    'Product': ['A', 'B', 'A'],
    'Sales': [100, 200, 150]
})

basic_pivot = pd.pivot_table(
    data=df,
    values="Sales",
    index="Product",
    margins=True,
    aggfunc=["sum", "mean", "count"]
)
basic_pivot.columns = ["Total sales", "Average Sales", "Total product sold"]
basic_pivot.to_excel("basic_pivot.xlsx",engine='openpyxl')
print("file generated...")


'''
Basic principle of pivot table---------------
values => this means # what to analyze.
aggfunc => this means #how to analyze.
index = > this means # Rows of the pivot table. (what to show)(whom data's is calculated) 
'''
#--------------------------------------------------------------------------------------------
'''
Additionaly--------
columns (this is the parameter that we can pass in the pivot_table)
(But what this means?)=> this creates a extra row above the 'index' represented column.
with it's values.
suppose i add declare 'columns="Date"' than above the product one new row added..
like 
code:
basic_pivot = pd.pivot_table(
    data=df,
    values="Sales",
    index="Product",
    columns="Date",
    aggfunc={"Sales":"sum"}
)
output:
    Date     2024-01-01  2024-01-02
    Product                        
    A             100.0       150.0
    B             200.0         NaN
    
    
without 'columns'
code:
basic_pivot = pd.pivot_table(
    data=df,
    values="Sales",
    index=["Product", "Date"],
    aggfunc={"Sales":"sum"}
)
output:
                        Sales
    Product Date             
    A       2024-01-01    100
            2024-01-02    150
    B       2024-01-01    200
'''
#------------------------------------------------------------------------------------------

'''
Multiple functions....
you can pass multiple functions into 'aggfunc' whether you want to apply that functions on same data or,
for different data you want to apply different function.
code:
    basic_pivot = pd.pivot_table(
        data=df,
        values="Sales",
        index="Product",
        aggfunc=["sum", "mean", "count"]
    )
    basic_pivot.columns = ["Total sales", "Average Sales", "Total product sold"]
    print(basic_pivot)

output:
         Total sales  Average Sales  Total product sold
Product                                                
A                250          125.0                   2
B                200          200.0                   1
'''
#----------------------------------------------------------------------
'''
Margin:
if margins=True => this will return total of each columns that is presented..
code:
    basic_pivot = pd.pivot_table(
        data=df,
        values="Sales",
        index="Product",
        margins=True,
        aggfunc=["sum", "mean", "count"]
    )
    basic_pivot.columns = ["Total sales", "Average Sales", "Total product sold"]
    print(basic_pivot)
output:
         Total sales  Average Sales  Total product sold
Product                                                
A                250          125.0                   2
B                200          200.0                   1
All              450          150.0                   3
'''