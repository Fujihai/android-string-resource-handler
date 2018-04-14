# Android字串资源处理工具

### 这是什么

一个使用Python语言编写的脚本。

可以将Android项目中的多语言字串 `.xml` 文件生成一份多语言 `.xls` 文件，供翻译人员校对更改。生成规则：以英文 `.xml` 文件中`string` 项的 `name` 字段为查找标准，并在其他多语言 `.xml` 文件中进行查找，`name` 字段相同的就会输出到 `.xls` 文件中。

另外，可以根据生成的 `.xls` 文件再重新生成 `xml` 文件。这意味着：后续只需维护一份`.xls` 文件，就可以解决多语言字串资源更替所带来的繁琐人工操作。

### 运行环境

* Python 3.6.1

### 如何使用

* 请使用 `pip` 命令安装相关依赖库 `xlwd`、`xlwt`、`ruamel.yaml` 。


* 配置 `config.xml` 文件，指定源 `xml` 文件路径，目标 `xls` 路径，目标 `xml` 路径。注意：要确保配置的路径中的文件夹都存在。若无，请事先生成。

* 进入 `scripts` 文件夹。

* `.xls` 文件生成 : `python read_xml_and_gen_xls.py` 。

  ![](https://github.com/liufushihai/android-string-resource-handler/blob/master/images/read_xml_and_gen_xls.gif)

* `.xml` 文件生成：`python read_xls_and_gen_xml.py` 。

  ![](https://github.com/liufushihai/android-string-resource-handler/blob/master/images/read_xls_and_gen_xml.gif)