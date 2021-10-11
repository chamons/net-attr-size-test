file = """
using System.Runtime.Versioning;

namespace attr_size;
"""

template = open ("template.txt", "r").read ();

for i in range(100):
    file += template.replace ("TEMPLATE", "Class" + str(i)) + "\n\n"

output = open('code.cs', 'w')
output.write(file)
