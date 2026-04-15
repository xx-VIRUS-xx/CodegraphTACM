# thefuck-21 :: tacm

query: #369 Fix `git_fix_stash` fails when script is just `git`

## selected nodes

- rank=1 layer=FILE tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py
- rank=2 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=3 layer=FILE tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=4 layer=FILE tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash.py
- rank=5 layer=CLASS tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/entrypoints/test_fix_command.py::TestGetRawCommand file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/entrypoints/test_fix_command.py
- rank=6 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=7 layer=CLASS tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=8 layer=CLASS tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_types.py::TestRule file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_types.py
- rank=9 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=10 layer=CLASS tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=11 layer=CLASS tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/output_readers/test_rerun.py::TestRerun file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/output_readers/test_rerun.py
- rank=12 layer=CLASS tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py::Zsh file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/zsh.py
- rank=13 layer=CLASS tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=14 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_types.py::TestCommand file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_types.py
- rank=15 layer=CLASS tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py
- rank=16 layer=CLASS tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::Cache file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=17 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py
- rank=18 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash.py
- rank=19 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_uncommitted_changes.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_uncommitted_changes.py
- rank=20 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command_one_of_this file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=21 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py
- rank=22 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=23 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash_pop.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash_pop.py
- rank=24 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py
- rank=25 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py
- rank=26 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_argument file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=27 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py::fix_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=28 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.is_match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=29 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash.py
- rank=30 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py
- rank=31 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=32 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand._get_script file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=33 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.get_corrected_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=34 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py
- rank=35 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=36 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=37 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py
- rank=38 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py
- rank=39 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command_closest file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=40 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.is_enabled file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=41 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::get_closest file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=42 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=43 layer=FUNCTION tokens=263 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/git.py::git_support file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/git.py
- rank=44 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=45 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=46 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rebase_no_changes.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rebase_no_changes.py
- rank=47 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_branch_exists.py::new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_branch_exists.py
- rank=48 layer=FUNCTION tokens=181 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py::select_command_with_arrows file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py
- rank=49 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_exists.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_exists.py
- rank=50 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::which file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=51 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py
- rank=52 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py
- rank=53 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_types.py::TestCommand.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_types.py
- rank=54 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::is_app file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=55 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py
- rank=56 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_missing.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_missing.py
- rank=57 layer=FUNCTION tokens=10 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=58 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.or_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py

## context

```text
file thefuck/rules/git_fix_stash.py
imports: thefuck
defines: match, get_new_command

file thefuck/entrypoints/fix_command.py
imports: pprint, os, sys, difflib, conf, corrector, exceptions, ui
defines: _get_raw_command, fix_command

file thefuck/thefuck/utils.py
imports: atexit, os, pickle, re, shelve, sys, six, decorator
defines: Cache, memoize, wrapper, which, is_exe, default_settings, _default_settings, get_closest, get_close_matches, include_path_in_search, get_all_executables, _safe, replace_argument, eager, get_all_matched_commands, replace_command, is_app, for_app, _for_app, cache, cache_decorator, wrapper, get_installation_version, get_alias, get_valid_history_without_current, _not_corrected, format_raw_script

file thefuck/rules/git_stash.py
imports: thefuck
defines: match, get_new_command

class TestGetRawCommand(object):  [tests/entrypoints/test_fix_command.py:6]
methods: test_from_command_argument
         test_from_force_command_argument, test_from_history

class CorrectedCommand(object):  [thefuck/thefuck/types.py:201]
methods: _get_script, run, __eq__, __hash__, __init__, __repr__

class Rule(object):  [thefuck/thefuck/types.py:85]
methods: from_path, get_corrected_commands, is_enabled, is_match
         __eq__, __init__, __repr__

class TestRule(object):  [thefuck/tests/test_types.py:47]
methods: test_from_path, test_from_path_excluded_rule
         test_from_path_rule_exception
         test_get_corrected_commands_with_rule_returns_command
         test_get_corrected_commands_with_rule_returns_list
         test_is_enabled, test_is_match, test_isnt_match
         test_isnt_match_when_rule_failed

class Command(object):  [thefuck/thefuck/types.py:12]
methods: from_raw_script, script_parts, stderr, stdout, update
         __eq__, __init__, __repr__

class Generic(object):  [thefuck/shells/generic.py:16]
methods: _create_shell_configuration, _expand_aliases
         _get_history_file_name, _get_history_line
         _get_history_lines, _get_version
         _script_from_history, and_, app_alias
         decode_utf8, encode_utf8, from_shell, get_aliases
         get_builtin_commands, get_history
         how_to_configure, info, instant_mode_alias, or_
         put_to_history, quote, split_command, to_shell

class TestRerun(object):  [tests/output_readers/test_rerun.py:11]
methods: setup_method, teardown_method, test_get_output
         test_get_output_invalid_continuation_byte
         test_get_output_unicode_misspell
         test_kill_process
         test_kill_process_access_denied
         test_wait_output_is_not_slow
         test_wait_output_is_slow
         test_wait_output_timeout
         test_wait_output_timeout_children

class Zsh(Generic):  [thefuck/shells/zsh.py:12]
methods: _get_history_file_name, _get_history_line, _get_version
         _parse_alias, _script_from_history, app_alias
         get_aliases, how_to_configure, instant_mode_alias

class Fish(Generic):  [thefuck/shells/fish.py:40]
methods: _expand_aliases, _get_history_file_name, _get_history_line
         _get_overridden_aliases, _get_version
         _put_to_history, _script_from_history, and_
         app_alias, get_aliases, how_to_configure, or_
         put_to_history

class TestCommand(object):  [thefuck/tests/test_types.py:116]
methods: Popen, prepare, test_from_script, test_from_script_calls

class TestFish(object):  [tests/shells/test_fish.py:9]
methods: Popen, shell, test_and_, test_app_alias
         test_app_alias_alter_history, test_from_shell
         test_get_aliases, test_get_history
         test_get_overridden_aliases, test_get_version
         test_get_version_error, test_how_to_configure
         test_how_to_configure_when_config_not_found
         test_or_, test_put_to_history, test_to_shell

class Cache(object):  [thefuck/thefuck/utils.py:199]
methods: _get_cache_dir, _get_key, _get_mtime, _init_db, _setup_db
         get_value, __init__

class Powershell(Generic):  [thefuck/shells/powershell.py:6]
methods: _get_version, and_, app_alias, how_to_configure

def get_new_command(command):
    formatme = shell.and_('git stash', '{}')
    return formatme.format(command.script)

def get_new_command(command):
    return shell.and_('git stash', 'git pull', 'git stash pop')

def git_not_command_one_of_this():
    return """git: 'st' is not a git command. See 'git --help'.

The most similar commands are
status
reset
stage
stash
stats
"""

def get_new_command(command):
    stash_cmd = command.script_parts[2]
    fixed = utils.get_closest(stash_cmd, stash_commands, fallback_to_first=False)

    if fixed is not None:
        return replace_argument(command.script, stash_cmd, fixed)
    else:
        cmd = command.script_parts[:]
        cmd.insert(2, 'save')
        return ' '.join(cmd)

def get_new_command(command):
    mistake = re.search(MISTAKE, command.output).group(0)
    fix = re.search(FIX, command.output).group(0)
    return command.script.replace(mistake, fix)

def get_new_command(command):
    return shell.and_('git add --update', 'git stash pop', 'git reset .')

def get_new_command(command):
    broken = command.script_parts[1]
    fix = re.findall(r'Did you mean `([^`]*)`', command.output)[0]

    return replace_argument(command.script, broken, fix)

def get_new_command(command):
    broken = command.script_parts[1]
    fix = re.findall(r'Did you mean [`"](?:yarn )?([^`"]*)[`"]', command.output)[0]

    return replace_argument(command.script, broken, fix)

def replace_argument(script, from_, to):
    """Replaces command line argument."""
    replaced_in_the_end = re.sub(u' {}$'.format(re.escape(from_)), u' {}'.format(to),
                                 script, count=1)
    if replaced_in_the_end != script:
        return replaced_in_the_end
    else:
        return script.replace(
            u' {} '.format(from_), u' {} '.format(to), 1)

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

def match(command):
    # catches "Please commit or stash them" and "Please, commit your changes or
    # stash them before you can switch branches."
    return 'or stash them' in command.output

    def Popen(self, mocker):
        mock = mocker.patch('thefuck.shells.fish.Popen')
        mock.return_value.stdout.read.side_effect = [(
            b'cd\nfish_config\nfuck\nfunced\nfuncsave\ngrep\nhistory\nll\nls\n'
            b'man\nmath\npopd\npushd\nruby'),
            (b'alias fish_key_reader /usr/bin/fish_key_reader\nalias g git\n'
             b'alias alias_with_equal_sign=echo\ninvalid_alias'), b'func1\nfunc2', b'']
        return mock

def git_not_command():
    return """git: 'brnch' is not a git command. See 'git --help'.

The most similar command is
branch
"""

    def _get_script(self):
        """Returns fixed commands script.

        If `settings.repeat` is `True`, appends command with second attempt
        of running fuck in case fixed command fails again.

        """
        if settings.repeat:
            repeat_fuck = '{} --repeat {}--force-command {}'.format(
                get_alias(),
                '--debug ' if settings.debug else '',
                shell.quote(self.script))
            return shell.or_(self.script, repeat_fuck)
        else:
            return self.script

    def get_corrected_commands(self, command):
        """Returns generator with corrected commands.

        :type command: Command
        :rtype: Iterable[CorrectedCommand]

        """
        new_commands = self.get_new_command(command)
        if not isinstance(new_commands, list):
            new_commands = (new_commands,)
        for n, new_command in enumerate(new_commands):
            yield CorrectedCommand(script=new_command,
                                   side_effect=self.side_effect,
                                   priority=(n + 1) * self.priority)

    def and_(self, *commands):
        return u' -and '.join('({0})'.format(c) for c in commands)

    def and_(self, *commands):
        return u' && '.join(commands)


    def and_(self, *commands):

def match(command):
    if command.script_parts and len(command.script_parts) > 1:
        return (command.script_parts[1] == 'stash'
                and 'usage:' in command.output)
    else:
        return False

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

def git_not_command_closest():
    return '''git: 'tags' is not a git command. See 'git --help'.

The most similar commands are
\tstage
\ttag
'''

    def is_enabled(self):
        """Returns `True` when rule enabled.

        :rtype: bool

        """
        return (
            self.name in settings.rules
            or self.enabled_by_default
            and ALL_ENABLED in settings.rules
        )

def get_closest(word, possibilities, cutoff=0.6, fallback_to_first=True):
    """Returns closest match or just first from possibilities."""
    possibilities = list(possibilities)
    try:
        return difflib_get_close_matches(word, possibilities, 1, cutoff)[0]
    except IndexError:
        if fallback_to_first:
            return possibilities[0]

    def patch(vals):
        vals = iter(vals)
        monkeypatch.setattr('thefuck.ui.get_key', lambda: next(vals))

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

def match(command):
    return re.search(MISTAKE, command.output) and re.search(FIX, command.output)

def replace_command(command, broken, matched):
    """Helper for *_no_command rules."""
    new_cmds = get_close_matches(broken, matched, cutoff=0.1)
    return [replace_argument(command.script, broken, new_cmd.strip())
            for new_cmd in new_cmds]

def output():
    return '''Applying: Test commit
No changes - did you forget to use 'git add'?
If there is nothing left to stage, chances are that something else
already introduced the same changes; you might want to skip this patch.

When you have resolved this problem, run "git rebase --continue".
If you prefer to skip this patch, run "git rebase --skip" instead.
To check out the original branch and stop rebasing, run "git rebase --abort".

'''

def new_command(branch_name):
    return [cmd.format(branch_name) for cmd in [
        'git branch -d {0} && git branch {0}',
        'git branch -d {0} && git checkout -b {0}',
        'git branch -D {0} && git branch {0}',
        'git branch -D {0} && git checkout -b {0}', 'git checkout {0}']]

def select_command_with_arrows(proc, TIMEOUT):
    """Ensures that command can be selected with arrow keys."""
    _set_confirmation(proc, True)

    proc.sendline(u'git h')
    assert proc.expect([TIMEOUT, u"git: 'h' is not a git command."])

    proc.sendline(u'fuck')
    assert proc.expect([TIMEOUT, u'git show'])
    proc.send('\033[B')
    assert proc.expect([TIMEOUT, u'git push'])
    proc.send('\033[B')
    assert proc.expect([TIMEOUT, u'git help', u'git hook'])
    proc.send('\033[A')
    assert proc.expect([TIMEOUT, u'git push'])
    proc.send('\033[B')
    assert proc.expect([TIMEOUT, u'git help', u'git hook'])
    proc.send('\n')

    assert proc.expect([TIMEOUT, u'usage', u'fatal: not a git repository'])

def get_new_command(command):
    branch_name = re.findall(
        r"fatal: A branch named '(.+)' already exists.", command.output)[0]
    branch_name = branch_name.replace("'", r"\'")
    new_command_templates = [['git branch -d {0}', 'git branch {0}'],
                             ['git branch -d {0}', 'git checkout -b {0}'],
                             ['git branch -D {0}', 'git branch {0}'],
                             ['git branch -D {0}', 'git checkout -b {0}'],
                             ['git checkout {0}']]
    for new_command_template in new_command_templates:
        yield shell.and_(*new_command_template).format(branch_name)

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

def match(command):
    # catches "git branch list" in place of "git branch"
    return (command.script_parts
            and command.script_parts[1:] == 'branch list'.split())

def match(command):
    return (" is not a git command. See 'git --help'." in command.output
            and ('The most similar command' in command.output
                 or 'Did you mean' in command.output))

    def Popen(self, monkeypatch):
        Popen = Mock()
        Popen.return_value.stdout.read.return_value = b'output'
        monkeypatch.setattr('thefuck.output_readers.rerun.Popen', Popen)
        return Popen

def is_app(command, *app_names, **kwargs):
    """Returns `True` if command is call to one of passed app names."""

    at_least = kwargs.pop('at_least', 0)
    if kwargs:
        raise TypeError("got an unexpected keyword argument '{}'".format(kwargs.keys()))

    if len(command.script_parts) > at_least:
        return os.path.basename(command.script_parts[0]) in app_names

    return False

def get_new_command(command):
    return shell.and_('git branch --delete list', 'git branch')

def get_new_command(command):
    return 'git clone ' + command.script

def git_command():
    return "* master"


    def or_(self, *commands):
```
