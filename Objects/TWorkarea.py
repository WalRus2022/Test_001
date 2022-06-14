import weakref
from Objects.TAgent import TAgent


class TWorkArea:
    _conn = ''
    _agent_cache = weakref.WeakValueDictionary()
    def __init__(self, cnString):
        self._conn = cnString

    def spam(self, k=None):
        print('spam')

    def agent(self, id:int=None, name:str=None, actype:int=None, reload:bool=False):
        a = None
        if id is None:
            a = TAgent._new(self, name=name, actype=actype)
            self._agent_cache[(a.id, a.uid)]= a
        else:
            if len(self._agent_cache)>0:
                for k,v in self._agent_cache.items():
                    iid, uid = k
                    if iid == id:
                        if not reload:
                            a = v
                        else:
                            self._agent_cache.pop(k)
                        break
                if a is None:
                    a = TAgent._loadfromid(self, id)
                    self._agent_cache[(a.id, a.uid)] = a
        return a

    def _cache_agents_update(self, agent):
        for k, v in self._agent_cache.items():
            iid, uid = k
            if uid == agent.uid:
                self._agent_cache.pop(k)
                self._agent_cache[(agent.id, agent.uid)] = agent
                break

def main():
    workarea = TWorkArea('string')
    a = workarea.agent(name='моя фирма', actype=5)
    a.save()
    print('a')
    print(a.name)
    print(a.id)

    c = workarea.agent(id=150)
    b = workarea.agent(id=150)
    d = workarea.agent(id=170)
    print('c')
    if c is not None:
        print (c.name)
        print (c.id)

    if b is not None:
        print (b.name)
        print (b.id)

    if d is not None:
        print (d.name)
        print (d.id)
    e = workarea.agent(id=155)
    print('Second load')
    if e is not None:
        print (e.name)
        print (e.id)
    print('reload')
    e = e.reload()
    # e.reload()
    if e is not None:
        print (e.name)
        print (e.id)
    print('From cache')
    e = workarea.agent(id=155)
    if e is not None:
        print (e.name)
        print (e.id)


if __name__ == '__main__':
    main()
