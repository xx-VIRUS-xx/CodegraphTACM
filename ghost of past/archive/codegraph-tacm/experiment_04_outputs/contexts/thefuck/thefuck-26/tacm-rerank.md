# thefuck-26 :: tacm-rerank

query: Support for either starting only the machine requested, or starting all machines

## selected nodes

- rank=1 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/vagrant_up.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/vagrant_up.py
- rank=2 layer=FUNCTION tokens=275 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py
- rank=3 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_not_command.py::get_docker_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_not_command.py
- rank=4 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cpp11.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cpp11.py
- rank=5 layer=FUNCTION tokens=247 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/whois.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/whois.py
- rank=6 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_adb_unknown_command.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_adb_unknown_command.py
- rank=7 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=8 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_argument file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=9 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/switch_lang.py::_get_matched_layout file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/switch_lang.py
- rank=10 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.put_to_history file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=11 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::color file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py
- rank=12 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py
- rank=13 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::_get_directory_names_only file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py
- rank=14 layer=FUNCTION tokens=1362 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=15 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.is_match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=16 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/npm.py::get_scripts file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/npm.py
- rank=17 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/path_from_history.py::_get_all_absolute_paths_from_history file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/path_from_history.py
- rank=18 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/wrong_hyphen_before_subcommand.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/wrong_hyphen_before_subcommand.py
- rank=19 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=20 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rm_staged.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rm_staged.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cpp11.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cpp11.py]
def match(command):
    return ('This file requires compiler and library support for the '
            'ISO C++ 2011 standard.' in command.output or
            '-Wc++11-extensions' in command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/whois.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/whois.py]
def match(command):
    """
    What the `whois` command returns depends on the 'Whois server' it contacted
    and is not consistent through different servers. But there can be only two
    types of errors I can think of with `whois`:
        - `whois https://en.wikipedia.org/` → `whois en.wikipedia.org`;
        - `whois en.wikipedia.org` → `whois wikipedia.org`.
    So we match any `whois` command and then:
        - if there is a slash: keep only the FQDN;
        - if there is no slash but there is a point: removes the left-most
          subdomain.

    We cannot either remove all subdomains because we cannot know which part is
    the subdomains and which is the domain, consider:
        - www.google.fr → subdomain: www, domain: 'google.fr';
        - google.co.uk → subdomain: None, domain; 'google.co.uk'.
    """
    return True

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_adb_unknown_command.py::output [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_adb_unknown_command.py]
def output():
    return '''Android Debug Bridge version 1.0.31

 -d                            - directs command to the only connected USB device
                                 returns an error if more than one USB device is present.
 -e                            - directs command to the only running emulator.
                                 returns an error if more than one emulator is running.
 -s <specific device>          - directs command to the device or emulator with the given
                                 serial number or qualifier. Overrides ANDROID_SERIAL
                                 environment variable.
'''

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py]
    def patch(vals):
        vals = iter(vals)
        monkeypatch.setattr('thefuck.ui.get_key', lambda: next(vals))

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/switch_lang.py::_get_matched_layout [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/switch_lang.py]
def _get_matched_layout(command):
    # don't use command.split_script here because a layout mismatch will likely
    # result in a non-splitable script as per shlex
    cmd = command.script.split(' ')
    for source_layout in source_layouts:
        is_all_match = True
        for cmd_part in cmd:
            if not all([ch in source_layout or ch in '-_' for ch in cmd_part]):
                is_all_match = False
                break

        if is_all_match:
            return source_layout

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.put_to_history [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py]
    def put_to_history(self, command):
        """Adds fixed command to shell history.

        In most of shells we change history on shell-level, but not
        all shells support it (Fish).

        """

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::color [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py]
def color(color_):
    """Utility for ability to disabling colored output."""
    if settings.no_colors:
        return ''
    else:
        return color_

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell.and_ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py]
    def and_(self, *commands):
        return u' -and '.join('({0})'.format(c) for c in commands)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::_get_directory_names_only [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py]
def _get_directory_names_only(path):
    return [d for d in os.listdir(path)
            if os.path.isdir(os.path.join(path, d))]

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.is_match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
    def is_match(self, command):
        """Returns `True` if rule matches the command.

        :type command: Command
        :rtype: bool

        """
        if command.output is None and self.requires_output:
            return False

        try:
            with logs.debug_time(u'Trying rule: {};'.format(self.name)):
                if self.match(command):
                    return True
        except Exception:
            logs.rule_failed(self, sys.exc_info())

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/npm.py::get_scripts [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/npm.py]
def get_scripts():
    """Get custom npm scripts."""
    proc = Popen(['npm', 'run-script'], stdout=PIPE)
    should_yeild = False
    for line in proc.stdout.readlines():
        line = line.decode()
        if 'available via `npm run-script`:' in line:
            should_yeild = True
            continue

        if should_yeild and re.match(r'^  [^ ]+', line):
            yield line.strip().split(' ')[0]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/path_from_history.py::_get_all_absolute_paths_from_history [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/path_from_history.py]
def _get_all_absolute_paths_from_history(command):
    counter = Counter()

    for line in get_valid_history_without_current(command):
        splitted = shell.split_command(line)

        for param in splitted[1:]:
            if param.startswith('/') or param.startswith('~'):
                if param.endswith('/'):
                    param = param[:-1]

                counter[param] += 1

    return (path for path, _ in counter.most_common(None))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/wrong_hyphen_before_subcommand.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/wrong_hyphen_before_subcommand.py]
def match(command):
    first_part = command.script_parts[0]
    if "-" not in first_part or first_part in get_all_executables():
        return False
    cmd, _ = first_part.split("-", 1)
    return cmd in get_all_executables()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py]
def replace_command(command, broken, matched):
    """Helper for *_no_command rules."""
    new_cmds = get_close_matches(broken, matched, cutoff=0.1)
    return [replace_argument(command.script, broken, new_cmd.strip())
            for new_cmd in new_cmds]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rm_staged.py::output [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rm_staged.py]
def output(target):
    return ('error: the following file has changes staged in the index:\n    {}\n(use '
            '--cached to keep the file, or -f to force removal)').format(target)
```
