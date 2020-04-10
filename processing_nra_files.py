import csv
import sys
import os.path



years = [2020]
months = [2]
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
site_list = []

#this will become a for loop later to roll through a bunch of dates
vehicle_cat_count_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
traffic_count_dict = []
def file_namer(year,month,day):
    if day >= 10:
        file_name = f'nra_docs/per-site-class-aggr-{year}-0{month}-{day}.csv'
    else:
        file_name = f'nra_docs/per-site-class-aggr-{year}-0{month}-0{day}.csv'
    return file_name
for year in years:
    for month in months:
        
        for day in days:
            vehicle_cat_count_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
            file_name = file_namer(year,month,day)
            if os.path.exists(file_name):
                with open(file_name) as nrafile:
                    csvrader = csv.reader(nrafile)
                    next(nrafile)
                    num_sites = 0
                    for row in csv.reader(nrafile):

                        category = int(row[1])
                        vehicle_cat_count_dict[category] += int(row[5])
                        num_sites += 1
                        if int(row[0]) not in site_list:
                            site_list.append(int(row[0]))
                    if num_sites == 0:
                        break
                    #print(vehicle_cat_count_dict)
                   
                    
                    date = day,month,year
                    print(day, month, year)
                    print(vehicle_cat_count_dict)
                    date_list = []
                    category_list = []
                    vehicle_count_list = []
                    index = 0
                    
                    



                    for item in vehicle_cat_count_dict:
                       
                        traffic_count_dict.append({"day": day, "month": month, "year" : year, "category" : index ,"number of vehicles" : vehicle_cat_count_dict[index],"number of sites" : len(site_list) })
                        index +=1
                        csv_file = f'nra_docs/nra_output/result_aggregated_csv_files.csv'
csv_columns = ["day","month","year","category","number of vehicles","number of sites"]
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for day in traffic_count_dict:
        writer.writerow(day)
print(site_list)