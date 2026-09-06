# thefuck-31 :: tacm-rerank

query: Fix the `git_diff_staged` rule

## selected nodes

- rank=1 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py
- rank=2 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py
- rank=3 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.is_match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=4 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_no_index.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_no_index.py
- rank=5 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py
- rank=6 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=7 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_argument file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=8 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rm_staged.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rm_staged.py
- rank=9 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rm_staged.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rm_staged.py
- rank=10 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.from_path file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=11 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::rule_failed file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py
- rank=12 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::get_loaded_rules file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py
- rank=13 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::get_rules file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py
- rank=14 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=15 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=16 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command_closest file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=17 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command_one_of_this file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=18 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py
- rank=19 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py
- rank=20 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py::_get_raw_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=21 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py::Settings._rules_from_env file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py
- rank=22 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.Popen file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py
- rank=23 layer=FUNCTION tokens=144 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::get_corrected_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py
- rank=24 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=25 layer=FUNCTION tokens=157 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rebase_no_changes.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rebase_no_changes.py
- rank=26 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py::Settings._priority_from_env file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py
- rank=27 layer=FUNCTION tokens=290 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cd_correction.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cd_correction.py
- rank=28 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py
- rank=29 layer=FUNCTION tokens=348 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push.py
- rank=30 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py
- rank=31 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py
- rank=32 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.and_ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py
- rank=33 layer=FUNCTION tokens=181 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.get_corrected_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py]
def match(command):
    return ('diff' in command.script and
            '--staged' not in command.script)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py]
def get_new_command(command):
    return replace_argument(command.script, 'diff', 'diff --staged')

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_no_index.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_no_index.py]
def get_new_command(command):
    return replace_argument(command.script, 'diff', 'diff --no-index')

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py]
def match(command):
    return (" is not a git command. See 'git --help'." in command.output
            and ('The most similar command' in command.output
                 or 'Did you mean' in command.output))

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rm_staged.py::output [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rm_staged.py]
def output(target):
    return ('error: the following file has changes staged in the index:\n    {}\n(use '
            '--cached to keep the file, or -f to force removal)').format(target)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rm_staged.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rm_staged.py]
def match(command):
    return (' rm ' in command.script and
            'error: the following file has changes staged in the index' in command.output and
            'use --cached to keep the file, or -f to force removal' in command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.from_path [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py::rule_failed [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/logs.py]
def rule_failed(rule, exc_info):
    exception(u'Rule {}'.format(rule.name), exc_info)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::get_loaded_rules [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::get_rules [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py]
def get_rules():
    """Returns all enabled rules.

    :rtype: [Rule]

    """
    paths = [rule_path for path in get_rules_import_paths()
             for rule_path in sorted(path.glob('*.py'))]
    return sorted(get_loaded_rules(paths),
                  key=lambda rule: rule.priority)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py]
def get_new_command(command):
    mistake = re.search(MISTAKE, command.output).group(0)
    fix = re.search(FIX, command.output).group(0)
    return command.script.replace(mistake, fix)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py]
def git_not_command():
    return """git: 'brnch' is not a git command. See 'git --help'.

The most similar command is
branch
"""

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command_closest [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py]
def git_not_command_closest():
    return '''git: 'tags' is not a git command. See 'git --help'.

The most similar commands are
\tstage
\ttag
'''

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command_one_of_this [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py]
def git_not_command_one_of_this():
    return """git: 'st' is not a git command. See 'git --help'.

The most similar commands are
status
reset
stage
stash
stats
"""

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py]
def get_new_command(command):
    broken = command.script_parts[1]
    fix = re.findall(r'Did you mean `([^`]*)`', command.output)[0]

    return replace_argument(command.script, broken, fix)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py]
def get_new_command(command):
    broken = command.script_parts[1]
    fix = re.findall(r'Did you mean [`"](?:yarn )?([^`"]*)[`"]', command.output)[0]

    return replace_argument(command.script, broken, fix)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py::_get_raw_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py::Settings._rules_from_env [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py]
    def _rules_from_env(self, val):
        """Transforms rules list from env-string to python."""
        val = val.split(':')
        if 'DEFAULT_RULES' in val:
            val = const.DEFAULT_RULES + [rule for rule in val if rule != 'DEFAULT_RULES']
        return val

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py::TestFish.Popen [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/shells/test_fish.py]
    def Popen(self, mocker):
        mock = mocker.patch('thefuck.shells.fish.Popen')
        mock.return_value.stdout.read.side_effect = [(
            b'cd\nfish_config\nfuck\nfunced\nfuncsave\ngrep\nhistory\nll\nls\n'
            b'man\nmath\npopd\npushd\nruby'),
            (b'alias fish_key_reader /usr/bin/fish_key_reader\nalias g git\n'
             b'alias alias_with_equal_sign=echo\ninvalid_alias'), b'func1\nfunc2', b'']
        return mock

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::get_corrected_commands [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py]
def get_corrected_commands(command):
    """Returns generator with sorted and unique corrected commands.

    :type command: thefuck.types.Command
    :rtype: Iterable[thefuck.types.CorrectedCommand]

    """
    corrected_commands = (
        corrected for rule in get_rules()
        if rule.is_match(command)
        for corrected in rule.get_corrected_commands(command))
    return organize_commands(corrected_commands)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py]
def match(command):
    return re.search(MISTAKE, command.output) and re.search(FIX, command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rebase_no_changes.py::output [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rebase_no_changes.py]
def output():
    return '''Applying: Test commit
No changes - did you forget to use 'git add'?
If there is nothing left to stage, chances are that something else
already introduced the same changes; you might want to skip this patch.

When you have resolved this problem, run "git rebase --continue".
If you prefer to skip this patch, run "git rebase --skip" instead.
To check out the original branch and stop rebasing, run "git rebase --abort".

'''

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py::Settings._priority_from_env [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py]
    def _priority_from_env(self, val):
        """Gets priority pairs from env."""
        for part in val.split(':'):
            try:
                rule, priority = part.split('=')
                yield rule, int(priority)
            except ValueError:
                continue

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cd_correction.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cd_correction.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py::output [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_push.py]
def output(branch_name):
    if not branch_name:
        return ''
    return '''fatal: The current branch {} has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin {}

'''.format(branch_name, branch_name)

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py::Powershell.and_ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/powershell.py]
    def and_(self, *commands):
        return u' -and '.join('({0})'.format(c) for c in commands)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py]
def get_new_command(command):
    broken_cmd = re.findall(r"git: '([^']*)' is not a git command",
                            command.output)[0]
    matched = get_all_matched_commands(command.output, ['The most similar command', 'Did you mean'])
    return replace_command(command, broken_cmd, matched)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py::Generic.and_ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/shells/generic.py]
    def and_(self, *commands):
        return u' && '.join(commands)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.get_corrected_commands [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
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
```
