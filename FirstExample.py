#!/usr/bin/env python
# Example of Documentation as Code
import optparse

def main():
    parser = optparse.OptionParser(usage='Usage: %prog -o [run|doc]')
    dac_choices = ['run', 'doc', 'Run', 'Doc', 'RUN', 'DOC']
    parser.add_option("-o", dest="runordoc",
                      type="choice",
                      choices=dac_choices,
                      help="Please specify if you want Run or Doc")

    (opts, args) = parser.parse_args()

    if opts.runordoc is None:
        print "A mandatory option is missing\n"
        parser.print_help()
        exit(-1)

    if opts.runordoc == "Run" or opts.runordoc == "run" or opts.runordoc =="RUN":
        print "Here goes the code to run"
        exit(0)

    elif opts.runordoc == "Doc" or opts.runordoc == "doc" or opts.runordoc =="DOC":
        DACv1 = """## Documentation Starts

Here you can add all the needed markdown documentation. You can split it as shown in this script.

"""

        DACv2 = """### Documentation Continues

Here goes the documentation example with a table:

 1 | 2 | 3 | 4 | 5
---|---|---|---
 T | H | I | S |
 I | S |   | A |
 T | A | B | L | E
"""

        print DACv1
        print DACv2.strip()

if __name__ == '__main__':
    main()