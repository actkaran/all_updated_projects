import win32com.client as win32

def clear_pts(ws):
    try:
        # Clear existing pivot tables in the given worksheet
        for pt in ws.PivotTables():
            pt.TableRange2.Clear()
    except Exception as e:
        print(f"Error clearing pivot tables: {e}")

def insert_pt_field_set1(pt):
    try:
        # Insert row fields
        pt.PivotFields("Comp").Orientation = 1  # xlRowField
        pt.PivotFields("Comp").Position = 1

        pt.PivotFields("Sag").Orientation = 1  # xlRowField
        pt.PivotFields("Sag").Position = 2

        # Insert values field
        pt.AddDataField(pt.PivotFields("FSN Title"), "Count of FSN Title", -4112)  # xlSum
        pt.PivotFields("Count of FSN Title").NumberFormat = "#,##0"

        pt.AddDataField(pt.PivotFields("Avg PI"), "Average of Avg PI", -4106)  # xlAverage
        pt.PivotFields("Average of Avg PI").NumberFormat = "$#,##0"
    except Exception as e:
        print(f"Error inserting pivot table fields: {e}")

# Construct the Excel application object
xlApp = win32.Dispatch('Excel.Application')
xlApp.Visible = True

# Create workbook and worksheet references
wb = xlApp.Workbooks.Open("demo2.xlsx")
ws_data = wb.Worksheets("PivotTable")
ws_report = wb.Worksheets("Output")

# Clear pivot tables on the Report tab
clear_pts(ws_report)

# Create pivot table cache
pt_cache = wb.PivotCaches().Create(SourceType=win32.constants.xlDatabase, SourceData=ws_data.UsedRange)

# Create pivot table
pt = pt_cache.CreatePivotTable(TableDestination=ws_report.Range("A1"), TableName="test_pivot")

# Toggle grand totals
pt.ColumnGrand = True
pt.RowGrand = False

# Set subtotal location
pt.SubtotalLocation = 2  # xlAtBottom

# Set the report layout to Tabular
pt.RowAxisLayout(1)  # xlTabularRow

# Update the table style
pt.TableStyle2 = "PivotStyleMedium9"

# Insert field set
insert_pt_field_set1(pt)

# Wrap up by adjusting column widths
ws_report.Columns("D:E").ColumnWidth = 35

# Save the workbook
wb.Save()