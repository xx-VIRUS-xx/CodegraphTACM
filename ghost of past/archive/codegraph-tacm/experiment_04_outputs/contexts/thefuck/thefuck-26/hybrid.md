# thefuck-26 :: hybrid

query: Support for either starting only the machine requested, or starting all machines

## selected nodes

- rank=1 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/vagrant_up.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/vagrant_up.py
- rank=2 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/wrong_hyphen_before_subcommand.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/wrong_hyphen_before_subcommand.py
- rank=3 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/choco_install.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/choco_install.py
- rank=4 layer=FUNCTION tokens=1362 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=5 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/missing_space_before_subcommand.py::_get_executable file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/missing_space_before_subcommand.py
- rank=6 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/ssh_known_hosts.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/ssh_known_hosts.py
- rank=7 layer=FUNCTION tokens=289 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::_get_brew_tap_specific_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py
- rank=8 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_not_found.py::_get_all_tasks file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_not_found.py
- rank=9 layer=FUNCTION tokens=1063 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help_new file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=10 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.is_enabled file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=11 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::_get_directory_names_only file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py
- rank=12 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/grunt_task_not_found.py::_get_all_tasks file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/grunt_task_not_found.py
- rank=13 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_0flag.py::first_0flag file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_0flag.py
- rank=14 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cpp11.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cpp11.py
- rank=15 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_no_command.py::get_all_executables file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_no_command.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/wrong_hyphen_before_subcommand.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/wrong_hyphen_before_subcommand.py]
def match(command):
    first_part = command.script_parts[0]
    if "-" not in first_part or first_part in get_all_executables():
        return False
    cmd, _ = first_part.split("-", 1)
    return cmd in get_all_executables()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/choco_install.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/choco_install.py]
def match(command):
    return ((command.script.startswith('choco install') or 'cinst' in command.script_parts)
            and 'Installing the following packages' in command.output)

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/missing_space_before_subcommand.py::_get_executable [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/missing_space_before_subcommand.py]
def _get_executable(script_part):
    for executable in get_all_executables():
        if len(executable) > 1 and script_part.startswith(executable):
            return executable

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/ssh_known_hosts.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/ssh_known_hosts.py]
def match(command):
    if not command.script:
        return False
    if not command.script.startswith(commands):
        return False

    patterns = (
        r'WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!',
        r'WARNING: POSSIBLE DNS SPOOFING DETECTED!',
        r"Warning: the \S+ host key for '([^']+)' differs from the key for the IP address '([^']+)'",
    )

    return any(re.findall(pattern, command.output) for pattern in patterns)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::_get_brew_tap_specific_commands [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py]
def _get_brew_tap_specific_commands(brew_path_prefix):
    """To get tap's specific commands
    https://github.com/Homebrew/homebrew/blob/master/Library/brew.rb#L115"""
    commands = []
    brew_taps_path = brew_path_prefix + TAP_PATH

    for user in _get_directory_names_only(brew_taps_path):
        taps = _get_directory_names_only(brew_taps_path + '/%s' % user)

        # Brew Taps's naming rule
        # https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/brew-tap.md#naming-conventions-and-limitations
        taps = (tap for tap in taps if tap.startswith('homebrew-'))
        for tap in taps:
            tap_cmd_path = brew_taps_path + TAP_CMD_PATH % (user, tap)

            if os.path.isdir(tap_cmd_path):
                commands += (name.replace('brew-', '').replace('.rb', '')
                             for name in os.listdir(tap_cmd_path)
                             if _is_brew_tap_cmd_naming(name))

    return commands

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_not_found.py::_get_all_tasks [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_not_found.py]
def _get_all_tasks():
    proc = Popen(['yarn', '--help'], stdout=PIPE)
    should_yield = False
    for line in proc.stdout.readlines():
        line = line.decode().strip()

        if 'Commands:' in line:
            should_yield = True
            continue

        if should_yield and '- ' in line:
            yield line.split(' ')[-1]

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.is_enabled [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
    def is_enabled(self):
        """Returns `True` when rule enabled.

        :rtype: bool

        """
        return (
            self.name in settings.rules
            or self.enabled_by_default
            and ALL_ENABLED in settings.rules
        )

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::_get_directory_names_only [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py]
def _get_directory_names_only(path):
    return [d for d in os.listdir(path)
            if os.path.isdir(os.path.join(path, d))]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/grunt_task_not_found.py::_get_all_tasks [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/grunt_task_not_found.py]
def _get_all_tasks():
    proc = Popen(['grunt', '--help'], stdout=PIPE)
    should_yield = False
    for line in proc.stdout.readlines():
        line = line.decode().strip()

        if 'Available tasks' in line:
            should_yield = True
            continue

        if should_yield and not line:
            return

        if '  ' in line:
            yield line.split(' ')[0]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_0flag.py::first_0flag [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_0flag.py]
def first_0flag(script_parts):
    return next((p for p in script_parts if len(p) == 2 and p.startswith("0")), None)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cpp11.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cpp11.py]
def match(command):
    return ('This file requires compiler and library support for the '
            'ISO C++ 2011 standard.' in command.output or
            '-Wc++11-extensions' in command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_no_command.py::get_all_executables [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_no_command.py]
def get_all_executables(mocker):
    mocker.patch('thefuck.rules.no_command.get_all_executables',
                 return_value=['vim', 'fsck', 'git', 'go', 'python'])
```
