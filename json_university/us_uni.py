import dns.resolver
import csv
import sys


Outlook = 0
Gmail = 0
Others = 0
NA = 0
progress = 0
limit = int(sys.argv[1])

csv_reader = csv.reader(open("./us_uni_list.csv"))
mxlist = []
for line in csv_reader:
    mxlist.append(line[0])
    if len(mxlist) == limit:
        break

for web in mxlist:
    dnslist = []
    try:
        answers = dns.resolver.resolve(web, 'MX')
        for rdata in answers:
            dnslist.append(str(rdata.exchange))
    except dns.exception.Timeout as a:
        print('dns.exception.Timeout:', a)
        dnslist.append("NoAnswer")
    except dns.resolver.NoAnswer as b:
        print('dns.resolver.NoAnswer:', b)
        dnslist.append("NoAnswer")
    except dns.resolver.NXDOMAIN as c:
        print('dns.resolver.NXDOMAIN:', c)
        dnslist.append("NoAnswer")
    except Exception as d:
        print('UnkonwnError:', d)
        dnslist.append("NoAnswer")

    if "google" in dnslist[0]:
        Gmail = Gmail + 1
    elif "outlook" in dnslist[0]:
        Outlook = Outlook + 1
    elif "NoAnswer" in dnslist[0]:
        NA = NA + 1
    else:
        Others = Others + 1
    progress = progress + 1
    print(Gmail, Outlook, Others, NA, "    ({}/{})".format(progress, limit), "{}%".format(round(progress/limit,5)*100))
print("Gmail: ", Gmail, "\nOutlook: ", Outlook, "\nOthers: ", Others, "\nN/A: ", NA)