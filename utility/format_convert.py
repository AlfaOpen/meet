from numpy.core.setup_common import file


def table_to_xml(tablename, connection):
    column_list = []
    filename = 'usappxml/' + tablename + '.xml'
    message = '<' + tablename + '>\n'

    outfile = file(filename, 'w')
    cursor = connection.cursor()

    cursor.execute("SELECT column_name from information_schema.columns where table_name = '%s'" % tablename)
    columns = cursor.fetchall()

    for column in columns:
        column_list.append(column[0])

    cursor.execute("select * from  %s" % tablename)
    rows = cursor.fetchall()

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
