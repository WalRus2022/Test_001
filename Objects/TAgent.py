import copy
import datetime
import uuid

from Objects.TProperty import TPropertyObject, TPropertyDate, TPropertyUUID, TPropertyUnInt, TPropertyStrSized, \
    TPropertyUnROInt, TPropertyAddress


class TAgent:
    # __slots__ = ('_workarea', 'id', 'uid', 'name', 'actype', 'date1', 'date2')

    _workarea = TPropertyObject('_workarea')
    id = TPropertyUnInt('id')
    # id = TPropertyRoUnInt('id')
    uid = TPropertyUUID('uid')
    name = TPropertyStrSized('name', size=255)
    actype = TPropertyUnInt('actype')
    date1 = TPropertyDate('date1')
    date2 = TPropertyDate('date2')
    address_ur =TPropertyAddress( 'address_ur')
    address_real =TPropertyAddress( 'address_real')


    @classmethod
    def _loadfromid(cls, workarea, id:int):
        agent = cls.__new__(cls)
        data = {'_workarea':workarea,'id':id, 'name':'Тестовый контрагент #'+str(id), 'uid':uuid.uuid4(), 'actype':1, 'date1':datetime.datetime(2022,6,12)}
        data['_uid'] = uuid.uuid4()
        for key, value in data.items():
            setattr(agent, key, value)
        return agent

    @classmethod
    def _new(cls, workarea, name:str=None, actype:int=None):
        agent = cls.__new__(cls)
        data = {'_workarea':workarea,'id': 0, 'name': name, 'uid': uuid.uuid4(), 'actype': actype, 'date1':datetime.datetime(2021,1,12)}
        for key, value in data.items():
            setattr(agent, key, value)
        return agent

    def save(self):
        self.id = 155
        self._workarea._cache_agents_update(self)

    def reload(self):
        return self._workarea.agent(id=self.id, reload=True)
        # del self
        # self = copy.deepcopy(agent_reload)
        # self.name +=' reload'
        # return agent_reload

def main():
    pass


if __name__ == '__main__':
    main()
