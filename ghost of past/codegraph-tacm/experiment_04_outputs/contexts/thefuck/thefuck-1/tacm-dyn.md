# thefuck-1 :: tacm-dyn

query: #1047: Fix pip_unknown_command by using a less restrictive regex

## selected nodes

- rank=1 layer=FILE tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py
- rank=2 layer=CLASS tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/entrypoints/test_fix_command.py::TestGetRawCommand file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/entrypoints/test_fix_command.py
- rank=3 layer=FUNCTION tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py
- rank=4 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py::pip_unknown_cmd_without_recommend file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py
- rank=5 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py::pip_unknown_cmd file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py
- rank=6 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=7 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py
- rank=8 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=9 layer=FUNCTION tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py::_parse_operations file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py
- rank=10 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py::fix_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=11 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=12 layer=FILE tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py
- rank=13 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py
- rank=14 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py
- rank=15 layer=CLASS tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=16 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.split_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=17 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=18 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=19 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=20 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py
- rank=21 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py
- rank=22 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py
- rank=23 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py::_get_unknown_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py
- rank=24 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py
- rank=25 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand.run file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=26 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py
- rank=27 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py
- rank=28 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py
- rank=29 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_reinstall.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_reinstall.py
- rank=30 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_image_being_used_by_container.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_image_being_used_by_container.py
- rank=31 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py::_get_raw_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=32 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py::brew_unknown_cmd2 file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py
- rank=33 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py::brew_unknown_cmd file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py
- rank=34 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=35 layer=FILE tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_image_being_used_by_container.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_image_being_used_by_container.py
- rank=36 layer=FILE tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py
- rank=37 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gradle_no_task.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gradle_no_task.py
- rank=38 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/grunt_task_not_found.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/grunt_task_not_found.py
- rank=39 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/nixos_cmd_not_found.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/nixos_cmd_not_found.py
- rank=40 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_not_found.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_not_found.py
- rank=41 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py
- rank=42 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=43 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_file.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_file.py
- rank=44 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_file.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_file.py
- rank=45 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_module_error.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_module_error.py
- rank=46 layer=FILE tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/adb_unknown_command.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/adb_unknown_command.py
- rank=47 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/adb_unknown_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/adb_unknown_command.py
- rank=48 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/go_unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/go_unknown_command.py
- rank=49 layer=FILE tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_alt_space.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_alt_space.py
- rank=50 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py
- rank=51 layer=FILE tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py
- rank=52 layer=FUNCTION tokens=238 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py::main file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/main.py
- rank=53 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Command.from_raw_script file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=54 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py
- rank=55 layer=FILE tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py
- rank=56 layer=FUNCTION tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py
- rank=57 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py
- rank=58 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/long_form_help.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/long_form_help.py
- rank=59 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/systemctl.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/systemctl.py
- rank=60 layer=FUNCTION tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_ag_literal.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_ag_literal.py
- rank=61 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_argument file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=62 layer=FILE tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/port_already_in_use.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/port_already_in_use.py
- rank=63 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/port_already_in_use.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/port_already_in_use.py
- rank=64 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/port_already_in_use.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/port_already_in_use.py
- rank=65 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/port_already_in_use.py::_get_pid_by_port file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/port_already_in_use.py
- rank=66 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.instant_mode_alias file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=67 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py
- rank=68 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_missing.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_missing.py
- rank=69 layer=FUNCTION tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py
- rank=70 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/mvn_unknown_lifecycle_phase.py::_get_failed_lifecycle file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/mvn_unknown_lifecycle_phase.py
- rank=71 layer=FILE tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/output_readers/read_log.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/output_readers/read_log.py
- rank=72 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/nixos_cmd_not_found.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/nixos_cmd_not_found.py
- rank=73 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py

## context

```text
file thefuck/rules/pip_unknown_command.py
imports: re, thefuck
defines: match, get_new_command

class TestGetRawCommand(object):  [tests/entrypoints/test_fix_command.py:6]
methods: test_from_command_argument
         test_from_force_command_argument, test_from_history

def match(command):
    return ('pip' in command.script and
            'unknown command' in command.output and
            'maybe you meant' in command.output)

def pip_unknown_cmd_without_recommend():
    return '''ERROR: unknown command "i"'''

def pip_unknown_cmd(broken, suggested):
    return 'ERROR: unknown command "{}" - maybe you meant "{}"'.format(broken, suggested)

    def patch(vals):
        vals = iter(vals)
        monkeypatch.setattr('thefuck.ui.get_key', lambda: next(vals))

def get_new_command(command):
    broken_cmd = re.findall(r'ERROR: unknown command "([^"]+)"',
                            command.output)[0]
    new_cmd = re.findall(r'maybe you meant "([^"]+)"', command.output)[0]

    return replace_argument(command.script, broken_cmd, new_cmd)

file thefuck/entrypoints/fix_command.py
imports: pprint, os, sys, difflib, conf, corrector, exceptions, ui
defines: _get_raw_command, fix_command

def _parse_operations(help_text_lines):
    operation_regex = re.compile(r'^([a-z-]+) +', re.MULTILINE)
    return operation_regex.findall(help_text_lines)

def fix_command(known_args):
    """Fixes previous command. Used when `thefuck` called without arguments."""
    settings.init(known_args)
    with logs.debug_time('Total'):
        logs.debug(u'Run with settings: {}'.format(pformat(settings)))
        raw_command = _get_raw_command(known_args)

        try:
            command = types.Command.from_raw_script(raw_command)
        except EmptyCommand:
            logs.debug('Empty command, nothing to do')
            return

        corrected_commands = get_corrected_commands(command)
        selected_command = select_command(corrected_commands)

        if selected_command:
            selected_command.run(command)
        else:
            sys.exit(1)

def get_new_command(command):
    mistake = re.search(MISTAKE, command.output).group(0)
    fix = re.search(FIX, command.output).group(0)
    return command.script.replace(mistake, fix)

file thefuck/rules/pip_install.py
imports: thefuck
defines: match, get_new_command

def match(command):
    return ('pip install' in command.script and 'Permission denied' in command.output)

def get_new_command(command):
    if '--user' not in command.script:  # add --user (attempt 1)
        return command.script.replace(' install ', ' install --user ')

    return 'sudo {}'.format(command.script.replace(' --user', ''))  # since --user didn't fix things, let's try sudo (attempt 2)

class Generic(object):  [thefuck/shells/generic.py:16]
methods: _create_shell_configuration, _expand_aliases
         _get_history_file_name, _get_history_line
         _get_history_lines, _get_version
         _script_from_history, and_, app_alias
         decode_utf8, encode_utf8, from_shell, get_aliases
         get_builtin_commands, get_history
         how_to_configure, info, instant_mode_alias, or_
         put_to_history, quote, split_command, to_shell

    def split_command(self, command):
        """Split the command using shell-like syntax."""
        encoded = self.encode_utf8(command)

        try:
            splitted = [s.replace("??", "\\ ") for s in shlex.split(encoded.replace('\\ ', '??'))]
        except ValueError:
            splitted = encoded.split(' ')

        return self.decode_utf8(splitted)

    def and_(self, *commands):
        return u' && '.join(commands)

class Command(object):  [thefuck/thefuck/types.py:12]
methods: from_raw_script, script_parts, stderr, stdout, update
         __eq__, __init__, __repr__

class CorrectedCommand(object):  [thefuck/thefuck/types.py:201]
methods: _get_script, run, __eq__, __hash__, __init__, __repr__

def match(command):
    is_proper_command = ('brew' in command.script and
                         'Unknown command' in command.output)

    if is_proper_command:
        broken_cmd = re.findall(r'Error: Unknown command: ([a-z]+)',
                                command.output)[0]
        return bool(get_closest(broken_cmd, _brew_commands()))
    return False

file thefuck/rules/gem_unknown_command.py
imports: re, subprocess, thefuck
defines: match, _get_unknown_command, _get_all_commands, get_new_command

def get_new_command(command):
    unknown_command = _get_unknown_command(command)
    all_commands = _get_all_commands()
    return replace_command(command, unknown_command, all_commands)

def _get_unknown_command(command):
    return re.findall(r'Unknown command (.*)$', command.output)[0]

def match(command):
    return ('ERROR:  While executing gem ... (Gem::CommandLineError)'
            in command.output
            and 'Unknown command' in command.output)

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

def get_new_command(command):
    broken_cmd = re.findall(r'Error: Unknown command: ([a-z]+)',
                            command.output)[0]
    return replace_command(command, broken_cmd, _brew_commands())

def get_new_command(command):
    broken = command.script_parts[1]
    fix = re.findall(r'Did you mean `([^`]*)`', command.output)[0]

    return replace_argument(command.script, broken, fix)

def get_new_command(command):
    broken = command.script_parts[1]
    fix = re.findall(r'Did you mean [`"](?:yarn )?([^`"]*)[`"]', command.output)[0]

    return replace_argument(command.script, broken, fix)

def match(command):
    return ('install' in command.script
            and warning_regex.search(command.output)
            and message_regex.search(command.output))

def match(command):
    '''
    Matches a command's output with docker's output
    warning you that you need to remove a container before removing an image.
    '''
    return 'image is being used by running container' in command.output

def _get_raw_command(known_args):
    if known_args.force_command:
        return [known_args.force_command]
    elif not os.environ.get('TF_HISTORY'):
        return known_args.command
    else:
        history = os.environ['TF_HISTORY'].split('\n')[::-1]
        alias = get_alias()
        executables = get_all_executables()
        for command in history:
            diff = SequenceMatcher(a=alias, b=command).ratio()
            if diff < const.DIFF_WITH_ALIAS or command in executables:
                return [command]
    return []

def brew_unknown_cmd2():
    return '''Error: Unknown command: instaa'''

def brew_unknown_cmd():
    return '''Error: Unknown command: inst'''

def docker_help(mocker):
    help = b'''Usage: docker [OPTIONS] COMMAND [arg...]

A self-sufficient runtime for linux containers.

Options:

  --api-cors-header=                   Set CORS headers in the remote API
  -b, --bridge=                        Attach containers to a network bridge
  --bip=                               Specify network bridge IP
  -D, --debug=false                    Enable debug mode
  -d, --daemon=false                   Enable daemon mode
    # ... truncated

file thefuck/rules/docker_image_being_used_by_container.py
imports: thefuck
defines: match, get_new_command

file thefuck/rules/git_fix_stash.py
imports: thefuck
defines: match, get_new_command

def match(command):
    return regex.findall(command.output)

def match(command):
    return regex.findall(command.output)

def match(command):
    return regex.findall(command.output)

def match(command):
    return regex.findall(command.output)

def match(command):
    return regex.findall(command.output)

def match(command):
    return re.search(MISTAKE, command.output) and re.search(FIX, command.output)

file thefuck/rules/fix_file.py
imports: re, os, thefuck
defines: _make_pattern, _search, match, get_new_command

def get_new_command(command):
    m = _search(command.output)

    # Note: there does not seem to be a standard for columns, so they are just
    # ignored by default
    if settings.fixcolcmd and 'col' in m.groupdict():
        editor_call = settings.fixcolcmd.format(editor=os.environ['EDITOR'],
                                                file=m.group('file'),
                                                line=m.group('line'),
                                                col=m.group('col'))
    else:
        editor_call = settings.fixlinecmd.format(editor=os.environ['EDITOR'],
                                                 file=m.group('file'),
                                                 line=m.group('line'))

    return shell.and_(editor_call, command.script)

def get_new_command(command):
    missing_module = re.findall(MISSING_MODULE, command.output)[0]
    return shell.and_("pip install {}".format(missing_module), command.script)

file thefuck/rules/adb_unknown_command.py
imports: thefuck
defines: match, get_new_command

def get_new_command(command):
    for idx, arg in enumerate(command.script_parts[1:]):
        # allowed params to ADB are a/d/e/s/H/P/L where s, H, P and L take additional args
        # for example 'adb -s 111 logcat' or 'adb -e logcat'
        if not arg[0] == '-' and not command.script_parts[idx] in ('-s', '-H', '-P', '-L'):
            adb_cmd = get_closest(arg, _ADB_COMMANDS)
            return replace_argument(command.script, arg, adb_cmd)

def match(command):
    return 'unknown command' in command.output

file thefuck/rules/fix_alt_space.py
imports: re, thefuck
defines: match, get_new_command

def get_new_command(command):
    return regex.findall(command.output)[0]

file thefuck/entrypoints/main.py
imports: system, os, sys, argument_parser, utils, shells, alias, fix_command
defines: main

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

    def from_raw_script(cls, raw_script):
        """Creates instance of `Command` from a list of script parts.

        :type raw_script: [basestring]
        :rtype: Command
        :raises: EmptyCommand

        """
        script = format_raw_script(raw_script)
        if not script:
            raise EmptyCommand

        expanded = shell.from_shell(script)
        output = get_output(script, expanded)
        return cls(expanded, output)

def get_new_command(command):
    not_found_commands = _get_between(
        command.output, 'Warning: Command(s) not found:',
        'Available commands:')
    possible_commands = _get_between(
        command.output, 'Available commands:')

    script = command.script
    for not_found in not_found_commands:
        fix = get_closest(not_found, possible_commands)
        script = script.replace(' {}'.format(not_found),
                                ' {}'.format(fix))

    return script

file thefuck/rules/unknown_command.py
imports: re, thefuck
defines: match, get_new_command

def match(command):
    return (re.search(r"([^:]*): Unknown command.*", command.output) is not None
            and re.search(r"Did you mean ([^?]*)?", command.output) is not None)

def get_new_command(command):
    broken_cmd = re.findall(r"([^:]*): Unknown command.*", command.output)[0]
    matched = re.findall(r"Did you mean ([^?]*)?", command.output)
    return replace_command(command, broken_cmd, matched)

def get_new_command(command):
    if re.search(help_regex, command.output) is not None:
        match_obj = re.search(help_regex, command.output, re.I)
        return match_obj.group(1)

    return replace_argument(command.script, '-h', '--help')

def match(command):
    # Catches "Unknown operation 'service'." when executing systemctl with
    # misordered arguments
    cmd = command.script_parts
    return (cmd and 'Unknown operation \'' in command.output and
            len(cmd) - cmd.index('systemctl') == 3)

def output():
    return ('ERR: Bad regex! pcre_compile() failed at position 1: missing )\n'
            'If you meant to search for a literal string, run ag with -Q\n')

def replace_argument(script, from_, to):
    """Replaces command line argument."""
    replaced_in_the_end = re.sub(u' {}$'.format(re.escape(from_)), u' {}'.format(to),
                                 script, count=1)
    if replaced_in_the_end != script:
        return replaced_in_the_end
    else:
        return script.replace(
            u' {} '.format(from_), u' {} '.format(to), 1)

file thefuck/rules/port_already_in_use.py
imports: re, subprocess, thefuck
defines: _get_pid_by_port, _get_used_port, match, get_new_command

def match(command):
    port = _get_used_port(command)
    return port and _get_pid_by_port(port)

def get_new_command(command):
    port = _get_used_port(command)
    pid = _get_pid_by_port(port)
    return shell.and_(u'kill {}'.format(pid), command.script)

def _get_pid_by_port(port):
    proc = Popen(['lsof', '-i', ':{}'.format(port)], stdout=PIPE)
    lines = proc.stdout.read().decode().split('\n')
    if len(lines) > 1:
        return lines[1].split()[1]
    else:
        return None

    def instant_mode_alias(self, alias_name):
        warn("Instant mode not supported by your shell")
        return self.app_alias(alias_name)

def version(thefuck_version, python_version, shell_info):
    sys.stderr.write(
        u'The Fuck {} using Python {} and {}\n'.format(thefuck_version,
                                                       python_version,
                                                       shell_info))

def match(command):
    # We want it to be a URL by itself
    if len(command.script_parts) != 1:
        return False
    # Ensure we got the error we expected
    if which(command.script_parts[0]) or not (
        'No such file or directory' in command.output
        or 'not found' in command.output
        or 'is not recognised as' in command.output
    ):
        return False
    url = parse.urlparse(command.script, scheme='ssh')
    # HTTP URLs need a network address
    if not url.netloc and url.scheme != 'ssh':
        return False
    # SSH needs a username and a splitter between the path
    if url.scheme == 'ssh' and not (
        '@' in command.script
        and ':' in command.script
    ):
        return False
    return url.scheme in ['http', 'https', 'ssh']

def get_new_command(command):
    misspelled_command = regex.findall(command.output)[0]
    return replace_command(command, misspelled_command, _get_operations())

def _get_failed_lifecycle(command):
    return re.search(r'\[ERROR\] Unknown lifecycle phase "(.+)"',
                     command.output)

file thefuck/output_readers/read_log.py
imports: os, shlex, mmap, re, shutil, backports, six, pyte
defines: _group_by_calls, _get_script_group_lines, _get_output_lines, _skip_old_lines, get_output

def get_new_command(command):
    name = regex.findall(command.output)[0]
    return shell.and_('nix-env -iA {}'.format(name), command.script)


    def and_(self, *commands):
```
