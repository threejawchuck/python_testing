def logging ():
    # USE LOGGING!!!!  It's so good it's now a built in to the language!!
    # Instead of using print to communicate with the user, use logging.  All
    # you have to do is import logging in all your modules, and use it instead
    # of print, that's it!!
    import os
    import time
    import logging

    # Log some messages
    logging.warn('warn message')
    logging.debug('debug message')
    logging.info('info message')
    logging.fatal('fatal message')

    # Then in the entry point of your program, usually in the 'if __name__ ==
    # "__main__"' block, you define your sinks for logging messages (screen,
    # file, etc) Here is my boilerplate to log to file and to screen.  There
    # are a million and one options on logging sinks, so see the python
    # documentation for more info.

    # Make log directory if it does not exist
    if not os.path.isdir('log'):
        os.makedirs('log')

    # File Sink
    logfile = time.strftime("RepoSync-%Y%m%d-%H%M%S.log")
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%Y%m%d %H:%M:%S',
        filename=os.path.join('log', logfile),
        filemode='w')

    # Screen Sink
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run example functions")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("EXAMPLE", type=str, help="the example to execute")
    args = parser.parse_args()

    if args.quiet:
        print("Quiet mode set")

    elif args.verbose:
        print("Verbose mode set")
    else:
        print("Default verbosity set")
        
    if args.EXAMPLE in globals():
       globals()[args.EXAMPLE]()
    else:
        raise NotImplementedError("Example %s not implemented" % args.EXAMPLE)
