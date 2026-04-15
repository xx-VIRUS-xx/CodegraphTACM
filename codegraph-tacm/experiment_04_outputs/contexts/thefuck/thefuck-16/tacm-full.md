# thefuck-16 :: tacm-full

query: #301: Set variables within the alias

## selected nodes

- rank=1 layer=FUNCTION tokens=242 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=2 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=3 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py
- rank=4 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=5 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py
- rank=6 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py
- rank=7 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_argument file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=8 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/alias.py::_get_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/alias.py
- rank=9 layer=FUNCTION tokens=1362 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=10 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py
- rank=11 layer=FUNCTION tokens=1063 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help_new file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=12 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.app_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py]
    def app_alias(self, alias_name):
        # It is VERY important to have the variables declared WITHIN the function
        return '''
            function {name} () {{
                TF_PYTHONIOENCODING=$PYTHONIOENCODING;
                export TF_SHELL=bash;
                export TF_ALIAS={name};
                export TF_SHELL_ALIASES=$(alias);
                export TF_HISTORY=$(fc -ln -10);
                export PYTHONIOENCODING=utf-8;
                TF_CMD=$(
                    thefuck {argument_placeholder} "$@"
                ) && eval "$TF_CMD";
                unset TF_HISTORY;
                export PYTHONIOENCODING=$TF_PYTHONIOENCODING;
                {alter_history}
            }}
        '''.format(
            name=alias_name,
            argument_placeholder=ARGUMENT_PLACEHOLDER,
            alter_history=('history -s $TF_CMD;'
                           if settings.alter_history else ''))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh.app_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py]
    def app_alias(self, alias_name):
        # It is VERY important to have the variables declared WITHIN the function
        return '''
            {name} () {{
                TF_PYTHONIOENCODING=$PYTHONIOENCODING;
                export TF_SHELL=zsh;
                export TF_ALIAS={name};
                TF_SHELL_ALIASES=$(alias);
                export TF_SHELL_ALIASES;
                TF_HISTORY="$(fc -ln -10)";
                export TF_HISTORY;
                export PYTHONIOENCODING=utf-8;
                TF_CMD=$(
                    thefuck {argument_placeholder} $@
                ) && eval $TF_CMD;
                unset TF_HISTORY;
                export PYTHONIOENCODING=$TF_PYTHONIOENCODING;
                {alter_history}
            }}
        '''.format(
            name=alias_name,
            argument_placeholder=ARGUMENT_PLACEHOLDER,
            alter_history=('test -n "$TF_CMD" && print -s $TF_CMD'
                           if settings.alter_history else ''))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py]
    def patch(vals):
        vals = iter(vals)
        monkeypatch.setattr('thefuck.ui.get_key', lambda: next(vals))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.Popen [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py]
    def Popen(self, mocker):
        mock = mocker.patch('thefuck.shells.fish.Popen')
        mock.return_value.stdout.read.side_effect = [(
            b'cd\nfish_config\nfuck\nfunced\nfuncsave\ngrep\nhistory\nll\nls\n'
            b'man\nmath\npopd\npushd\nruby'),
            (b'alias fish_key_reader /usr/bin/fish_key_reader\nalias g git\n'
             b'alias alias_with_equal_sign=echo\ninvalid_alias'), b'func1\nfunc2', b'']
        return mock

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh.app_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py]
    def app_alias(self, alias_name):
        return ("alias {0} 'setenv TF_SHELL tcsh && setenv TF_ALIAS {0} && "
                "set fucked_cmd=`history -h 2 | head -n 1` && "
                "eval `thefuck ${{fucked_cmd}}`'").format(alias_name)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_argument [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py]
def replace_argument(script, from_, to):
    """Replaces command line argument."""
    replaced_in_the_end = re.sub(u' {}$'.format(re.escape(from_)), u' {}'.format(to),
                                 script, count=1)
    if replaced_in_the_end != script:
        return replaced_in_the_end
    else:
        return script.replace(
            u' {} '.format(from_), u' {} '.format(to), 1)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/alias.py::_get_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/alias.py]
def _get_alias(known_args):
    if six.PY2:
        warn("The Fuck will drop Python 2 support soon, more details "
             "https://github.com/nvbn/thefuck/issues/685")

    alias = shell.app_alias(known_args.alias)

    if known_args.enable_experimental_instant_mode:
        if six.PY2:
            warn("Instant mode requires Python 3")
        elif not which('script'):
            warn("Instant mode requires `script` app")
        else:
            return shell.instant_mode_alias(known_args.alias)

    return alias

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py::output [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py]
def output(branch_name):
    if not branch_name:
        return ''
    return '''fatal: The current branch {} has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin {}

'''.format(branch_name, branch_name)

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py]
def get_alias():
    return os.environ.get('TF_ALIAS', 'fuck')
```
