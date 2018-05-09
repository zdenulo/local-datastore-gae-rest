import os

# this can be set also in shell as
# export DATASTORE_EMULATOR_HOST=localhost:8081

os.environ['DATASTORE_EMULATOR_HOST'] = 'localhost:8081'


from google.cloud import datastore

client = datastore.Client()


def list_books():
    """Fetch all Book entities in Datastore and return as list"""
    res = client.query(kind='Book').fetch()
    return list(res)


def create_book(name):
    """Create simple entity and store in Datastore"""
    key = client.key('Book')
    key = client.allocate_ids(key, 1)

    entity = datastore.Entity(key=key[0])
    entity.update({'name': name})
    client.put(entity)


if __name__ == '__main__':
    create_book('local')
    books = list_books()
    for b in books:
        print b


