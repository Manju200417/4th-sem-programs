#11. Create Data Frame from Excel sheet using Pandas and Perform Operations on Data Frames 
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "name": ["Manju", "Vinayk", "Chetan"],
    "age": [21, 22, 23],
})
# data to Excel file
df.to_excel("demo.xlsx", index=False)

# Read the Excel file
print(pd.read_excel("demo.xlsx"))


































# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     "age": [20, 21, 19, 22, 20],
#     "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
#     "is_student": [True, False, True, False, True],
#     "height_cm": [165, 175, 180, 170, 160],
#     "weight_kg": [55, 75, 65, 80, 50]
# }
# try:
#     print(pd.DataFrame(data))
# except Exception as e:
#     print(f"Error: {e}")
# # df.to_html("sample_data.html",index=True)



# -------------------------------------------------------
#reading excel file with Pandas
# -------------------------------------------------------

# xl = pd.read_excel("sample_data.xlsx")

# print(pd.DataFrame(xl))

# -------------------------------------------------------

# user dada to pandas DataFrame
# -------------------------------------------------------
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     "age": [20, 21, 19, 22, 20],
# }

# print(pd.DataFrame(data))


# -------------------------------------------------------

# creating EXCEL file with Pandas       ====> we need one Module called "openpyxl" to read and write Excel files
# ------------------------------------------------------
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25, 30, 35, 45, 60],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# }

# df = pd.DataFrame(data)

# # Save to Excel file
# df.to_excel("sample_data.xlsx", index=False)
# -------------------------------------------------------