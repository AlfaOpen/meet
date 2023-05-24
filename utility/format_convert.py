from model.boundary import Boundary
from model.boundary_info import BoundaryInfo
from model.composition_part import CompositionPart
from model.faults import Faults
from model.faults_all3d import FaultsAll3d
from model.faults_shp import FaultsShp
from model.geologic_unit import GeologicUnit
from model.geological_event import GeologicalEvent
from model.isoline import Isoline
from model.isoline_info import IsolineInfo



def table_to_xml(tablename, tableschema, connection):
    column_list = []
    filename = tablename + '.xml'
    message_open = '<' + tablename + '>\n'
    message_close = '</' + tablename + '>\n'

    outfile = open(filename, 'w')
    cursor = connection.cursor()

    cursor.execute(
        "SELECT column_name from information_schema.columns where table_name = '%s'" % tablename + "and table_schema = '%s'" % tableschema)
    # cursor.execute('''SELECT table_to_xml('public."Boundary"', true, false, '')''')
    columns = cursor.fetchall()
    print(columns)

    for column in columns:
        column_list.append(column[0])
        print(len(column_list))

    # cursor.execute("select * from  %s" % tablename)
    cursor.execute('''select * from public."FaultsAll3d"''')
    rows = cursor.fetchall()
    print(rows)

    outfile.write('<?xml version="1.0" ?>\n')
    outfile.write(message_open)
    k = 1

    for row in rows:
        outfile.write('  <row' + str(k) + '>\n')
        for i in range(len(column_list)):
            outfile.write('    <%s>%s</%s>\n' % (column_list[i], row[i], column_list[i]))
            # outfile  .write('    <%s>%s</%s>\n' % (column_list[i], row[i], column_list[i]))
        outfile.write('</row' + str(k) + '>\n')
        k = k + 1

    outfile.write(message_close)

    outfile.close()
    return True
