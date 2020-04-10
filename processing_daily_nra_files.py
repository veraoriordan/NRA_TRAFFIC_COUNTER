import pandas as pd
import csv
import numpy as np

traffic_count_dict = []
for filenum in range(10,701):
    #change file_name to suit where you put the downloaded tfdayreport files
    file_name = f'nra_docs/nra_daily_files/tfdayreport ({filenum}).xls'
    
    with open(file_name) as f:
        f.readline()
        f.readline()
        f.readline()
        title_date = f.readline()
    #this is needed to access the time stamp
    	
    #print(title_date)
    #print(type(title_date))
    day = int(title_date[-11:-9])
    month = int(title_date[-14:-12])
    year = int(title_date[-20:-15])
    date = day,month,year

    data = pd.read_html(file_name, header = None)
 

    date_data = data[0]
    #print(date_data)
    vehicle_data_frame = data[6]
  
  
    #dictionary of categories - 0 = motorbike, 1 = car, 2 = lgv, 3 = bus, 4 = hgv_rig, 5 = hgv art, 6 = caravan 
    vehicle_cat_count_dict = {1:vehicle_data_frame.iat[0,2], 2:vehicle_data_frame.iat[0,4],3:vehicle_data_frame.iat[0,6],4:vehicle_data_frame.iat[0,8],
                                5:vehicle_data_frame.iat[0,10],6:vehicle_data_frame.iat[0,12],7:vehicle_data_frame.iat[0,14]}
    
    

    indexa = 1
    
    num_sites = 1
      
    for key,value in vehicle_cat_count_dict.items():
        try:                
            traffic_count_dict.append({"day": day, "month":month, "year": year , "category" : key ,"number of vehicles" : int(value) ,"number of sites" : num_sites })
            indexa +=1
        except ValueError:
            print("NaN value here - skip past this one")
            continue
    

    csv_file = f'nra_docs/nra_output/result_individual_daily_reports.csv'
    #this is the output file in my file directory, edit to what suits you.
    csv_columns = ["day","month", "year","category","number of vehicles","number of sites"]
    print(date)
    print(vehicle_cat_count_dict)
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        #uncomment the above line if you want a header on the file with the csv_column labels
        for day in traffic_count_dict:
            
            writer.writerow(day)
            



