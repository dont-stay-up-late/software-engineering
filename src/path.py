from pathlib import Path

def root():
    '''
    Returns the absolute path of project root in environment-specific string.
    '''
    r = Path.cwd()
    if str(r).endswith('src') or str(r).endswith('src/') or str(r).endswith('src\\'):
        return r.parent
    return r

def path(arg):
    '''
    Returns the absolute path of a required file in environment-specific string.
    '''
    r = root()
    segs = arg.split('/\\')
    for seg in segs:
        if seg != '':
            r = r.joinpath(seg)
    return str(r)