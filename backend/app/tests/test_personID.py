from crud.persons_crud import check_user_ID
from databases import persons_collection

def test_user_id():
    res1=check_user_ID(1)
    res0=check_user_ID(0)
    
    person1=persons_collection.find_one({"PersonID":1}, {'_id': False})
    
    
    assert  res1==person1
    assert  res0==None