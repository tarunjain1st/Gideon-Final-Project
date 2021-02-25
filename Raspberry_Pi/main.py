from db_connection import dataLink
api='gideon_v2.0_259634'

test = dataLink(api)
test.uploadDht(23,80)
print(test.fetchDht())
