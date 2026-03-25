# Basic formatting
# Old
print('%s %s' % ('one', 'two'))
# New
'{} {}'.format('one', 'two')
# Output
# one two
# Old
print('%d %d' % (1, 2))
# New
print('{} {}'.format(1, 2))
# Output
# 1 2
# New
print('{1} {0}'.format('one', 'two'))


# Output
# two one
# Value conversion
class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


# Old
print('%s %r' % (Data(), Data()))
# New
print('{0!s} {0!r}'.format(Data()))


# Output
# str repr

class Data(object):

    def __repr__(self):
        return 'räpr'


# Old
print('%r %a' % (Data(), Data()))
# New
print('{0!r} {0!a}'.format(Data()))
# Output
# räpr r\xe4pr


# Padding and aligning strings
# Align right:
# Old
print('%10s' % ('test',))
# New
print('{:>10}'.format('test'))
# Output
#       test
# Align left:
# Old
print('%-10s' % ('test',))
# New
print('{:10}'.format('test'))
# Output
# test
# You are able to choose the padding character:

# This operation is not available with old-style formatting.

# New
print('{:_<10}'.format('test'))
# Output
# test______
# And also center align values:

# This operation is not available with old-style formatting.

# New
print('{:^10}'.format('test'))
# Output
#    test
# This operation is not available with old-style formatting.

# New
print('{:^6}'.format('zip'))
# Output
#  zip
# Truncating long strings
# Old
print('%.5s' % ('xylophone',))
# New
print('{:.5}'.format('xylophone'))
# Output
# xylop
# Combining truncating and padding
# Old
print('%-10.5s' % ('xylophone',))
# New
print('{:*^10.5}'.format('xylophone'))
# Output
# xylop
# Numbers
# Of course it is also possible to format numbers.

# Integers:

# Old
print('%d' % (42,))
# New
print('{:d}'.format(42))
# Output
# 42
# Floats:

# Old
print('%f' % (3.141592653589793,))
# New
print('{:f}'.format(3.141592653589793))
# Output
# 3.141593
# Padding numbers
# Old
print('%4d' % (42,))
# New
print('{:4d}'.format(42))
# Output
#   42
# Old
print('%06.2f' % (3.141592653589793,))
# New
print('{:06.2f}'.format(3.141592653589793))
# Output
# 003.14
# Old
print('%04d' % (42,))
# New
print('{:04d}'.format(42))
# Output
# 0042
# Signed numbers
# Old
print('%+d' % (42,))
# New
print('{:+d}'.format(42))
# Output
# +42
# Old
print('% d' % ((- 23),))
# New
print('{: d}'.format((- 23)))
# Output
# -23
# Old
print('% d' % (42,))
# New
print('{: d}'.format(42))
# Output
#  42
# This operation is not available with old-style formatting.

# New
print('{:=5d}'.format((- 23)))
# Output
# -  23
# New
print('{:=+5d}'.format(23))
# Output
# +  23
# Named placeholders
# Setup
data = {'first': 'Hodor', 'last': 'Hodor!'}
# Old
print('%(first)s %(last)s' % data)
# New
print('{first} {last}'.format(**data))
# Output
# Hodor Hodor!
# .format() also accepts keyword arguments.

# This operation is not available with old-style formatting.

# New
print('{first} {last}'.format(first='Hodor', last='Hodor!'))
# Output
# Hodor Hodor!
# Getitem and Getattr
# New style formatting allows even greater flexibility in accessing nested data structures.

# It supports accessing containers that support __getitem__ like for example dictionaries and lists:

# This operation is not available with old-style formatting.

# Setup
person = {'first': 'Jean-Luc', 'last': 'Picard'}
# New
print('{p[first]} {p[last]}'.format(p=person))
# Output
# Jean-Luc Picard
# Setup
data = [4, 8, 15, 16, 23, 42]
# New
print('{d[4]} {d[5]}'.format(d=data))


# Output
# 23 42
# As well as accessing attributes on objects via getattr():
#
# This operation is not available with old-style formatting.

# Setup
class Plant(object):
    type = 'tree'


# New
print('{p.type}'.format(p=Plant()))


# Output
# tree
# Both type of access can be freely mixed and arbitrarily nested:
#
# This operation is not available with old-style formatting.
#
# Setup
class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]


# New
print('{p.type}: {p.kinds[0][name]}'.format(p=Plant()))
# Output
# tree: oak
# Datetime
# New style formatting also allows objects to control their own rendering. This for example allows datetime objects to be formatted inline:
#
# This operation is not available with old-style formatting.
#
# Setup
from datetime import datetime

# New
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))
# Output
# 2001-02-03 04:05
# Parametrized formats
# Additionally, new style formatting allows all of the components of the format to be specified dynamically using parametrization. Parametrized formats are nested expressions in braces that can appear anywhere in the parent format after the colon.
#
# Old style formatting also supports some parametrization but is much more limited. Namely it only allows parametrization of the width and precision of the output.
#
# Parametrized alignment and width:
#
# This operation is not available with old-style formatting.
#
# New
print('{:{align}{width}}'.format('test', align='^', width='10'))
# Output
#    test
# Parametrized precision:
#
# Old
print('%.*s = %.*f' % (3, 'Gibberish', 3, 2.7182))
# New
print('{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3))
# Output
# Gib = 2.718
# Width and precision:
#
# Old
print('%*.*f' % (5, 2, 2.7182))
# New
print('{:{width}.{prec}f}'.format(2.7182, width=5, prec=2))
# Output
#  2.72
# The nested format can be used to replace any part of the format spec, so the precision example above could be rewritten as:
#
# This operation is not available with old-style formatting.
#
# New
print('{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3'))
# Output
# Gib = 2.72
# The components of a date-time can be set separately:
#
# This operation is not available with old-style formatting.
#
# Setup
from datetime import datetime

dt = datetime(2001, 2, 3, 4, 5)
# New
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))
# Output
# 2001-02-03 04:05
# The nested formats can be positional arguments. Position depends on the order of the opening curly braces:
#
# This operation is not available with old-style formatting.
#
# New
print('{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3))
# Output
#      +2.72
# And of course keyword arguments can be added to the mix as before:
#
# This operation is not available with old-style formatting.
#
# New
print('{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3, sign='+'))


# Output
#      +2.72
# Custom objects
# The datetime example works through the use of the __format__() magic method. You can define custom format handling in your own objects by overriding this method. This gives you complete control over the format syntax used.
#
# This operation is not available with old-style formatting.
#
# Setup
class HAL9000(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'


# New
print('{:open-the-pod-bay-doors}'.format(HAL9000()))
# Output
# I'm afraid I can't do that.
