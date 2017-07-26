c = get_config()

c.InteractiveShellApp.exec_lines = [
    '%autoreload 2',
    'from __future__ import division',
    'from __future__ import print_function',
    'pd.set_option("display.float_format", lambda x: "%.3f" % x)',
    'pd.set_option("display.width", 120)',
    'pd.set_option("max_rows", 300)'
]

# A list of dotted module names of IPython extensions to load.
c.TerminalIPythonApp.extensions = ['autoreload']

# c.InteractiveShellApp.extensions = ['auto_reload', 'line_profiler_ext', 'memory_profiler_ext']
