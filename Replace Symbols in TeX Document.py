# sOctober 21 2016 07:01:35.Close Code
'''T22.10 Скласти програму, яка здійснює заміну новим рядком рядка, що
відповідає заданому регулярному виразу, у знайдених у заданому каталозі
та його підкаталогах усіх текстових файлах, імена яких відповідають
заданій масці.'''
import re, os
import mmap

print('Start...')
catalog = '.' # '/' - from the root, 'cat', '.' - in file's directory

# to do add [, ] and (, ) support fix \{} 
patterns = {r'<=>def':  '$\\\\overset{\\\\text{def}}{\\\\iff}$',
            r'<=>':     "$\\\\iff$",
            r'<=':      "$\\\\Leftarrow$",
            r'=>':      "$\\\\implies$",
            r'\|->':    "\\\\mapsto ",
            r'->':      '\\\\rightarrow ',
            r'-\*':     '\\\\textbullet ',
            r'\\}':      '\\\\right\}',
            r'\\{':      '\\\\left\{',
            }
for (dirpath, dirnames, filenames) in os.walk(catalog):
    # filtering out all hidden files and folders
    filenames = [f for f in filenames if not f[0] == '.']
    dirnames[:] = [d for d in dirnames if not d[0] == '.']
    for filename in filenames:
        # print('File under consideration', filename)
        if '.' not in filename:
            # print('file rejected immediately')
            break
        name = re.search('\.(.+)$', filename)
        if name.group(1) == 'tex':
            print(filename)
            import io
            with io.open(os.path.join(dirpath, filename), 'r', encoding='utf-8', errors='replace') as file:
                text = file.read()
            file = open(os.path.join(dirpath, filename+'.backup.tex'), 'wb')
            file.write(text.encode('utf8'))
            file.close()
            # print('- recognized and open an applicable file')
            for pattern, replacement in patterns.items():
                pattern = re.compile(pattern, flags=0)
                print(re.search(pattern, text))
                textnew = re.sub(pattern, replacement, text)
                text = textnew
                print('replacement', str(pattern), replacement)
            file = open(os.path.join(dirpath, filename), 'wb')
            file.write(text.encode('utf8'))
            file.close()
        else:
            # print('File {} doest\'t match a criteria and is rejected'.format(filename))
            pass

'''
import re, mmap

with open('/var/log/error.log', 'r+') as f:
  data = mmap.mmap(f.fileno(), 0)
  mo = re.search('error: (.*)', data)
  if mo:
    print "found error", mo.group(1)


pattern = r'\* \[(.*)\]\(#(.*)\)'
'''
