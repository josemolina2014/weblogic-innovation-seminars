connect('weblogic','welcome1','t3://localhost:7001')
edit()
startEdit()
deploy(appName='heapApp', partition='Medrec-Dev', resourceGroup='app1RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab3/heapApp.war')
activate()
disconnect()
