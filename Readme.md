 python -m venv venv
 Set-ExecutionPolicy Unrestricted -Scope Process
  .\venv\Scripts\Activate


  db.user.insertOne({"name":"akewal","email":"akewal@citco.com","department":"it","location":"pune","seat_allocation":[{"seat":"c1","date":"01-01-2024"},{"seat":"c2","date":"01-01-2024"}],"mobile_no":"+911277884499"})

  db.user.find().pretty()


{'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}
{'n': 1, 'upserted': ObjectId('64ab21e63e4faa0584324063'), 'nModified': 0, 'ok': 1.0, 'updatedExisting': False}   