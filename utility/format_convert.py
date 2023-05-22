from model.boundary import Boundary


def table_to_xml(tablename, tableschema, connection):
    column_list = []
    filename = 'usappxml/' + tablename + '.xml'
    message = '<' + tablename + '>\n'

    outfile = open("Boundary", 'w')
    cursor = connection.cursor()

    cursor.execute("SELECT column_name from information_schema.columns where table_name = '%s'" % tablename + "and table_schema = '%s'" % tableschema )
    # cursor.execute('''SELECT table_to_xml('public."Boundary"', true, false, '')''')
    columns = cursor.fetchall()
    print(columns)

    for column in columns:
        column_list.append(column[0])
        print(len((column_list)))

    # cursor.execute("select * from  %s" % tablename)
    cursor.execute('''select * from public."Boundary"''')
    rows = cursor.fetchall()
    print (rows)

    outfile.write('<?xml version="1.0" ?>\n')
    outfile.write(message)

    for row in rows:
        outfile.write('  <row>\n')
        for i in range(len(column_list)):
            outfile.write('    <%s>%s</%s>\n' % (column_list[i], row[i], column_list[i]))
            outfile.write('    <%s>%s</%s>\n' % (column_list[i], row[i], column_list[i]))
            outfile.write('  </row>\n')

    outfile.write(message)

    outfile.close()
    return True
