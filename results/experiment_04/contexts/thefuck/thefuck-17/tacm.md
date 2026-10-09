# thefuck-17 :: tacm

query: #402: Don't invoke bash for getting aliases

## selected nodes

- rank=1 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=2 layer=FILE tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=3 layer=FILE tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=4 layer=FILE tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/const.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/const.py
- rank=5 layer=CLASS tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=6 layer=CLASS tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=7 layer=CLASS tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py::TestBash file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py
- rank=8 layer=CLASS tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=9 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=10 layer=CLASS tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py
- rank=11 layer=CLASS tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py
- rank=12 layer=CLASS tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py
- rank=13 layer=CLASS tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_zsh.py::TestZsh file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_zsh.py
- rank=14 layer=CLASS tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::Cache file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=15 layer=CLASS tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_tcsh.py::TestTcsh file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_tcsh.py
- rank=16 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=17 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py
- rank=18 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py::TestBash.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py
- rank=19 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py
- rank=20 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=21 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::_get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=22 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish._get_overridden_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=23 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_all_executables file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=24 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic._expand_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=25 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish._expand_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=26 layer=FUNCTION tokens=11 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=27 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash._get_version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=28 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.how_to_configure file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=29 layer=FUNCTION tokens=232 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=30 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash._get_history_file_name file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=31 layer=FUNCTION tokens=10 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py::TestBash.shell file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py
- rank=32 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_zsh.py::TestZsh.shell_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_zsh.py
- rank=33 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py::TestBash.shell_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_bash.py
- rank=34 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=35 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=36 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_argument file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=37 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash._get_history_line file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=38 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py::Tcsh._parse_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/tcsh.py
- rank=39 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py
- rank=40 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_tcsh.py::TestTcsh.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_tcsh.py
- rank=41 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.from_shell file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=42 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/switch_lang.py::_get_matched_layout file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/switch_lang.py
- rank=43 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash._parse_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=44 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_zsh.py::TestZsh.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_zsh.py
- rank=45 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=46 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=47 layer=FUNCTION tokens=249 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh.app_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py
- rank=48 layer=FUNCTION tokens=194 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py::Bash.instant_mode_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/bash.py
- rank=49 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::which file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=50 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::for_app file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=51 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py::get_aliases file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py
- rank=52 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_all_matched_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=53 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py
- rank=54 layer=FUNCTION tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::color file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py
- rank=55 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=56 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.or_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py

## context

```text
file thefuck/shells/bash.py
imports: os, subprocess, tempfile, uuid, conf, const, utils, generic
defines: Bash

file thefuck/shells/fish.py
imports: subprocess, time, os, sys, six, conf, const, utils
defines: Fish, _get_functions, _get_aliases

file thefuck/thefuck/utils.py
imports: atexit, os, pickle, re, shelve, sys, six, decorator
defines: Cache, memoize, wrapper, which, is_exe, default_settings, _default_settings, get_closest, get_close_matches, include_path_in_search, get_all_executables, _safe, replace_argument, eager, get_all_matched_commands, replace_command, is_app, for_app, _for_app, cache, cache_decorator, wrapper, get_installation_version, get_alias, get_valid_history_without_current, _not_corrected, format_raw_script

file thefuck/thefuck/const.py
imports: —
defines: _GenConst

class Bash(Generic):  [thefuck/shells/bash.py:11]
methods: _get_history_file_name, _get_history_line, _get_version
         _parse_alias, app_alias, get_aliases
         how_to_configure, instant_mode_alias

class Fish(Generic):  [thefuck/shells/fish.py:40]
methods: _expand_aliases, _get_history_file_name, _get_history_line
         _get_overridden_aliases, _get_version
         _put_to_history, _script_from_history, and_
         app_alias, get_aliases, how_to_configure, or_
         put_to_history

class TestBash(object):  [tests/shells/test_bash.py:9]
methods: Popen, shell, shell_aliases, test_and_, test_app_alias
         test_app_alias_variables_correctly_set
         test_from_shell, test_get_aliases
         test_get_history, test_get_version_error
         test_how_to_configure
         test_how_to_configure_when_config_not_found
         test_info, test_or_, test_split_command
         test_to_shell

class Generic(object):  [thefuck/shells/generic.py:16]
methods: _create_shell_configuration, _expand_aliases
         _get_history_file_name, _get_history_line
         _get_history_lines, _get_version
         _script_from_history, and_, app_alias
         decode_utf8, encode_utf8, from_shell, get_aliases
         get_builtin_commands, get_history
         how_to_configure, info, instant_mode_alias, or_
         put_to_history, quote, split_command, to_shell

class CorrectedCommand(object):  [thefuck/thefuck/types.py:201]
methods: _get_script, run, __eq__, __hash__, __init__, __repr__

class TestFish(object):  [tests/shells/test_fish.py:9]
methods: Popen, shell, test_and_, test_app_alias
         test_app_alias_alter_history, test_from_shell
         test_get_aliases, test_get_history
         test_get_overridden_aliases, test_get_version
         test_get_version_error, test_how_to_configure
         test_how_to_configure_when_config_not_found
         test_or_, test_put_to_history, test_to_shell

class Zsh(Generic):  [thefuck/shells/zsh.py:12]
methods: _get_history_file_name, _get_history_line, _get_version
         _parse_alias, _script_from_history, app_alias
         get_aliases, how_to_configure, instant_mode_alias

class Tcsh(Generic):  [thefuck/shells/tcsh.py:8]
methods: _get_history_file_name, _get_history_line, _get_version
         _parse_alias, app_alias, get_aliases
         how_to_configure

class TestZsh(object):  [tests/shells/test_zsh.py:9]
methods: Popen, shell, shell_aliases, test_and_, test_app_alias
         test_app_alias_variables_correctly_set
         test_from_shell, test_get_aliases
         test_get_history, test_get_version_error
         test_how_to_configure
         test_how_to_configure_when_config_not_found
         test_info, test_or_, test_to_shell

class Cache(object):  [thefuck/thefuck/utils.py:199]
methods: _get_cache_dir, _get_key, _get_mtime, _init_db, _setup_db
         get_value, __init__

class TestTcsh(object):  [tests/shells/test_tcsh.py:8]
methods: Popen, shell, test_and_, test_app_alias, test_from_shell
         test_get_aliases, test_get_history
         test_get_version_error, test_how_to_configure
         test_how_to_configure_when_config_not_found
         test_info, test_or_, test_to_shell

    def get_aliases(self):
        raw_aliases = os.environ.get('TF_SHELL_ALIASES', '').split('\n')
        return dict(self._parse_alias(alias)
                    for alias in raw_aliases if alias and '=' in alias)

    def get_aliases(self):
        proc = Popen(['tcsh', '-ic', 'alias'], stdout=PIPE, stderr=DEVNULL)
        return dict(
            self._parse_alias(alias)
            for alias in proc.stdout.read().decode('utf-8').split('\n')
            if alias and '\t' in alias)

    def Popen(self, mocker):
        mock = mocker.patch('thefuck.shells.bash.Popen')
        return mock

    def get_aliases(self):
        raw_aliases = os.environ.get('TF_SHELL_ALIASES', '').split('\n')
        return dict(self._parse_alias(alias)
                    for alias in raw_aliases if alias and '=' in alias)


    def get_aliases(self):
        overridden = self._get_overridden_aliases()
        functions = _get_functions(overridden)
        raw_aliases = _get_aliases(overridden)
        functions.update(raw_aliases)

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


    def _get_overridden_aliases(self):
        overridden = os.environ.get('THEFUCK_OVERRIDDEN_ALIASES',
                                    os.environ.get('TF_OVERRIDDEN_ALIASES', ''))
        default = {'cd', 'grep', 'ls', 'man', 'open'}
        for alias in overridden.split(','):
            default.add(alias.strip())

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

    def _expand_aliases(self, command_script):
        aliases = self.get_aliases()
        binary = command_script.split(' ')[0]
        if binary in aliases:
            return command_script.replace(binary, aliases[binary], 1)
        else:
            return command_script


    def _expand_aliases(self, command_script):
        aliases = self.get_aliases()
        binary = command_script.split(' ')[0]
        if binary in aliases and aliases[binary] != binary:
            return command_script.replace(binary, aliases[binary], 1)
        elif binary in aliases:
            return u'fish -ic "{}"'.format(command_script.replace('"', r'\"'))
        else:

    def get_aliases(self):
        return {}

    def _get_version(self):
        """Returns the version of the current shell"""
        proc = Popen(['bash', '-c', 'echo $BASH_VERSION'],
                     stdout=PIPE, stderr=DEVNULL)
        return proc.stdout.read().decode('utf-8').strip()

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

    def _get_history_file_name(self):
        return os.environ.get("HISTFILE",
                              os.path.expanduser('~/.bash_history'))

    def shell(self):
        return Bash()

    def shell_aliases(self):
        os.environ['TF_SHELL_ALIASES'] = (
            'fuck=\'eval $(thefuck $(fc -ln -1 | tail -n 1))\'\n'
            'l=\'ls -CF\'\n'
            'la=\'ls -A\'\n'
            'll=\'ls -alF\'')

    def shell_aliases(self):
        os.environ['TF_SHELL_ALIASES'] = (
            'alias fuck=\'eval $(thefuck $(fc -ln -1))\'\n'
            'alias l=\'ls -CF\'\n'
            'alias la=\'ls -A\'\n'
            'alias ll=\'ls -alF\'')

def replace_command(command, broken, matched):
    """Helper for *_no_command rules."""
    new_cmds = get_close_matches(broken, matched, cutoff=0.1)
    return [replace_argument(command.script, broken, new_cmd.strip())
            for new_cmd in new_cmds]

    def patch(vals):
        vals = iter(vals)
        monkeypatch.setattr('thefuck.ui.get_key', lambda: next(vals))

def replace_argument(script, from_, to):
    """Replaces command line argument."""
    replaced_in_the_end = re.sub(u' {}$'.format(re.escape(from_)), u' {}'.format(to),
                                 script, count=1)
    if replaced_in_the_end != script:
        return replaced_in_the_end
    else:
        return script.replace(
            u' {} '.format(from_), u' {} '.format(to), 1)

    def _get_history_line(self, command_script):
        return u'{}\n'.format(command_script)

    def _parse_alias(self, alias):
        name, value = alias.split("\t", 1)
        return name, value

    def Popen(self, mocker):
        mock = mocker.patch('thefuck.shells.fish.Popen')
        mock.return_value.stdout.read.side_effect = [(
            b'cd\nfish_config\nfuck\nfunced\nfuncsave\ngrep\nhistory\nll\nls\n'
            b'man\nmath\npopd\npushd\nruby'),
            (b'alias fish_key_reader /usr/bin/fish_key_reader\nalias g git\n'
             b'alias alias_with_equal_sign=echo\ninvalid_alias'), b'func1\nfunc2', b'']
        return mock

    def Popen(self, mocker):
        mock = mocker.patch('thefuck.shells.tcsh.Popen')
        mock.return_value.stdout.read.return_value = (
            b'fuck\teval $(thefuck $(fc -ln -1))\n'
            b'l\tls -CF\n'
            b'la\tls -A\n'
            b'll\tls -alF')
        return mock

    def from_shell(self, command_script):
        """Prepares command before running in app."""
        return self._expand_aliases(command_script)

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

    def _parse_alias(self, alias):
        name, value = alias.replace('alias ', '', 1).split('=', 1)
        if value[0] == value[-1] == '"' or value[0] == value[-1] == "'":
            value = value[1:-1]
        return name, value

    def Popen(self, mocker):
        mock = mocker.patch('thefuck.shells.zsh.Popen')
        return mock

    def and_(self, *commands):
        return u' && '.join(commands)


    def and_(self, *commands):

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

    def instant_mode_alias(self, alias_name):
        if os.environ.get('THEFUCK_INSTANT_MODE', '').lower() == 'true':
            mark = USER_COMMAND_MARK + '\b' * len(USER_COMMAND_MARK)
            return '''
                export PS1="{user_command_mark}$PS1";
                {app_alias}
            '''.format(user_command_mark=mark,
                       app_alias=self.app_alias(alias_name))
        else:
            log_path = os.path.join(
                gettempdir(), 'thefuck-script-log-{}'.format(uuid4().hex))
            return '''
                export THEFUCK_INSTANT_MODE=True;
                export THEFUCK_OUTPUT_LOG={log};
                thefuck --shell-logger {log};
                rm {log};
                exit
            '''.format(log=log_path)

def which(program):
    """Returns `program` path or `None`."""
    try:
        from shutil import which

        return which(program)
    except ImportError:
        def is_exe(fpath):
            return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

        fpath, fname = os.path.split(program)
        if fpath:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                path = path.strip('"')
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file

        return None

def for_app(*app_names, **kwargs):
    """Specifies that matching script is for one of app names."""
    def _for_app(fn, command):
        if is_app(command, *app_names, **kwargs):
            return fn(command)
        else:
            return False

    return decorator(_for_app)

def get_aliases(mocker):
    mocker.patch('thefuck.shells.shell.get_aliases',
                 return_value=['vim', 'apt-get', 'fsck', 'fuck'])

def get_all_matched_commands(stderr, separator='Did you mean'):
    if not isinstance(separator, list):
        separator = [separator]
    should_yield = False
    for line in stderr.split('\n'):
        for sep in separator:
            if sep in line:
                should_yield = True
                break
        else:
            if should_yield and line:
                yield line.strip()

    def and_(self, *commands):
        return u' -and '.join('({0})'.format(c) for c in commands)

def color(color_):
    """Utility for ability to disabling colored output."""
    if settings.no_colors:
        return ''
    else:
        return color_

def get_alias():
    return os.environ.get('TF_ALIAS', 'fuck')


    def or_(self, *commands):
```
