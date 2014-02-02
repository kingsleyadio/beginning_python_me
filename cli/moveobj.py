import shutil1 as sh
import os

def move(src, dst):
    def __pwrmov(src, dst):
        try:
            try:
                os.chmod(src, ~0)
                sh.move(src, dst)
                return 1
            except IOError:
                fd=dst+'\\'+os.path.basename(src)
                if os.path.isfile(fd):
                    os.chmod(fd, ~0)
                    os.remove(fd)
                return 0
            except sh.Error:
                os.chmod(src, ~0)
                if os.path.isfile(src):
                    os.chmod(dst+'\\'+os.path.basename(src), ~0)
                    os.remove(dst+'\\'+os.path.basename(src))
                    sh.move(src, dst)
                    return 1
                li=os.listdir(src)
                if not li:
                    os.chmod(src, ~0)
                    os.rmdir(src)
                    return 1
                for i in li:
                    a=src+'\\'+i
                    b=dst+'\\'+os.path.basename(src)
                    os.chmod(a, ~0)
                    if not os.path.exists(b+'\\'+i):
                        sh.move(a, b)
                    else:
                        __pwrmov(a, b)
                try:
                    os.chmod(src, ~0)
                    os.rmdir(src)
                except: raise
                return 1
            except:
                return 0
        except IOError:
            f=b+'\\'+os.path.basename(a)
            if os.path.isfile(f):
                os.chmod(f, ~0)
                os.remove(f)
            return 0
        except:
            return 0
            
    try:
        sh.move(src, dst)
        print 'successful'
    except IOError:
        fd=dst+'\\'+os.path.basename(src)
        if os.path.isfile(fd):
            os.chmod(fd, ~0)
            os.remove(fd)
        print 'cant move'
    except:
        print 'tryin power move'
        if __pwrmov(src, dst):
            print 'success'
        else:
            print 'cant move'