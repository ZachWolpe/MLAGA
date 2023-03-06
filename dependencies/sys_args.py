
import getopt
import sys


class argument:
    def __init__(self, name, short_name, takes_input, default_value=None) -> None:
        self.name           = name
        self.short_name     = short_name
        self.takes_input    = takes_input
        self.default_value  = default_value


class argument_handlr:

    @staticmethod
    def _get_shortnames(short_name, takes_input=True):
        return short_name + ':' if takes_input else short_name

    @staticmethod
    def _get_longnames(long_name, takes_input=True):
        return long_name + '=' if takes_input else long_name
    
    @staticmethod
    def _get_takes_input(arguments):
        return {arg.name:arg.takes_input for arg in arguments}

    def __init__(self, arguments:list[argument]) -> None:
    
        return_object  = {arg.name:arg.default_value for arg in arguments}
        arg_shortnames = [argument_handlr._get_shortnames(arg.short_name, takes_input=arg.takes_input) for arg in arguments]
        arg_longnames  = [argument_handlr._get_longnames(arg.name,        takes_input=arg.takes_input) for arg in arguments]

        self.sys_argv   = sys.argv
        argv            = self.sys_argv[1:]
        try:
            opts, args = getopt.getopt(argv,
                                       ''.join(arg_shortnames),
                                       arg_longnames)
            
        except Exception as e:
            print(e)

        _key_search_list = []
        short = [sn.replace(':','') for sn in arg_shortnames]
        long  = [ln.replace('=','') for ln in arg_longnames]
        inpt  = argument_handlr._get_takes_input(arguments) 
    
        for s,l in zip(short,long):
            _key_search_list.append(['-' + s, '--' + l, l, inpt[l]])
            
        for name, val in opts:
            for ks in _key_search_list:
                if name in ks:
                    if ks[-1] == True:
                        return_object[ks[-2]] = val
                    else:
                        return_object[ks[-2]] = True
                    break

        self.args_dict = return_object

    def add_to_globals(self):
        # USE WITH CAUSTION!!! UNDETECTED IN STATIC ANALYSIS
        for k,v in self.args_dict.items():
            globals()[k] = v
        

    def print_configuration(self):
        filename = self.sys_argv[0]
        lines = ''; s=' '; mn = max([len(i) for i in self.args_dict.keys()]) + 2
        for k,v in self.args_dict.items():
            lines += f'\n           {k}:{s:>{mn-len(k)}} {v}'
        message = \
        f"""
        --------------------------------------------------------------------------------
        ================================================================================
        Running file: {filename}
        {lines}

        ================================================================================
        --------------------------------------------------------------------------------
        """  
        print(message) 

# Example --------------++
# arguments = [
#     argument('yt_url',      'y', True),
#     argument('bucket_name', 'b', True),
#     argument('exe',         'e', True),
#     argument('path',        'p', True),
#     argument('cached_audio','c', False)
# ]

# ah = argument_handlr(arguments)
# print(ah.args_dict)

# ah.print_configuration()
# # Example --------------++