import shutil1 as sh
import os, sys, e32

def docopy(src, dst):
    def __pwrcopy(src, dst):
        try:
            try:
                if os.path.isfile(src):
                    os.chmod(dst, ~0)
                    sh.copyfile(src, dst)
                    return 1
                else:
                    sh.copytree(src, dst)
                    return 1
            except IOError:
                if os.path.isfile(dst):
                    os.chmod(dst, ~0)
                    os.remove(dst)
                return 0
            except OSError:
                a=os.listdir(src)
                if len(a)==0 and os.path.exists(dst):
                    #os.rmdir(src)
                    return 1
                else:
                    for i in a:
                        d=src+'\\'+i
                        f=dst+'\\'+i
                        if not os.path.exists(f):
                            if os.path.isfile(d):
                                sh.copyfile(d, f)
                            else:
                                sh.copytree(d, f)
                        else:
                            __pwrcopy(d, f)
                    return 1
            except:
                return 0
        except IOError:
            if os.path.isfile(f):
                os.chmod(f, ~0)
                os.remove(f)
            return 0
        except:
            return 0
    dst=dst+'\\'+os.path.basename(src)
    try:
        if os.path.isfile(src):
            sh.copyfile(src, dst)
        else:
            sh.copytree(src, dst)
        print 'successful'
    except IOError:
        if os.path.isfile(dst):
            os.chmod(dst, ~0)
            os.remove(dst)
        print 'cant copy'
        return
    except:
        print 'trying power copy'
        if  __pwrcopy(src, dst):
            print 'success'
        else:
            print 'cant copy'