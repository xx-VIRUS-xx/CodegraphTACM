# thefuck-26 :: codesearch

query: Support for either starting only the machine requested, or starting all machines

## selected nodes

- rank=1 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/vagrant_up.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/vagrant_up.py
- rank=2 layer=FUNCTION tokens=1063 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help_new file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=3 layer=FUNCTION tokens=231 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/shell_logger.py::_spawn file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/shell_logger.py
- rank=4 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/output_readers/test_rerun.py::TestRerun.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/output_readers/test_rerun.py
- rank=5 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_bash.py::proc file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_bash.py
- rank=6 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_zsh.py::proc file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_zsh.py
- rank=7 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/conftest.py::builtins_open file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/conftest.py
- rank=8 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py::Rule.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py
- rank=9 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/not_configured.py::_record_first_run file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/not_configured.py
- rank=10 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py::_get_operations file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py
- rank=11 layer=FUNCTION tokens=275 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py
- rank=12 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/system/win32.py::open_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/system/win32.py
- rank=13 layer=FUNCTION tokens=1362 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=14 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::Cache.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/vagrant_up.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/vagrant_up.py]
def get_new_command(command):
    cmds = command.script_parts
    machine = None
    if len(cmds) >= 3:
        machine = cmds[2]

    start_all_instances = shell.and_(u"vagrant up", command.script)
    if machine is None:
        return start_all_instances
    else:
        return [shell.and_(u"vagrant up {}".format(machine), command.script),
                start_all_instances]

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/shell_logger.py::_spawn [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/shell_logger.py]
def _spawn(shell, master_read):
    """Create a spawned process.

    Modified version of pty.spawn with terminal size support.

    """
    pid, master_fd = pty.fork()

    if pid == pty.CHILD:
        os.execlp(shell, shell)

    try:
        mode = tty.tcgetattr(pty.STDIN_FILENO)
        tty.setraw(pty.STDIN_FILENO)
        restore = True
    except tty.error:    # This is the same as termios.error
        restore = False

    _set_pty_size(master_fd)
    signal.signal(signal.SIGWINCH, lambda *_: _set_pty_size(master_fd))

    try:
        pty._copy(master_fd, master_read, pty._read)
    except OSError:
        if restore:
            tty.tcsetattr(pty.STDIN_FILENO, tty.TCSAFLUSH, mode)

    os.close(master_fd)
    return os.waitpid(pid, 0)[1]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/output_readers/test_rerun.py::TestRerun.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/output_readers/test_rerun.py]
    def setup_method(self, test_method):
        self.patcher = patch('thefuck.output_readers.rerun.Process')
        process_mock = self.patcher.start()
        self.proc_mock = process_mock.return_value = Mock()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_bash.py::proc [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_bash.py]
def proc(request, spawnu, TIMEOUT):
    container, instant_mode = request.param
    proc = spawnu(*container)
    proc.sendline(init_bashrc.format(
        u'--enable-experimental-instant-mode' if instant_mode else ''))
    proc.sendline(u"bash")
    if instant_mode:
        assert proc.expect([TIMEOUT, u'instant mode ready: True'])
    return proc

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_zsh.py::proc [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/test_zsh.py]
def proc(request, spawnu, TIMEOUT):
    container, instant_mode = request.param
    proc = spawnu(*container)
    proc.sendline(init_zshrc.format(
        u'--enable-experimental-instant-mode' if instant_mode else ''))
    proc.sendline(u"zsh")
    if instant_mode:
        assert proc.expect([TIMEOUT, u'instant mode ready: True'])
    return proc

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/conftest.py::builtins_open [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/conftest.py]
def builtins_open(mocker):
    return mocker.patch('six.moves.builtins.open')

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py::Rule.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py]
    def __init__(self, name='', match=lambda *_: True,
                 get_new_command=lambda *_: '',
                 enabled_by_default=True,
                 side_effect=None,
                 priority=DEFAULT_PRIORITY,
                 requires_output=True):
        super(Rule, self).__init__(name, match, get_new_command,
                                   enabled_by_default, side_effect,
                                   priority, requires_output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/not_configured.py::_record_first_run [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/not_configured.py]
def _record_first_run():
    """Records shell pid to tracker file."""
    info = {'pid': _get_shell_pid(),
            'time': time.time()}

    mode = 'wb' if six.PY2 else 'w'
    with _get_not_configured_usage_tracker_path().open(mode) as tracker:
        json.dump(info, tracker)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py::_get_operations [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py]
def _get_operations():
    proc = subprocess.Popen('yum', stdout=subprocess.PIPE)

    lines = proc.stdout.readlines()
    lines = [line.decode('utf-8') for line in lines]
    lines = dropwhile(lambda line: not line.startswith("List of Commands:"), lines)
    lines = islice(lines, 2, None)
    lines = list(takewhile(lambda line: line.strip(), lines))
    return [line.strip().split(' ')[0] for line in lines]

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/system/win32.py::open_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/system/win32.py]
def open_command(arg):
    return 'cmd /c start ' + arg

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py]
def docker_help(mocker):
    help = b'''Usage: docker [OPTIONS] COMMAND [arg...]

A self-sufficient runtime for linux containers.

Options:

  --api-cors-header=                   Set CORS headers in the remote API
  -b, --bridge=                        Attach containers to a network bridge
  --bip=                               Specify network bridge IP
  -D, --debug=false                    Enable debug mode
  -d, --daemon=false                   Enable daemon mode
  --default-gateway=                   Container default gateway IPv4 address
  --default-gateway-v6=                Container default gateway IPv6 address
  --default-ulimit=[]                  Set default ulimits for containers
  --dns=[]                             DNS server to use
  --dns-search=[]                      DNS search domains to use
  -e, --exec-driver=native             Exec driver to use
  --exec-opt=[]                        Set exec driver options
  --exec-root=/var/run/docker          Root of the Docker execdriver
  --fixed-cidr=                        IPv4 subnet for fixed IPs
  --fixed-cidr-v6=                     IPv6 subnet for fixed IPs
  -G, --group=docker                   Group for the unix socket
  -g, --graph=/var/lib/docker          Root of the Docker runtime
  -H, --host=[]                        Daemon socket(s) to connect to
  -h, --help=false                     Print usage
  --icc=true                           Enable inter-container communication
  --insecure-registry=[]               Enable insecure registry communication
  --ip=0.0.0.0                         Default IP when binding container ports
  --ip-forward=true                    Enable net.ipv4.ip_forward
  --ip-masq=true                       Enable IP masquerading
  --iptables=true                      Enable addition of iptables rules
  --ipv6=false                         Enable IPv6 networking
  -l, --log-level=info                 Set the logging level
  --label=[]                           Set key=value labels to the daemon
  --log-driver=json-file               Default driver for container logs
  --log-opt=map[]                      Set log driver options
  --mtu=0                              Set the containers network MTU
  -p, --pidfile=/var/run/docker.pid    Path to use for daemon PID file
  --registry-mirror=[]                 Preferred Docker registry mirror
  -s, --storage-driver=                Storage driver to use
  --selinux-enabled=false              Enable selinux support
  --storage-opt=[]                     Set storage driver options
  --tls=false                          Use TLS; implied by --tlsverify
  --tlscacert=~/.docker/ca.pem         Trust certs signed only by this CA
  --tlscert=~/.docker/cert.pem         Path to TLS certificate file
  --tlskey=~/.docker/key.pem           Path to TLS key file
  --tlsverify=false                    Use TLS and verify the remote
  --userland-proxy=true                Use userland proxy for loopback traffic
  -v, --version=false                  Print version information and quit

Commands:
    attach    Attach to a running container
    build     Build an image from a Dockerfile
    commit    Create a new image from a container's changes
    cp        Copy files/folders from a container's filesystem to the host path
    create    Create a new container
    diff      Inspect changes on a container's filesystem
    events    Get real time events from the server
    exec      Run a command in a running container
    export    Stream the contents of a container as a tar archive
    history   Show the history of an image
    images    List images
    import    Create a new filesystem image from the contents of a tarball
    info      Display system-wide information
    inspect   Return low-level information on a container or image
    kill      Kill a running container
    load      Load an image from a tar archive
    login     Register or log in to a Docker registry server
    logout    Log out from a Docker registry server
    logs      Fetch the logs of a container
    pause     Pause all processes within a container
    port      Lookup the public-facing port that is NAT-ed to PRIVATE_PORT
    ps        List containers
    pull      Pull an image or a repository from a Docker registry server
    push      Push an image or a repository to a Docker registry server
    rename    Rename an existing container
    restart   Restart a running container
    rm        Remove one or more containers
    rmi       Remove one or more images
    run       Run a command in a new container
    save      Save an image to a tar archive
    search    Search for an image on the Docker Hub
    start     Start a stopped container
    stats     Display a stream of a containers' resource usage statistics
    stop      Stop a running container
    tag       Tag an image into a repository
    top       Lookup the running processes of a container
    unpause   Unpause a paused container
    version   Show the Docker version information
    wait      Block until a container stops, then print its exit code

Run 'docker COMMAND --help' for more information on a command.
'''
    mock = mocker.patch('subprocess.Popen')
    mock.return_value.stdout = BytesIO(help)
    return mock

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::Cache.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py]
    def __init__(self):
        self._db = None
```
