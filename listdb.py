import sqlite3

def htmlModuleRes(text,name):
    p = text.find(name)+len(name)
    return text[p:text.find('\n',p)]

def listdb(db,table,tables,url):
    f = open('listdb_modules.html','r')
    htmlModules = f.read()
    f.close()
    f = open('listdb.html','r')
    html = f.read()
    f.close()
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("""SELECT * FROM ?"""+(table,))
    row = c.fetchone()
    htmlTable=""
    while row!=None:
        htmlRow=""
        for i in row:
            htmlRow += htmlModuleRes(htmlModules,'[#TableElement#]').replace('[#Name#]',str(i))
        htmlTable += htmlModuleRes(htmlModules,'[#TableRow#]').replace('[#TableElements#]',htmlRow)
        row = c.fetchone()
    htmlMenu = ""
    for i in tables:
        if i == table:
            htmlMenu += htmlModuleRes(htmlModules,'[#ActiveTable#]').replace('[#Name#]',i)
        else:
            htmlMenu += htmlModuleRes(htmlModules,'[#Table#]').replace('[#Name#]',i).replace('[#URL#]',url+i)
    return html.replace('[#TableBody#]',htmlTable).replace('[#TableName#]',table).replace('[#TableList#]',htmlMenu)
