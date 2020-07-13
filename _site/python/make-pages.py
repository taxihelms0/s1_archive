import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if '.txt' in f:
        # do something
        # change infileName and year for different files.
        infileName = f
        year = infileName.strip('.txt')
        with open(infileName, "r") as inFile:
            
            data = inFile.readlines()

            for line in data:
                words = line.split()
                if words:
                ############# FORMAT DATE ############
                    date = words[0].split('/')
                    month = date[0]
                    if len(month) > 1:
                        monthString = "{}"
                    else: 
                        monthString = "0{}"
                    monthString = monthString.format(month)
                    # print monthString
                    try:
                        day = date[1]
                    except:
                        print("error processing", words)
                        return 1
                    if len(day) > 1:
                        dayString = "{}"
                    else: 
                        dayString = "0{}"
                    dayString = dayString.format(day)
                    # print dayString
                    # filename format == year-mo-da-title-sep-by-dashes.md
                    dateString = "{}-{}-{}" 
                    dateString = dateString.format(year,monthString,dayString)
                    # print dateString
                ################ FORMAT TITLE #################
                    # len(words-1)
                    title = ""
                    for word in words:
                        if word != words[0]:
                            title += word
                        if word != words[len(words)-1]:
                            title += " "
                    ############## remove illegal chars and add .md extension
                    title = title.replace('w/', 'with')
                    title = title.replace('"', '')
                    title = title.replace('/', '')
                    title = title.replace(':', '')
                    title = title.replace('&', ' ')
                    # title = title.replace('---', '-')
                    fileName = dateString + title.replace(' ', '-') + ".md"
                    fileName = fileName.replace(',', '')
                    title = title.strip(' ')
                    print(title)
                    try:
                        outFile = open(fileName, "a")
                    except:
                        print("could not open", fileName)
                    try:
                        outFile.write("---")
                        outFile.write("\ntitle: ")
                        outFile.write(title)
                        outFile.write("\ndate: ")
                        outFile.write(dateString)
                        outFile.write("\n---")
                    except:
                        print("could not write", fileName)
                    try:
                        outFile.close()
                    except:
                        print("could not close", fileName)
        inFile.close()
