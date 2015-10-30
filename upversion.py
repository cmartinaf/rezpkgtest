import os
import inspect
import ordereddict
import shutil
import pprint

def upversion(package_filepath):
    '''
    '''
    if os.path.exists(package_filepath):
        _locals = {}
        _globals = ordereddict.OrderedDict()

        execfile(package_filepath, _locals, _globals)
        
        version = _globals.get('version')

        major, minor, micro = version.split('.')

        micro = int(micro) + 1

        version = '.'.join((major, minor, str(micro)))

        _globals['version'] = str(version)
        
        output_filepath = os.path.join(os.path.dirname(package_filepath), '.package.py')

        with open(output_filepath, 'w') as out:
            for key, value in _globals.items():
                if inspect.isfunction(value):                                         
                    # pprint.pprint(inspect.getsource(value), stream=out)
                    out.write(inspect.getsource(value))
                elif isinstance(value, basestring):
                    if '\n' in value:                                                
                        out.write("{0} = '''{1}'''\n".format(key, value))                        
                    else:
                        out.write("{0} = '{1}'\n".format(key, value))
                else:
                    out.write("{0} = {1}\n".format(key, pprint.pformat(value)))
                out.write('\n')

        shutil.copy(output_filepath, package_filepath)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Rez Package Up-Versioner.")
 
    parser.add_argument('--major')
    parser.add_argument('--minor')    
    parser.add_argument('--micro')
 
    args = parser.parse_args()

    if package_filepath is None:        
        package_filepath = os.path.join(os.getcwd(), 'package.py')
    

    upversion("/Volumes/af/tools/sandbox/cmartin/dpooltools/maya/package.py")
