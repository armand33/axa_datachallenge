import date as dg
import codecs

def date_to_timestamp():
    with codecs.open("data/submission_original.txt",'r', encoding='utf-8') as original:
        out = codecs.open("data/submission.txt", 'w', encoding="utf-8")
        first_line = True
        for line in original:
            if first_line:
                first_line = False
                out.write(line)
                continue
            line = line.split("\t")
            out.write(str(dg.date_to_timestamp(line[0]))+"\t"+line[1]+'\t'+line[2])
        out.close()

def timestamp_to_date():
    with codecs.open("data/submission_tmp.txt",'r', encoding='utf-8') as original:
        out = codecs.open("data/submission_final.txt", 'w', encoding="utf-8")
        first_line = True
        for line in original:
            line = line.split("\n")[0]
            if first_line:
                first_line = False
                out.write(line+"\n")
                continue
            line = line.split("\t")
            out.write(str(dg.timestamp_to_date(int(line[0])))+"\t"+line[1]+'\t'+str(int(1.6*float(line[2])))+"\n")
        out.close()

if __name__ == "__main__":
    #date_to_timestamp()
    #timestamp_to_date()
    pass
