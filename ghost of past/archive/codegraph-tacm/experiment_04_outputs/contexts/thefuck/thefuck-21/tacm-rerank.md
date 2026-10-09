# thefuck-21 :: tacm-rerank

query: #369 Fix `git_fix_stash` fails when script is just `git`

## selected nodes

- rank=1 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py
- rank=2 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash_pop.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash_pop.py
- rank=3 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash.py
- rank=4 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_uncommitted_changes.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_uncommitted_changes.py
- rank=5 layer=FUNCTION tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/git.py::git_support file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/specific/git.py
- rank=6 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=7 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=8 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_exists.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_exists.py
- rank=9 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py
- rank=10 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py
- rank=11 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py
- rank=12 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py
- rank=13 layer=FUNCTION tokens=169 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py
- rank=14 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command_closest file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=15 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command_one_of_this file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=16 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py
- rank=17 layer=FUNCTION tokens=157 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rebase_no_changes.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_rebase_no_changes.py
- rank=18 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_branch_exists.py::new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_branch_exists.py
- rank=19 layer=FUNCTION tokens=223 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py::select_command_with_arrows file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py
- rank=20 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=21 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py
- rank=22 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rebase_merge_dir.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rebase_merge_dir.py
- rank=23 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py
- rank=24 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py::refuse_with_confirmation file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py
- rank=25 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py::replace_argument file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/utils.py
- rank=26 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_missing.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_missing.py
- rank=27 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_pull.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_pull.py
- rank=28 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py
- rank=29 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py::fix_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=30 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_bisect_usage.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_bisect_usage.py
- rank=31 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_git_clone.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_git_clone.py
- rank=32 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push_without_commits.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push_without_commits.py
- rank=33 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_clone.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_clone.py
- rank=34 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_bisect_usage.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_bisect_usage.py
- rank=35 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.is_match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_fix_stash.py]
def get_new_command(command):
    stash_cmd = command.script_parts[2]
    fixed = utils.get_closest(stash_cmd, stash_commands, fallback_to_first=False)

    if fixed is not None:
        return replace_argument(command.script, stash_cmd, fixed)
    else:
        cmd = command.script_parts[:]
        cmd.insert(2, 'save')
        return ' '.join(cmd)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash_pop.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash_pop.py]
def get_new_command(command):
    return shell.and_('git add --update', 'git stash pop', 'git reset .')

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_stash.py]
def get_new_command(command):
    formatme = shell.and_('git stash', '{}')
    return formatme.format(command.script)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_uncommitted_changes.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_uncommitted_changes.py]
def get_new_command(command):
    return shell.and_('git stash', 'git pull', 'git stash pop')

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py]
def get_new_command(command):
    mistake = re.search(MISTAKE, command.output).group(0)
    fix = re.search(FIX, command.output).group(0)
    return command.script.replace(mistake, fix)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py]
def match(command):
    return re.search(MISTAKE, command.output) and re.search(FIX, command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_exists.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_exists.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py]
def match(command):
    # catches "git branch list" in place of "git branch"
    return (command.script_parts
            and command.script_parts[1:] == 'branch list'.split())

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py]
def match(command):
    return (" is not a git command. See 'git --help'." in command.output
            and ('The most similar command' in command.output
                 or 'Did you mean' in command.output))

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py::git_not_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_not_command.py]
def git_not_command():
    return """git: 'brnch' is not a git command. See 'git --help'.

The most similar command is
branch
"""

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_branch_exists.py::new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_branch_exists.py]
def new_command(branch_name):
    return [cmd.format(branch_name) for cmd in [
        'git branch -d {0} && git branch {0}',
        'git branch -d {0} && git checkout -b {0}',
        'git branch -D {0} && git branch {0}',
        'git branch -D {0} && git checkout -b {0}', 'git checkout {0}']]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py::select_command_with_arrows [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::patch [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py]
    def patch(vals):
        vals = iter(vals)
        monkeypatch.setattr('thefuck.ui.get_key', lambda: next(vals))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py]
def get_new_command(command):
    if '--user' not in command.script:  # add --user (attempt 1)
        return command.script.replace(' install ', ' install --user ')

    return 'sudo {}'.format(command.script.replace(' --user', ''))  # since --user didn't fix things, let's try sudo (attempt 2)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rebase_merge_dir.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_rebase_merge_dir.py]
def get_new_command(command):
    command_list = ['git rebase --continue', 'git rebase --abort', 'git rebase --skip']
    rm_cmd = command.output.split('\n')[-4]
    command_list.append(rm_cmd.strip())
    return get_close_matches(command.script, command_list, 4, 0)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_branch_list.py]
def get_new_command(command):
    return shell.and_('git branch --delete list', 'git branch')

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py::refuse_with_confirmation [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/functional/plots.py]
def refuse_with_confirmation(proc, TIMEOUT):
    """Ensures that fix can be refused when confirmation enabled."""
    _set_confirmation(proc, True)

    proc.sendline(u'ehco test')

    proc.sendline(u'fuck')
    assert proc.expect([TIMEOUT, u'echo test'])
    assert proc.expect([TIMEOUT, u'enter'])
    assert proc.expect_exact([TIMEOUT, u'ctrl+c'])
    proc.send('\003')

    assert proc.expect([TIMEOUT, u'Aborted'])

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_missing.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_missing.py]
def get_new_command(command):
    return 'git clone ' + command.script

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_pull.py::output [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_git_pull.py]
def output():
    return '''There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=<remote>/<branch> master

'''

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_not_command.py]
def get_new_command(command):
    broken_cmd = re.findall(r"git: '([^']*)' is not a git command",
                            command.output)[0]
    matched = get_all_matched_commands(command.output, ['The most similar command', 'Did you mean'])
    return replace_command(command, broken_cmd, matched)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py::fix_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_bisect_usage.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_bisect_usage.py]
def get_new_command(command):
    broken = re.findall(r'git bisect ([^ $]*).*', command.script)[0]
    usage = re.findall(r'usage: git bisect \[([^\]]+)\]', command.output)[0]
    return replace_command(command, broken, usage.split('|'))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_git_clone.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_clone_git_clone.py]
def get_new_command(command):
    return command.script.replace(' git clone ', ' ', 1)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push_without_commits.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_push_without_commits.py]
def get_new_command(command):
    return shell.and_('git commit -m "Initial commit"', command.script)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_clone.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_pull_clone.py]
def match(command):
    return ('fatal: Not a git repository' in command.output
            and "Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set)." in command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_bisect_usage.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_bisect_usage.py]
def match(command):
    return ('bisect' in command.script_parts and
            'usage: git bisect' in command.output)

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
```
