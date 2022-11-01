import csv 

# files to loop through to extract data
files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
output = 'pink_morsel_sales.csv'

# create output file

line_count = 0

def create_output(data, sale):
    with open(output, mode='w', newline="") as csv_file_w:
        fieldnames = ['Sales', 'Date', 'Region']
        writer = csv.DictWriter(csv_file_w, fieldnames=fieldnames)
        if line_count == 0:
            writer.writeheader()     
        else:
            writer.writerow({'Sales': sale, 'Date': row['date'], 'Region': row['region']})
        csv_file_w.close()
       


# for file in files:
    # open csv file 
with open('daily_sales_data_0.csv', mode='r') as csv_file_r:
    csv_reader = csv.DictReader(csv_file_r)
    for row in csv_reader:
        # export any product that is called pink morsel to dictionary
        if row['product'] == 'pink morsel':
            print(row)
            sale = round(float(row['price'].replace('$', "")) * int(row['quantity']), 2)
            create_output(row, sale)
            line_count += 1





# add selected items to a separate csv file incl. all columns


# create columns sales, dates, region


# price * quantity = sales 