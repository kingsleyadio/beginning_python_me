import walkfile
from zipfile import ZipFile as zipf
from zipfile import ZIP_DEFLATED
def zip():
    fl=zipf('e:\\adikstools\\wf.zip', 'w', ZIP_DEFLATED)
    b='e:\\adikstools\\mysmsbackup\\'
    wal=walkfile.Walk()
    list=wal.walk(b)
    for i in list:
        fl.write(i)
    fl.close()
    print 'completed'
    
if __name__=='__main__':
    zip()