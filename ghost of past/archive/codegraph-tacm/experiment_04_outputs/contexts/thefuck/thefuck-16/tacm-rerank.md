# thefuck-16 :: tacm-rerank

query: #301: Set variables within the alias

## selected nodes

- rank=1 layer=FUNCTION tokens=242 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=2 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=3 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py
- rank=4 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py
- rank=5 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=6 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=7 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py
- rank=8 layer=FUNCTION tokens=231 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_valid_history_without_current file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=9 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=10 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py
- rank=11 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::_get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=12 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/alias.py::_get_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/alias.py
- rank=13 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_argument file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=14 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.is_match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=15 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand.run file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=16 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py
- rank=17 layer=FUNCTION tokens=1063 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help_new file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=18 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py::output_bitbucket file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py
- rank=19 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_all_executables file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=20 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.instant_mode_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh.app_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py]
    def app_alias(self, alias_name):
        return ("alias {0} 'setenv TF_SHELL tcsh && setenv TF_ALIAS {0} && "
                "set fucked_cmd=`history -h 2 | head -n 1` && "
                "eval `thefuck ${{fucked_cmd}}`'").format(alias_name)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.app_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py]
    def app_alias(self, alias_name):
        return """alias {0}='eval "$(TF_ALIAS={0} PYTHONIOENCODING=utf-8 """ \
               """thefuck "$(fc -ln -1)")"'""".format(alias_name)

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_valid_history_without_current [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py]
def get_valid_history_without_current(command):
    def _not_corrected(history, tf_alias):
        """Returns all lines from history except that comes before `fuck`."""
        previous = None
        for line in history:
            if previous is not None and line != tf_alias:
                yield previous
            previous = line
        if history:
            yield history[-1]

    from thefuck.shells import shell
    history = shell.get_history()
    tf_alias = get_alias()
    executables = set(get_all_executables())\
        .union(shell.get_builtin_commands())

    return [line for line in _not_corrected(history, tf_alias)
            if not line.startswith(tf_alias) and not line == command.script
            and line.split(' ')[0] in executables]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py]
def get_alias():
    return os.environ.get('TF_ALIAS', 'fuck')

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh.get_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py]
    def get_aliases(self):
        proc = Popen(['tcsh', '-ic', 'alias'], stdout=PIPE, stderr=DEVNULL)
        return dict(
            self._parse_alias(alias)
            for alias in proc.stdout.read().decode('utf-8').split('\n')
            if alias and '\t' in alias)

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand.run [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
    def run(self, old_cmd):
        """Runs command from rule for passed command.

        :type old_cmd: Command

        """
        if self.side_effect:
            self.side_effect(old_cmd, self.script)
        if settings.alter_history:
            shell.put_to_history(self.script)
        # This depends on correct setting of PYTHONIOENCODING by the alias:
        logs.debug(u'PYTHONIOENCODING: {}'.format(
            os.environ.get('PYTHONIOENCODING', '!!not-set!!')))

        sys.stdout.write(self._get_script())

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py::output_bitbucket [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py]
def output_bitbucket():
    return '''Total 0 (delta 0), reused 0 (delta 0)
remote:
remote: Create pull request for feature/set-upstream:
remote:   https://bitbucket.org/set-upstream
remote:
To git@bitbucket.org:test.git
   e5e7fbb..700d998  feature/set-upstream -> feature/set-upstream
Branch feature/set-upstream set up to track remote branch feature/set-upstream from origin.
'''

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_all_executables [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py]
def get_all_executables():
    from thefuck.shells import shell

    def _safe(fn, fallback):
        try:
            return fn()
        except OSError:
            return fallback

    tf_alias = get_alias()
    tf_entry_points = ['thefuck', 'fuck']

    bins = [exe.name.decode('utf8') if six.PY2 else exe.name
            for path in os.environ.get('PATH', '').split(os.pathsep)
            if include_path_in_search(path)
            for exe in _safe(lambda: list(Path(path).iterdir()), [])
            if not _safe(exe.is_dir, True)
            and exe.name not in tf_entry_points]
    aliases = [alias.decode('utf8') if six.PY2 else alias
               for alias in shell.get_aliases() if alias != tf_alias]

    return bins + aliases

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.instant_mode_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py]
    def instant_mode_alias(self, alias_name):
        warn("Instant mode not supported by your shell")
        return self.app_alias(alias_name)
```
