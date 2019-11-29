from api.models import db, Person, Email
from api.core import create_response, serialize_list, logger
import csv


def reader(filename):
    fields = []
    rows = []

    # reading csv file
    with open(filename, "r") as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))

    # printing the field names
    print("Field names are:" + ", ".join(field for field in fields))

    #  printing first 3 rows
    print("\nFirst 3 rows are:\n")
    for row in rows[:3]:
        # parsing each column of a row
        for col in row:
            print("%10s" % col),
        print("\n")


def writer(header, data, filename, option):
    with open(filename, "w", newline="") as csvfile:
        if option == "write":
            movies = csv.writer(csvfile)
            movies.writerow(header)
            for x in data:
                movies.writerow(x)
        elif option == "update":
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
        else:
            print("Option is not known")

    # create SQLAlchemy Objects
    new_person = Person(name=data["name"])
    email = Email(email=data["email"])
    new_person.emails.append(email)

    # commit it to database
    db.session.add_all([new_person, email])
    db.session.commit()
    return create_response(
        message=f"Successfully created person {new_person.name} with id: {new_person._id}"
    )


def updater(filename):
    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]
        # print(readData)
        readData[0]["Age"] = "16"
        # print(readData)

    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, "update")
