from cmd import Cmd
import json
from types import MethodType
import inspect
from curses import wrapper
import os
class MyPrompt(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        print(dir(self.__class__))

    def postcmd(self, stop, line):
        if line == 'curses':
            os.system("cls")

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit

    def do_help(self, arg):
        'List available commands with "help" or detailed help with "help cmd".'
        if arg:
            # XXX check arg syntax
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write("%s\n" % str(doc))
                        return
                except AttributeError:
                    pass
                self.stdout.write("%s\n" % str(self.nohelp % (arg,)))
                return
            func()
        else:
            names = self.get_names()
            noms = list(vars(self).keys())
            for nom in noms:
                if nom[:5] == 'help_':
                    names.append(nom)
                if nom[:3] == 'do_':
                    names.append(nom)
            print(names)
            cmds_doc = []
            cmds_undoc = []
            help = {}
            for name in names:
                if name[:5] == 'help_':
                    help[name[5:]] = 1
            names.sort()
            # There can be duplicates if routines overridden
            prevname = ''
            for name in names:
                if name[:3] == 'do_':
                    if name == prevname:
                        continue
                    prevname = name
                    cmd = name[3:]
                    if cmd in help:
                        cmds_doc.append(cmd)
                        del help[cmd]
                    elif getattr(self, name).__doc__:
                        cmds_doc.append(cmd)
                    else:
                        cmds_undoc.append(cmd)
            self.stdout.write("%s\n" % str(self.doc_leader))
            self.print_topics(self.doc_header, cmds_doc, 15, 80)
            self.print_topics(self.misc_header, list(help.keys()), 15, 80)
            self.print_topics(self.undoc_header, cmds_undoc, 15, 80)

def create_command_funct(name, help):
    def do_cmd(self, args):
        print("You ran" + inspect.stack()[0][3] + " command")
    do_cmd.__name__ = "do_" + name
    do_cmd.__doc__ = help
    return do_cmd

def addfunct(name, help, prompt):
    c = create_command_funct(name, help)
    setattr(prompt, c.__name__, MethodType(c, prompt))

if __name__ == '__main__':
    prompt = MyPrompt()
    with open("Commands.json", encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    for i in data['Commands']:
        if i["Command"] == "help":
            continue
        addfunct(i['Command'], i['defaultOutput'], prompt)
    print(vars(prompt))
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
