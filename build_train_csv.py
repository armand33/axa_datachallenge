import os
import codecs
import date as dg
import pandas as pd
import datetime

def generate_line(timestamp, ass_assignment, calls : int = 0):
    line = dg.timestamp_to_date(timestamp)
    hour = int(line.split(" ")[1].split(":")[0])
    month = int(line.split(" ")[0].split("-")[1])
    week_day = datetime.datetime.fromtimestamp(timestamp).strftime('%A')
    if (week_day == "Monday"):
        if month == 1:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 2:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 3:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 4:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 5:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 6:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 7:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 8:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;"+ass_assignment+"\n"
        if month == 9:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;"+ass_assignment+"\n"
        if month == 10:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;"+ass_assignment+"\n"
        if month == 11:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;"+ass_assignment+"\n"
        if month == 12:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;"+ass_assignment+"\n"
    if (week_day == "Tuesday"):
        if month == 1:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 2:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 3:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 4:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 5:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 6:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 7:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 8:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;"+ass_assignment+"\n"
        if month == 9:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;"+ass_assignment+"\n"
        if month == 10:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;"+ass_assignment+"\n"
        if month == 11:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;"+ass_assignment+"\n"
        if month == 12:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;"+ass_assignment+"\n"
    if (week_day == "Wednesday"):
        if month == 1:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 2:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 3:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 4:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 5:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 6:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 7:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 8:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;"+ass_assignment+"\n"
        if month == 9:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;"+ass_assignment+"\n"
        if month == 10:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;"+ass_assignment+"\n"
        if month == 11:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;"+ass_assignment+"\n"
        if month == 12:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;"+ass_assignment+"\n"
    if (week_day == "Thursday"):
        if month == 1:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 2:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 3:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 4:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 5:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;0;0;0;1;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 6:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;0;0;0;0;1;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 7:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;0;0;0;0;0;1;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 8:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;0;0;0;0;0;0;1;0;0;0;0;"+ass_assignment+"\n"
        if month == 9:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;1;0;0;0;"+ass_assignment+"\n"
        if month == 10:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;1;0;0;"+ass_assignment+"\n"
        if month == 11:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;1;0;"+ass_assignment+"\n"
        if month == 12:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;"+ass_assignment+"\n"
    if (week_day == "Friday"):
        if month == 1:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;1;0;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 2:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;1;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 3:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;0;1;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 4:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;0;0;1;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 5:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;0;0;0;1;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 6:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;0;0;0;0;1;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 7:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;0;0;0;0;0;1;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 8:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;0;0;0;0;0;0;1;0;0;0;0;"+ass_assignment+"\n"
        if month == 9:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;1;0;0;0;"+ass_assignment+"\n"
        if month == 10:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;1;0;0;"+ass_assignment+"\n"
        if month == 11:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;1;0;"+ass_assignment+"\n"
        if month == 12:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;0;1;"+ass_assignment+"\n"
    if (week_day == "Saturday"):
        if month == 1:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;1;0;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 2:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;1;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 3:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;0;1;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 4:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;0;0;1;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 5:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;0;0;0;1;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 6:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;0;0;0;0;1;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 7:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;0;0;0;0;0;1;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 8:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;0;0;0;0;0;0;1;0;0;0;0;"+ass_assignment+"\n"
        if month == 9:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;1;0;0;0;"+ass_assignment+"\n"
        if month == 10:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;1;0;0;"+ass_assignment+"\n"
        if month == 11:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;1;0;"+ass_assignment+"\n"
        if month == 12:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;0;1;"+ass_assignment+"\n"
    if (week_day == "Sunday"):
        if month == 1:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;1;0;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 2:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;1;0;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 3:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;0;1;0;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 4:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;0;0;1;0;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 5:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;0;0;0;1;0;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 6:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;0;0;0;0;1;0;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 7:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;0;0;0;0;0;1;0;0;0;0;0;"+ass_assignment+"\n"
        if month == 8:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;0;0;0;0;0;0;1;0;0;0;0;"+ass_assignment+"\n"
        if month == 9:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;1;0;0;0;"+ass_assignment+"\n"
        if month == 10:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;1;0;0;"+ass_assignment+"\n"
        if month == 11:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;1;0;"+ass_assignment+"\n"
        if month == 12:
            out_line = str(timestamp)+";"+str(calls)+";"+str(hour)+";0;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;0;0;1;"+ass_assignment+"\n"

    return out_line


def run():

    relevant_centers = ["CAT","CMS","Crises","Domicile","Gestion","Gestion - Accueil Telephonique",
                        "Gestion Assurances","Gestion Clients","Gestion_DZ","Gestion Relation Clienteles",
                        "Gestion Renault","Japon","Manager","Médical","Mécanicien","Nuit","Prestataires",
                        "RENAULT","Regulation Medicale","RTC","SAP","Services","Tech. Axa","Tech. Inter",
                        "Tech. Total","Téléphonie"]

    with codecs.open("data/train_2011_2012_2013.csv", "r", encoding='utf-8') as in_file:

        out = codecs.open('data/train.csv', 'w', encoding='utf-8')

        first_line = True

        line_counter = 0
        total_lines = 10878471

        print("Done: 0 lines", end="")

        for line in in_file:
            if line_counter % 1000 == 0:
                print("\rDone: {}/{} ({}%) lines".format(line_counter, total_lines,
                                                         int(line_counter / total_lines * 100)), end="")

            line = line.split('\n')[0]

            if first_line:
                line = line.split(";")
                out.write(line[0]+";"+line[81]+";Hour;Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday;January;February;March;April;May;June;July;August;September;October;November;December;"+line[12]+"\n")
                first_line = False
                line_counter += 1
                continue

            line = line.split(";")
            if line[12] in relevant_centers:
                timestamp = int(dg.date_to_timestamp(line[0]))
                out_line = generate_line(timestamp, line[12], int(line[81]))
                out.write(out_line)
            line_counter += 1

        print("\rDone: {}/{} ({}%) lines".format(line_counter, total_lines, int(line_counter / total_lines * 100)))

    out.close()

    #file = pd.read_csv('data/train.csv', sep = ';')
    #file.sort_values('DATE',inplace=True)
    #file.to_csv("data/train_sorted.csv", sep=";", encoding = 'utf-8', index=False)

if __name__ == "__main__":
    run()
