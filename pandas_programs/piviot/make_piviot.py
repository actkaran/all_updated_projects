import pandas as pd

df = pd.read_excel("Comp_Data_Report_20241107.xlsx", sheet_name="Comp Report 1 - Value Players")
print("dataframe loaded...")
main_pivot = pd.pivot_table(
    data=df,                   # Your input DataFrame
    index=['Comp', 'Sag'],     # Creates nested index with Company and Sag
    values=[                   # Columns you want to analyze
        'FSN Title',
        'LP PI @Fk mix',
        'FSP PI @ FK Mix',
        'LP PI @Nielsen Mix',
        'Avg PI'
    ],
    margins=True,
    dropna=False,
    margins_name="Grand Total", # Rename the margin column name
    aggfunc={                  # Define how to aggregate each column
        'FSN Title': 'count',  # Count number of titles
        'LP PI @Fk mix': 'sum',        # Sum these values
        'FSP PI @ FK Mix': 'sum',
        'LP PI @Nielsen Mix': 'sum',
        'Avg PI': 'sum'
    }
).round(2)  # Round all numbers to 2 decimal places

# Renaming the columns
main_pivot.columns = [
    'Count of FSN Title',
    'Sum of FK PI @ FK MIX',
    'Sum of FK FSP PI @ FK MIX',
    'Sum of NPI',
    'Sum of Avg PI'
]


# def export_pivot_with_subtotals(pivot_table, filename):
with pd.ExcelWriter("demo1.xlsx", engine='xlsxwriter') as writer:
    # Write to Excel with subtotals
    pivot_table_with_totals = main_pivot.copy()
    # pivot_table_with_totals.loc['Grand Total'] = main_pivot.sum()

    pivot_table_with_totals.to_excel(
        writer,
        sheet_name='Analyzed data'
    )

    # Get worksheet object
    worksheet = writer.sheets['Analyzed data']
    workbook = writer.book

    # Add formats
    total_format = workbook.add_format({
        'bold': True,
        'bg_color': '#FFA07A',
        'border': 1
    })

    # Format total row
    # last_row = len(pivot_table_with_totals.index)
    # for col in range(len(pivot_table_with_totals.columns) + 1):
    #     worksheet.write(last_row, col, pivot_table_with_totals.iloc[-1, col - 1] if col > 0 else 'Grand Total',
    #                     total_format)


print("file generated...")