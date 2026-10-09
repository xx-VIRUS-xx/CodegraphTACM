# thefuck-31 :: tacm-dyn

query: Fix the `git_diff_staged` rule

## selected nodes

- rank=1 layer=FILE tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py
- rank=2 layer=CLASS tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py::Rule file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py
- rank=3 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py
- rank=4 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py
- rank=5 layer=CLASS tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_types.py::TestRule file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_types.py
- rank=6 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.is_match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=7 layer=CLASS tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/entrypoints/test_fix_command.py::TestGetRawCommand file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/entrypoints/test_fix_command.py
- rank=8 layer=CLASS tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=9 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.from_path file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=10 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=11 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.get_corrected_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=12 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_argument file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=13 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py::Rule.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py
- rank=14 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rm_staged.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rm_staged.py
- rank=15 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rm_staged.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rm_staged.py
- rank=16 layer=FILE tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rm_staged.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rm_staged.py
- rank=17 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::rule_failed file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py
- rank=18 layer=FILE tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_no_index.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_no_index.py
- rank=19 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_no_index.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_no_index.py
- rank=20 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_no_index.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_no_index.py
- rank=21 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::get_loaded_rules file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py
- rank=22 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=23 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::get_rules file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py
- rank=24 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=25 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command_closest file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=26 layer=FILE tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py
- rank=27 layer=FILE tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=28 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=29 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py
- rank=30 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py
- rank=31 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=32 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py::_get_raw_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=33 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py::fix_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=34 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py
- rank=35 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py
- rank=36 layer=CLASS tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=37 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=38 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic._get_version file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=39 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=40 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py::Settings._rules_from_env file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py
- rank=41 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rebase_no_changes.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rebase_no_changes.py
- rank=42 layer=FUNCTION tokens=249 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cd_correction.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cd_correction.py
- rank=43 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py::docker_help file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_docker_not_command.py
- rank=44 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command_one_of_this file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=45 layer=FUNCTION tokens=308 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push.py
- rank=46 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py
- rank=47 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py
- rank=48 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py
- rank=49 layer=FILE tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py
- rank=50 layer=FUNCTION tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::color file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py
- rank=51 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py::Settings._priority_from_env file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py
- rank=52 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py::Fish.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/fish.py
- rank=53 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_exists.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_exists.py
- rank=54 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.info file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=55 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_install.py::brew_no_available_formula_three file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_install.py
- rank=56 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_uncommitted_changes.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_uncommitted_changes.py
- rank=57 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_file.py file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_file.py
- rank=58 layer=FUNCTION tokens=10 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py::TestCache.fn file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py

## context

```text
file thefuck/rules/git_diff_staged.py
imports: thefuck
defines: match, get_new_command

class Rule(types.Rule):  [thefuck/tests/utils.py:5]
methods: __init__

def get_new_command(command):
    return replace_argument(command.script, 'diff', 'diff --staged')

def match(command):
    return ('diff' in command.script and
            '--staged' not in command.script)

class TestRule(object):  [thefuck/tests/test_types.py:47]
methods: test_from_path, test_from_path_excluded_rule
         test_from_path_rule_exception
         test_get_corrected_commands_with_rule_returns_command
         test_get_corrected_commands_with_rule_returns_list
         test_is_enabled, test_is_match, test_isnt_match
         test_isnt_match_when_rule_failed

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

class TestGetRawCommand(object):  [tests/entrypoints/test_fix_command.py:6]
methods: test_from_command_argument
         test_from_force_command_argument, test_from_history

class Rule(object):  [thefuck/thefuck/types.py:85]
methods: from_path, get_corrected_commands, is_enabled, is_match
         __eq__, __init__, __repr__

    def from_path(cls, path):
        """Creates rule instance from path.

        :type path: pathlib.Path
        :rtype: Rule

        """
        name = path.name[:-3]
        if name in settings.exclude_rules:
            logs.debug(u'Ignoring excluded rule: {}'.format(name))
            return
        with logs.debug_time(u'Importing rule: {};'.format(name)):
            try:
                rule_module = load_source(name, str(path))
            except Exception:
                logs.exception(u"Rule {} failed to load".format(name), sys.exc_info())
                return
        priority = getattr(rule_module, 'priority', DEFAULT_PRIORITY)
        return cls(name, rule_module.match,
                   rule_module.get_new_command,
                   getattr(rule_module, 'enabled_by_default', True),
                   getattr(rule_module, 'side_effect', None),
                   settings.priority.get(name, priority),
                   getattr(rule_module, 'requires_output', True))

    def patch(vals):
        vals = iter(vals)
        monkeypatch.setattr('thefuck.ui.get_key', lambda: next(vals))

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

def replace_argument(script, from_, to):
    """Replaces command line argument."""
    replaced_in_the_end = re.sub(u' {}$'.format(re.escape(from_)), u' {}'.format(to),
                                 script, count=1)
    if replaced_in_the_end != script:
        return replaced_in_the_end
    else:
        return script.replace(
            u' {} '.format(from_), u' {} '.format(to), 1)

    def __init__(self, name='', match=lambda *_: True,
                 get_new_command=lambda *_: '',
                 enabled_by_default=True,
                 side_effect=None,
                 priority=DEFAULT_PRIORITY,
                 requires_output=True):
        super(Rule, self).__init__(name, match, get_new_command,
                                   enabled_by_default, side_effect,
                                   priority, requires_output)

def output(target):
    return ('error: the following file has changes staged in the index:\n    {}\n(use '
            '--cached to keep the file, or -f to force removal)').format(target)

def match(command):
    return (' rm ' in command.script and
            'error: the following file has changes staged in the index' in command.output and
            'use --cached to keep the file, or -f to force removal' in command.output)

file thefuck/rules/git_rm_staged.py
imports: thefuck
defines: match, get_new_command

def rule_failed(rule, exc_info):
    exception(u'Rule {}'.format(rule.name), exc_info)

file thefuck/rules/git_diff_no_index.py
imports: thefuck
defines: match, get_new_command

def get_new_command(command):
    return replace_argument(command.script, 'diff', 'diff --no-index')

def match(command):
    files = [arg for arg in command.script_parts[2:]
             if not arg.startswith('-')]
    return ('diff' in command.script
            and '--no-index' not in command.script
            and len(files) == 2)

def get_loaded_rules(rules_paths):
    """Yields all available rules.

    :type rules_paths: [Path]
    :rtype: Iterable[Rule]

    """
    for path in rules_paths:
        if path.name != '__init__.py':
            rule = Rule.from_path(path)
            if rule and rule.is_enabled:
                yield rule

def get_new_command(command):
    mistake = re.search(MISTAKE, command.output).group(0)
    fix = re.search(FIX, command.output).group(0)
    return command.script.replace(mistake, fix)

def get_rules():
    """Returns all enabled rules.

    :rtype: [Rule]

    """
    paths = [rule_path for path in get_rules_import_paths()
             for rule_path in sorted(path.glob('*.py'))]
    return sorted(get_loaded_rules(paths),
                  key=lambda rule: rule.priority)

def git_not_command():
    return """git: 'brnch' is not a git command. See 'git --help'.

The most similar command is
branch
"""

def git_not_command_closest():
    return '''git: 'tags' is not a git command. See 'git --help'.

The most similar commands are
\tstage
\ttag
'''

file thefuck/rules/git_fix_stash.py
imports: thefuck
defines: match, get_new_command

file thefuck/thefuck/types.py
imports: os, sys, shells, conf, const, exceptions, utils, output_readers
defines: Command, Rule, CorrectedCommand

class CorrectedCommand(object):  [thefuck/thefuck/types.py:201]
methods: _get_script, run, __eq__, __hash__, __init__, __repr__

def get_new_command(command):
    broken = command.script_parts[1]
    fix = re.findall(r'Did you mean `([^`]*)`', command.output)[0]

    return replace_argument(command.script, broken, fix)

def get_new_command(command):
    broken = command.script_parts[1]
    fix = re.findall(r'Did you mean [`"](?:yarn )?([^`"]*)[`"]', command.output)[0]

    return replace_argument(command.script, broken, fix)

file thefuck/entrypoints/fix_command.py
imports: pprint, os, sys, difflib, conf, corrector, exceptions, ui
defines: _get_raw_command, fix_command

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

def match(command):
    return (" is not a git command. See 'git --help'." in command.output
            and ('The most similar command' in command.output
                 or 'Did you mean' in command.output))

    def Popen(self, mocker):
        mock = mocker.patch('thefuck.shells.fish.Popen')
        mock.return_value.stdout.read.side_effect = [(
            b'cd\nfish_config\nfuck\nfunced\nfuncsave\ngrep\nhistory\nll\nls\n'
            b'man\nmath\npopd\npushd\nruby'),
            (b'alias fish_key_reader /usr/bin/fish_key_reader\nalias g git\n'
             b'alias alias_with_equal_sign=echo\ninvalid_alias'), b'func1\nfunc2', b'']
        return mock

class Generic(object):  [thefuck/shells/generic.py:16]
methods: _create_shell_configuration, _expand_aliases
         _get_history_file_name, _get_history_line
         _get_history_lines, _get_version
         _script_from_history, and_, app_alias
         decode_utf8, encode_utf8, from_shell, get_aliases
         get_builtin_commands, get_history
         how_to_configure, info, instant_mode_alias, or_
         put_to_history, quote, split_command, to_shell

    def and_(self, *commands):
        return u' && '.join(commands)

    def _get_version(self):
        """Returns the version of the current shell"""
        return ''

def match(command):
    return re.search(MISTAKE, command.output) and re.search(FIX, command.output)

    def _rules_from_env(self, val):
        """Transforms rules list from env-string to python."""
        val = val.split(':')
        if 'DEFAULT_RULES' in val:
            val = const.DEFAULT_RULES + [rule for rule in val if rule != 'DEFAULT_RULES']
        return val

def output():
    return '''Applying: Test commit
No changes - did you forget to use 'git add'?
If there is nothing left to stage, chances are that something else
already introduced the same changes; you might want to skip this patch.

When you have resolved this problem, run "git rebase --continue".
If you prefer to skip this patch, run "git rebase --skip" instead.
To check out the original branch and stop rebasing, run "git rebase --abort".

'''

def get_new_command(command):
    """
    Attempt to rebuild the path string by spellchecking the directories.
    If it fails (i.e. no directories are a close enough match), then it
    defaults to the rules of cd_mkdir.
    Change sensitivity by changing MAX_ALLOWED_DIFF. Default value is 0.6
    """
    dest = command.script_parts[1].split(os.sep)
    if dest[-1] == '':
        dest = dest[:-1]

    if dest[0] == '':
        cwd = os.sep
        dest = dest[1:]
    elif six.PY2:
        cwd = os.getcwdu()
    else:
        cwd = os.getcwd()
    for directory in dest:
        if directory == ".":
            continue
        elif directory == "..":
            cwd = os.path.split(cwd)[0]
            continue
        best_matches = get_close_matches(directory, _get_sub_dirs(cwd), cutoff=MAX_ALLOWED_DIFF)
        if best_matches:
            cwd = os.path.join(cwd, best_matches[0])
        else:
            return cd_mkdir.get_new_command(command)
    return u'cd "{0}"'.format(cwd)

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

def output(branch_name):
    if not branch_name:
        return ''
    return '''fatal: The current branch {} has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin {}

'''.format(branch_name, branch_name)

def get_new_command(command):
    broken_cmd = re.findall(r"git: '([^']*)' is not a git command",
                            command.output)[0]
    matched = get_all_matched_commands(command.output, ['The most similar command', 'Did you mean'])
    return replace_command(command, broken_cmd, matched)

    def and_(self, *commands):
        return u' -and '.join('({0})'.format(c) for c in commands)

file thefuck/thefuck/logs.py
imports: contextlib, datetime, sys, traceback, colorama, conf
defines: color, warn, exception, rule_failed, failed, show_corrected_command, confirm_text, debug, debug_time, how_to_configure_alias, already_configured, configured_successfully, version

def color(color_):
    """Utility for ability to disabling colored output."""
    if settings.no_colors:
        return ''
    else:
        return color_

    def _priority_from_env(self, val):
        """Gets priority pairs from env."""
        for part in val.split(':'):
            try:
                rule, priority = part.split('=')
                yield rule, int(priority)
            except ValueError:
                continue


    def and_(self, *commands):

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

    def info(self):
        """Returns the name and version of the current shell"""
        try:
            version = self._get_version()
        except Exception as e:
            warn(u'Could not determine shell version: {}'.format(e))
            version = ''
        return u'{} {}'.format(self.friendly_name, version).rstrip()

def brew_no_available_formula_three():
    return '''Warning: No available formula with the name "gitt". Did you mean git, gitg or gist?'''

def get_new_command(command):
    return shell.and_('git stash', 'git pull', 'git stash pop')

file thefuck/rules/fix_file.py
imports: re, os, thefuck
defines: _make_pattern, _search, match, get_new_command

        def fn():
            return 'test'
```
