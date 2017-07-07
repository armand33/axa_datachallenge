import date as dg
import codecs
import build_train_csv as bc
import change_submission_dates as change

def run():
    with codecs.open("data/submission.txt", 'r', encoding='utf-8') as sub:
        out = codecs.open("data/submission.csv", 'w', encoding="utf-8")
        first_line = True
        for line in sub:
            if first_line:
                line = line.split("\t")
                out.write(line[0]+";prediction;Hour;Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday;January;February;March;April;May;June;July;August;September;October;November;December;"+line[1]+"\n")
                first_line = False
                continue

            line = line.split('\t')
            out.write(bc.generate_line(int(line[0]), line[1]))
        out.close()

if __name__ == "__main__":
    change.date_to_timestamp()
    run()
