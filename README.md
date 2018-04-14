# android-string-resource-handler

### What is this?

A python script.

It can generate `.xls`  file by  means of  android `.xml` file and it also can genereate `.xml` with  the `.xls` file you generated . 

Make you work effectively !

### Run Environment

* Python 3.6.1

### How to use

* Please install relative module  `xlwd` 、`xlwt` 、`ruamel.yaml` by  `pip` command.

* Configure  `config.xml` file and set the origin xml path , target xls path ,

  target xml path . Warning : make sure the folder in the path has existed. 

  Otherwise you need to create the folder which in path.

* Generated `.xls` file :  `python read_xml_and_gen_xls.py` .

  ![]()

* Genereated `.xml` file :  `python read_xls_and_gen_xml.py` .

  ![]()