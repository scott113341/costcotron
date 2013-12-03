class person:
    def __init__(self, name):
        self.name = name
        self.owed = 0.0
        self.unique_items = []


def costcotron(filename):
    matt = person('matt')
    scott = person('scott')
    ryan = person('ryan')
    ian = person('ian')
    gavin = person('gavin')

    peeps = [matt, scott, ryan, ian, gavin]

    # python magic
    with open(filename) as f:
        report = []
        for line in f:
            item = line.split('/')
            count = int(item[0])
            i_name = item[1]
            price = float(item[2])
            payees = item[3:]

            if payees[0] == 'all\n':
                report.append(item)
                for p in peeps:
                    p.owed += count * price / float(len(peeps))
            else:
                for payee in payees:
                    for p in peeps:
                        if p.name + '\n' == payee or p.name == payee:
                            p.owed += count * price / len(payees)
                            titem = item
                            titem[2] = count * price / len(payees)
                            p.unique_items.append(titem)

    # ugly formatting jank
    f = open(filename[:-2] + 'out', 'w')
    f.write("COSTCO REPORT\n")
    f.write("_____________\n\n")
    f.write("Matt\t\tScott\t\tRyan\t\tIan\t\t\tGavin\n")
    price_line = ''
    for p in peeps:
        price_line += '$%.2f\t\t' % p.owed
    f.write(price_line)
    f.write('\n\n\nALL Items\n')
    f.write('__________\n\n')
    for l in report:
        f.write("x%s %s @ $%s" % (l[0], l[1], l[2]))
        if int(l[0]) > 1:
            f.write(" each\n")
        else:
            f.write("\n")

    f.write("\n\n\nINDIVIDUAL Breakdown\n")
    f.write("++++++++++++++++++++\n")
    for p in peeps:
        if p.unique_items:
            f.write("\n\n%s\n______\n\n" % p.name.upper())
            for i in p.unique_items:
                f.write("x%s %s @ $%.2f" % (i[0], i[1], i[2]))
                if int(i[0]) > 1:
                    f.write(" each\n")
                else:
                    f.write("\n")

print ('HELP: The input file should be separated by newlines and be of the format: ' +
      'numberofitems/itemname/price/nameofpersontopay/nameofpersontopay2 etc... ' +
      'or just numberofitems/item name/price/all if everyone is splitting the cost.\n')
filename = raw_input("Enter the costco file to be slurped: ")
costcotron(filename)
