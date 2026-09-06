# thefuck-3 :: hybrid

query: #869: Use `fish --version` instead of an interactive shell for info()

## selected nodes

- rank=1 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish._get_version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=2 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.info file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=3 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic._get_version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=4 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.shell file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py
- rank=5 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.put_to_history file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=6 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh._get_version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py
- rank=7 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.how_to_configure file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=8 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh._get_version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py
- rank=9 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash._get_version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=10 layer=FUNCTION tokens=275 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py
- rank=11 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py
- rank=12 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py
- rank=13 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::_get_functions file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=14 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_not_command.py::get_docker_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_not_command.py
- rank=15 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_fish.py::proc file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_fish.py
- rank=16 layer=FUNCTION tokens=1063 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help_new file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=17 layer=FUNCTION tokens=178 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell._get_version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py
- rank=18 layer=FUNCTION tokens=375 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/argument_parser.py::Parser._add_arguments file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/argument_parser.py
- rank=19 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::_get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=20 layer=FUNCTION tokens=242 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=21 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_add_force.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_add_force.py
- rank=22 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_argument_parser.py::_args file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_argument_parser.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish._get_version [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py]

    def _get_version(self):
        """Returns the version of the current shell"""
        proc = Popen(['fish', '--version'], stdout=PIPE, stderr=DEVNULL)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.info [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py]
    def info(self):
        """Returns the name and version of the current shell"""
        try:
            version = self._get_version()
        except Exception as e:
            warn(u'Could not determine shell version: {}'.format(e))
            version = ''
        return u'{} {}'.format(self.friendly_name, version).rstrip()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic._get_version [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py]
    def _get_version(self):
        """Returns the version of the current shell"""
        return ''

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.shell [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py]
    def shell(self):
        return Fish()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.put_to_history [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py]
    def put_to_history(self, command):
        """Adds fixed command to shell history.

        In most of shells we change history on shell-level, but not
        all shells support it (Fish).

        """

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh._get_version [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py]
    def _get_version(self):
        """Returns the version of the current shell"""
        proc = Popen(['tcsh', '--version'], stdout=PIPE, stderr=DEVNULL)
        return proc.stdout.read().decode('utf-8').split()[1]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.how_to_configure [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py]

    def how_to_configure(self):
        return self._create_shell_configuration(
            content=u"thefuck --alias | source",
            path='~/.config/fish/config.fish',

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh._get_version [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py]
    def _get_version(self):
        """Returns the version of the current shell"""
        proc = Popen(['zsh', '-c', 'echo $ZSH_VERSION'],
                     stdout=PIPE, stderr=DEVNULL)
        return proc.stdout.read().decode('utf-8').strip()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash._get_version [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py]
    def _get_version(self):
        """Returns the version of the current shell"""
        proc = Popen(['bash', '-c', 'echo $BASH_VERSION'],
                     stdout=PIPE, stderr=DEVNULL)
        return proc.stdout.read().decode('utf-8').strip()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py::main [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py]
def main():
    parser = Parser()
    known_args = parser.parse(sys.argv)

    if known_args.help:
        parser.print_help()
    elif known_args.version:
        logs.version(get_installation_version(),
                     sys.version.split()[0], shell.info())
    # It's important to check if an alias is being requested before checking if
    # `TF_HISTORY` is in `os.environ`, otherwise it might mess with subshells.
    # Check https://github.com/nvbn/thefuck/issues/921 for reference
    elif known_args.alias:
        print_alias(known_args)
    elif known_args.command or 'TF_HISTORY' in os.environ:
        fix_command(known_args)
    elif known_args.shell_logger:
        try:
            from .shell_logger import shell_logger  # noqa: E402
        except ImportError:
            logs.warn('Shell logger supports only Linux and macOS')
        else:
            shell_logger(known_args.shell_logger)
    else:
        parser.print_usage()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::version [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py]
def version(thefuck_version, python_version, shell_info):
    sys.stderr.write(
        u'The Fuck {} using Python {} and {}\n'.format(thefuck_version,
                                                       python_version,
                                                       shell_info))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.Popen [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py]
    def Popen(self, mocker):
        mock = mocker.patch('thefuck.shells.fish.Popen')
        mock.return_value.stdout.read.side_effect = [(
            b'cd\nfish_config\nfuck\nfunced\nfuncsave\ngrep\nhistory\nll\nls\n'
            b'man\nmath\npopd\npushd\nruby'),
            (b'alias fish_key_reader /usr/bin/fish_key_reader\nalias g git\n'
             b'alias alias_with_equal_sign=echo\ninvalid_alias'), b'func1\nfunc2', b'']
        return mock

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::_get_functions [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py]
def _get_functions(overridden):
    proc = Popen(['fish', '-ic', 'functions'], stdout=PIPE, stderr=DEVNULL)
    functions = proc.stdout.read().decode('utf-8').strip().split('\n')
    return {func: func for func in functions if func not in overridden}

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_not_command.py::get_docker_commands [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_not_command.py]
def get_docker_commands():
    proc = subprocess.Popen('docker', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Old version docker returns its output to stdout, while newer version returns to stderr.
    lines = proc.stdout.readlines() or proc.stderr.readlines()
    lines = [line.decode('utf-8') for line in lines]

    # Only newer versions of docker have management commands in the help text.
    if 'Management Commands:\n' in lines:
        management_commands = _parse_commands(lines, 'Management Commands:')
    else:
        management_commands = []
    regular_commands = _parse_commands(lines, 'Commands:')
    return management_commands + regular_commands

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_fish.py::proc [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_fish.py]
def proc(request, spawnu, TIMEOUT):
    proc = spawnu(*request.param)
    proc.sendline(u'thefuck --alias > ~/.config/fish/config.fish')
    proc.sendline(u'fish')
    return proc

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help_new [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py]
def docker_help_new(mocker):
    helptext_new = b'''
Usage:	docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/Users/ik1ne/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var
                           and default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/Users/ik1ne/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/Users/ik1ne/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/Users/ik1ne/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.
'''
    mock = mocker.patch('subprocess.Popen')
    mock.return_value.stdout = BytesIO(b'')
    mock.return_value.stderr = BytesIO(helptext_new)
    return mock

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell._get_version [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py]
    def _get_version(self):
        """Returns the version of the current shell"""
        try:
            proc = Popen(
                ['powershell.exe', '$PSVersionTable.PSVersion'],
                stdout=PIPE,
                stderr=DEVNULL)
            version = proc.stdout.read().decode('utf-8').rstrip().split('\n')
            return '.'.join(version[-1].split())
        except IOError:
            proc = Popen(['pwsh', '--version'], stdout=PIPE, stderr=DEVNULL)
            return proc.stdout.read().decode('utf-8').split()[-1]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/argument_parser.py::Parser._add_arguments [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/argument_parser.py]
    def _add_arguments(self):
        """Adds arguments to parser."""
        self._parser.add_argument(
            '-v', '--version',
            action='store_true',
            help="show program's version number and exit")
        self._parser.add_argument(
            '-a', '--alias',
            nargs='?',
            const=get_alias(),
            help='[custom-alias-name] prints alias for current shell')
        self._parser.add_argument(
            '-l', '--shell-logger',
            action='store',
            help='log shell output to the file')
        self._parser.add_argument(
            '--enable-experimental-instant-mode',
            action='store_true',
            help='enable experimental instant mode, use on your own risk')
        self._parser.add_argument(
            '-h', '--help',
            action='store_true',
            help='show this help message and exit')
        self._add_conflicting_arguments()
        self._parser.add_argument(
            '-d', '--debug',
            action='store_true',
            help='enable debug output')
        self._parser.add_argument(
            '--force-command',
            action='store',
            help=SUPPRESS)
        self._parser.add_argument(
            'command',
            nargs='*',
            help='command that should be fixed')

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::_get_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py]
def _get_aliases(overridden):
    aliases = {}
    proc = Popen(['fish', '-ic', 'alias'], stdout=PIPE, stderr=DEVNULL)
    alias_out = proc.stdout.read().decode('utf-8').strip()
    if not alias_out:
        return aliases
    for alias in alias_out.split('\n'):
        for separator in (' ', '='):
            split_alias = alias.replace('alias ', '', 1).split(separator, 1)
            if len(split_alias) == 2:
                name, value = split_alias
                break
        else:
            continue
        if name not in overridden:
            aliases[name] = value
    return aliases

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.app_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py]

    def app_alias(self, alias_name):
        if settings.alter_history:
            alter_history = ('    builtin history delete --exact'
                             ' --case-sensitive -- $fucked_up_command\n'
                             '    builtin history merge\n')
        else:
            alter_history = ''
        # It is VERY important to have the variables declared WITHIN the alias
        return ('function {0} -d "Correct your previous console command"\n'
                '  set -l fucked_up_command $history[1]\n'
                '  env TF_SHELL=fish TF_ALIAS={0} PYTHONIOENCODING=utf-8'
                ' thefuck $fucked_up_command {2} $argv | read -l unfucked_command\n'
                '  if [ "$unfucked_command" != "" ]\n'
                '    eval $unfucked_command\n{1}'
                '  end\n'

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_add_force.py::output [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_add_force.py]
def output():
    return ('The following paths are ignored by one of your .gitignore files:\n'
            'dist/app.js\n'
            'dist/background.js\n'
            'dist/options.js\n'
            'Use -f if you really want to add them.\n')

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_argument_parser.py::_args [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_argument_parser.py]
def _args(**override):
    args = {'alias': None, 'command': [], 'yes': False,
            'help': False, 'version': False, 'debug': False,
            'force_command': None, 'repeat': False,
            'enable_experimental_instant_mode': False,
            'shell_logger': None}
    args.update(override)
    return args
```
