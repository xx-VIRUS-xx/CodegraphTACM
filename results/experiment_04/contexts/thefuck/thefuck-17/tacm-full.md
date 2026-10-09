# thefuck-17 :: tacm-full

query: #402: Don't invoke bash for getting aliases

## selected nodes

- rank=1 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py::TestBash.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py
- rank=2 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py
- rank=3 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=4 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py
- rank=5 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=6 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::_get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=7 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/switch_lang.py::_get_matched_layout file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/switch_lang.py
- rank=8 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish._get_overridden_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=9 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic._expand_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=10 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish._expand_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=11 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_all_executables file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=12 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py::TestBash.shell file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py
- rank=13 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.how_to_configure file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=14 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash._get_version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=15 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py::get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py
- rank=16 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=17 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=18 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash._get_history_file_name file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=19 layer=FUNCTION tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/git.py::git_support file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/git.py
- rank=20 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_zsh.py::TestZsh.shell_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_zsh.py
- rank=21 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py::TestBash.shell_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py
- rank=22 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=23 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh._parse_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py
- rank=24 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py
- rank=25 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::color file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py
- rank=26 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.from_shell file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=27 layer=FUNCTION tokens=348 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push.py
- rank=28 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=29 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py::how_to_configure file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py
- rank=30 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py::Settings.init file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py
- rank=31 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/tsuru_not_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/tsuru_not_command.py
- rank=32 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/npm.py::get_scripts file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/npm.py
- rank=33 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py::_Shelve.get file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py
- rank=34 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py::TestBash.Popen [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py]
    def Popen(self, mocker):
        mock = mocker.patch('thefuck.shells.bash.Popen')
        return mock

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh.get_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py]
    def get_aliases(self):
        proc = Popen(['tcsh', '-ic', 'alias'], stdout=PIPE, stderr=DEVNULL)
        return dict(
            self._parse_alias(alias)
            for alias in proc.stdout.read().decode('utf-8').split('\n')
            if alias and '\t' in alias)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.get_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py]
    def get_aliases(self):
        raw_aliases = os.environ.get('TF_SHELL_ALIASES', '').split('\n')
        return dict(self._parse_alias(alias)
                    for alias in raw_aliases if alias and '=' in alias)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh.get_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py]
    def get_aliases(self):
        raw_aliases = os.environ.get('TF_SHELL_ALIASES', '').split('\n')
        return dict(self._parse_alias(alias)
                    for alias in raw_aliases if alias and '=' in alias)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.get_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py]

    def get_aliases(self):
        overridden = self._get_overridden_aliases()
        functions = _get_functions(overridden)
        raw_aliases = _get_aliases(overridden)
        functions.update(raw_aliases)

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish._get_overridden_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py]

    def _get_overridden_aliases(self):
        overridden = os.environ.get('THEFUCK_OVERRIDDEN_ALIASES',
                                    os.environ.get('TF_OVERRIDDEN_ALIASES', ''))
        default = {'cd', 'grep', 'ls', 'man', 'open'}
        for alias in overridden.split(','):
            default.add(alias.strip())

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic._expand_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py]
    def _expand_aliases(self, command_script):
        aliases = self.get_aliases()
        binary = command_script.split(' ')[0]
        if binary in aliases:
            return command_script.replace(binary, aliases[binary], 1)
        else:
            return command_script

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish._expand_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py]

    def _expand_aliases(self, command_script):
        aliases = self.get_aliases()
        binary = command_script.split(' ')[0]
        if binary in aliases and aliases[binary] != binary:
            return command_script.replace(binary, aliases[binary], 1)
        elif binary in aliases:
            return u'fish -ic "{}"'.format(command_script.replace('"', r'\"'))
        else:

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py::TestBash.shell [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py]
    def shell(self):
        return Bash()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.how_to_configure [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py]
    def how_to_configure(self):
        if os.path.join(os.path.expanduser('~'), '.bashrc'):
            config = '~/.bashrc'
        elif os.path.join(os.path.expanduser('~'), '.bash_profile'):
            config = '~/.bash_profile'
        else:
            config = 'bash config'

        return self._create_shell_configuration(
            content=u'eval "$(thefuck --alias)"',
            path=config,
            reload=u'source {}'.format(config))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash._get_version [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py]
    def _get_version(self):
        """Returns the version of the current shell"""
        proc = Popen(['bash', '-c', 'echo $BASH_VERSION'],
                     stdout=PIPE, stderr=DEVNULL)
        return proc.stdout.read().decode('utf-8').strip()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py::get_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py]
def get_aliases(mocker):
    mocker.patch('thefuck.shells.shell.get_aliases',
                 return_value=['vim', 'apt-get', 'fsck', 'fuck'])

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.get_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py]
    def get_aliases(self):
        return {}

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py]
    def patch(vals):
        vals = iter(vals)
        monkeypatch.setattr('thefuck.ui.get_key', lambda: next(vals))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash._get_history_file_name [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py]
    def _get_history_file_name(self):
        return os.environ.get("HISTFILE",
                              os.path.expanduser('~/.bash_history'))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/git.py::git_support [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/git.py]
def git_support(fn, command):
    """Resolves git aliases and supports testing for both git and hub."""
    # supports GitHub's `hub` command
    # which is recommended to be used with `alias git=hub`
    # but at this point, shell aliases have already been resolved
    if not is_app(command, 'git', 'hub'):
        return False

    # perform git aliases expansion
    if command.output and 'trace: alias expansion:' in command.output:
        search = re.search("trace: alias expansion: ([^ ]*) => ([^\n]*)",
                           command.output)
        alias = search.group(1)

        # by default git quotes everything, for example:
        #     'commit' '--amend'
        # which is surprising and does not allow to easily test for
        # eg. 'git commit'
        expansion = ' '.join(shell.quote(part)
                             for part in shell.split_command(search.group(2)))
        new_script = re.sub(r"\b{}\b".format(alias), expansion, command.script)

        command = command.update(script=new_script)

    return fn(command)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_zsh.py::TestZsh.shell_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_zsh.py]
    def shell_aliases(self):
        os.environ['TF_SHELL_ALIASES'] = (
            'fuck=\'eval $(thefuck $(fc -ln -1 | tail -n 1))\'\n'
            'l=\'ls -CF\'\n'
            'la=\'ls -A\'\n'
            'll=\'ls -alF\'')

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py::TestBash.shell_aliases [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py]
    def shell_aliases(self):
        os.environ['TF_SHELL_ALIASES'] = (
            'alias fuck=\'eval $(thefuck $(fc -ln -1))\'\n'
            'alias l=\'ls -CF\'\n'
            'alias la=\'ls -A\'\n'
            'alias ll=\'ls -alF\'')

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh._parse_alias [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py]
    def _parse_alias(self, alias):
        name, value = alias.split("\t", 1)
        return name, value

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell.and_ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py]
    def and_(self, *commands):
        return u' -and '.join('({0})'.format(c) for c in commands)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::color [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py]
def color(color_):
    """Utility for ability to disabling colored output."""
    if settings.no_colors:
        return ''
    else:
        return color_

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.from_shell [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py]
    def from_shell(self, command_script):
        """Prepares command before running in app."""
        return self._expand_aliases(command_script)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push.py]
def get_new_command(command):
    # If --set-upstream or -u are passed, remove it and its argument. This is
    # because the remaining arguments are concatenated onto the command suggested
    # by git, which includes --set-upstream and its argument
    command_parts = command.script_parts[:]
    upstream_option_index = _get_upstream_option_index(command_parts)

    if upstream_option_index is not None:
        command_parts.pop(upstream_option_index)

        # In case of `git push -u` we don't have next argument:
        if len(command_parts) > upstream_option_index:
            command_parts.pop(upstream_option_index)
    else:
        # the only non-qualified permitted options are the repository and refspec; git's
        # suggestion include them, so they won't be lost, but would be duplicated otherwise.
        push_idx = command_parts.index('push') + 1
        while len(command_parts) > push_idx and command_parts[len(command_parts) - 1][0] != '-':
            command_parts.pop(len(command_parts) - 1)

    arguments = re.findall(r'git push (.*)', command.output)[-1].replace("'", r"\'").strip()
    return replace_argument(" ".join(command_parts), 'push',
                            'push {}'.format(arguments))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py]
def replace_command(command, broken, matched):
    """Helper for *_no_command rules."""
    new_cmds = get_close_matches(broken, matched, cutoff=0.1)
    return [replace_argument(command.script, broken, new_cmd.strip())
            for new_cmd in new_cmds]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py::how_to_configure [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py]
def how_to_configure(proc, TIMEOUT):
    proc.sendline(u'fuck')
    assert proc.expect([TIMEOUT, u"alias isn't configured"])

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py::Settings.init [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py]
    def init(self, args=None):
        """Fills `settings` with values from `settings.py` and env."""
        from .logs import exception

        self._setup_user_dir()
        self._init_settings_file()

        try:
            self.update(self._settings_from_file())
        except Exception:
            exception("Can't load settings from file", sys.exc_info())

        try:
            self.update(self._settings_from_env())
        except Exception:
            exception("Can't load settings from env", sys.exc_info())

        self.update(self._settings_from_args(args))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/tsuru_not_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/tsuru_not_command.py]
def match(command):
    return (' is not a tsuru command. See "tsuru help".' in command.output
            and '\nDid you mean?\n\t' in command.output)

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py::_Shelve.get [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py]
            def get(self, k, v=None):
                return value.get(k, v)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.and_ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py]

    def and_(self, *commands):
```
