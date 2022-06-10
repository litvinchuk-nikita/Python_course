# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#   ...
#   |--templates
#   |   |--mainapp
#   |   |   |--base.html
#   |   |   |--index.html
#   |   |--authapp
#   |       |--base.html
#   |       |--index.html
# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.
import os
import shutil
if not os.path.exists('task_7_3'):
    os.mkdir('task_7_3')
for root, dirs, files in os.walk('my_project_1'):
    for file in files:
        if os.path.join(root, file).endswith('.html'):
            new_dir = os.path.join('task_7_3', os.path.basename(os.path.dirname(os.path.join(root, file))))
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            new_file = os.path.join(root, file)
            new_path = os.path.join(new_dir, os.path.basename(os.path.join(root, file)))
            shutil.copy(new_file, new_path)
