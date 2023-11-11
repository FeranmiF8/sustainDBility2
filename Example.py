import faws


def main():
    server = faws.connect(ip, user, pass)
    
    table = server.openTable('tableName')
    
    print(table.get('key')) #prints a list with values from key
    
    table.set('key', ['value1', 'value2']) #sets key to value
    