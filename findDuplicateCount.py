# %%
import csv

def incident_count():
  
  list = []
  # Input filename
  input_filename = 'incident.csv'
  with open(input_filename, 'r') as csv_file:
      csv_read=csv.reader(csv_file, delimiter=',')
      for row in csv_read:
        list.append(', '.join(row))

  counts = {}
  for i in list:
    counts[i] = counts.get(i, 0) + 1
    
  return counts


def generate_csv_report():
    
    # assign header columns 
    headerList = ['Hostname','Count']  
    '''
      Assigning Header directly to the csv in key,value is not possible
      as I have to open a csv again just to add Header in it.
      It's possible with DictWriter and writerows.
    '''
  
    # Output filename
    output_filename = "output_incident.csv" 
    # open CSV file and assign header 
    with open(output_filename, 'w', newline='') as file: 
        add_header = csv.DictWriter(file, delimiter=',', fieldnames=headerList) 
        add_header.writeheader()
        
    # Save extracted data to a CSV file
    count_in_csv = incident_count()
  
    with open(output_filename, 'a+', newline='') as outfile:
      csv_writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      for k,v in count_in_csv.items():
        csv_writer.writerow([k] + [v])
        
    return ''      


def main():
    incident_count()
    generate_csv_report()
 

if __name__ == "__main__":
    main()    
