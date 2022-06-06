import csv

# simple get matrix 
# file(str) name of the csvfile to be read
# search(list) given search, it will look for columns 
# # with the exact same string and put it in the matrix
def get_matrix(file,search):
    
    colval = []
    with open(file) as f:
        f_reader = csv.reader(f, delimiter=',')
        ncol = len(next(f_reader))
        f.seek(0)
        for row in f_reader: #find where things we want to search are
            i = 0
            while i < ncol:
                j = 0
                while j < len(search):
                    if row[i] == search[j]:
                        colval.append(i)
                    j += 1
                i += 1
                if len(search) == len(colval):
                    break
            break
        data = [[]] 
        count = 0
        
        for row in f_reader:
            i = 0
            list = []
            while i < len(colval):
                list.append(row[colval[i]])
                i += 1
            data.append(list)
            count += 1
        data.pop(0)
    return data

# simple write to csvfile function
# filename(str) is the name of the file to be written to (will be overwritten) default is 'dailyboardchange.csv'
# head(list) the words to be written to the top
# data(matrix) the data to write to the file
def write_to_csvfile(head, data, filename = 'dailyboardchange.csv'):
    with open(filename, 'w', newline='') as daily:
        writer = csv.writer(daily, delimiter=',')
        writer.writerow(head) #write header (fieldnames)
        
        for rows in data:
            writer.writerow(rows)
    daily.close()
    return
