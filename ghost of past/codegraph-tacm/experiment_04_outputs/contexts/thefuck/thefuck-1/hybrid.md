# thefuck-1 :: hybrid

query: #1047: Fix pip_unknown_command by using a less restrictive regex

## selected nodes

- rank=1 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py::pip_unknown_cmd_without_recommend file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py
- rank=2 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py::pip_unknown_cmd file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py
- rank=3 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py
- rank=4 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py
- rank=5 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py::brew_unknown_cmd file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py
- rank=6 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py
- rank=7 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py::brew_unknown_cmd2 file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py
- rank=8 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_module_error.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_module_error.py
- rank=9 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/go_unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/go_unknown_command.py
- rank=10 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py::_get_unknown_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py
- rank=11 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py
- rank=12 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/systemctl.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/systemctl.py
- rank=13 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_reinstall.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_reinstall.py
- rank=14 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/long_form_help.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/long_form_help.py
- rank=15 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py
- rank=16 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gradle_no_task.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gradle_no_task.py
- rank=17 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/mercurial.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/mercurial.py
- rank=18 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/grunt_task_not_found.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/grunt_task_not_found.py
- rank=19 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/nixos_cmd_not_found.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/nixos_cmd_not_found.py
- rank=20 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_not_found.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_not_found.py
- rank=21 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/long_form_help.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/long_form_help.py
- rank=22 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py
- rank=23 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_not_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_not_command.py
- rank=24 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py
- rank=25 layer=FUNCTION tokens=169 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py
- rank=26 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py
- rank=27 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=28 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py
- rank=29 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/rails_migrations_pending.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/rails_migrations_pending.py
- rank=30 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py
- rank=31 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py
- rank=32 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py
- rank=33 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=34 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py
- rank=35 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_image_being_used_by_container.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_image_being_used_by_container.py
- rank=36 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py
- rank=37 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py
- rank=38 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py
- rank=39 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py::_parse_operations file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py
- rank=40 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_command.py
- rank=41 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sed_unterminated_s.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sed_unterminated_s.py
- rank=42 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/omnienv_no_such_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/omnienv_no_such_command.py
- rank=43 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_module_error.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_module_error.py
- rank=44 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_ag_literal.py::output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_ag_literal.py
- rank=45 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/conda_mistype.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/conda_mistype.py
- rank=46 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py
- rank=47 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_merge.py::get_new_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_merge.py
- rank=48 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/touch.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/touch.py
- rank=49 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_go_unknown_command.py::build_misspelled_output file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_go_unknown_command.py
- rank=50 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/man.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/man.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py::pip_unknown_cmd_without_recommend [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py]
def pip_unknown_cmd_without_recommend():
    return '''ERROR: unknown command "i"'''

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py::pip_unknown_cmd [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_pip_unknown_command.py]
def pip_unknown_cmd(broken, suggested):
    return 'ERROR: unknown command "{}" - maybe you meant "{}"'.format(broken, suggested)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py]
def match(command):
    return ('pip' in command.script and
            'unknown command' in command.output and
            'maybe you meant' in command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_install.py]
def match(command):
    return ('pip install' in command.script and 'Permission denied' in command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py::brew_unknown_cmd [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py]
def brew_unknown_cmd():
    return '''Error: Unknown command: inst'''

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py]
def match(command):
    is_proper_command = ('brew' in command.script and
                         'Unknown command' in command.output)

    if is_proper_command:
        broken_cmd = re.findall(r'Error: Unknown command: ([a-z]+)',
                                command.output)[0]
        return bool(get_closest(broken_cmd, _brew_commands()))
    return False

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py::brew_unknown_cmd2 [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_brew_unknown_command.py]
def brew_unknown_cmd2():
    return '''Error: Unknown command: instaa'''

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_module_error.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_module_error.py]
def get_new_command(command):
    missing_module = re.findall(MISSING_MODULE, command.output)[0]
    return shell.and_("pip install {}".format(missing_module), command.script)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/go_unknown_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/go_unknown_command.py]
def match(command):
    return 'unknown command' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py::_get_unknown_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py]
def _get_unknown_command(command):
    return re.findall(r'Unknown command (.*)$', command.output)[0]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_unknown_command.py]
def get_new_command(command):
    broken_cmd = re.findall(r'Error: Unknown command: ([a-z]+)',
                            command.output)[0]
    return replace_command(command, broken_cmd, _brew_commands())

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/systemctl.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/systemctl.py]
def match(command):
    # Catches "Unknown operation 'service'." when executing systemctl with
    # misordered arguments
    cmd = command.script_parts
    return (cmd and 'Unknown operation \'' in command.output and
            len(cmd) - cmd.index('systemctl') == 3)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_reinstall.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/brew_reinstall.py]
def match(command):
    return ('install' in command.script
            and warning_regex.search(command.output)
            and message_regex.search(command.output))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/long_form_help.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/long_form_help.py]
def get_new_command(command):
    if re.search(help_regex, command.output) is not None:
        match_obj = re.search(help_regex, command.output, re.I)
        return match_obj.group(1)

    return replace_argument(command.script, '-h', '--help')

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py]
def match(command):
    return ('ERROR:  While executing gem ... (Gem::CommandLineError)'
            in command.output
            and 'Unknown command' in command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gradle_no_task.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gradle_no_task.py]
def match(command):
    return regex.findall(command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/mercurial.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/mercurial.py]
def match(command):
    return ('hg: unknown command' in command.output
            and '(did you mean one of ' in command.output
            or "hg: command '" in command.output
            and "' is ambiguous:" in command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/grunt_task_not_found.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/grunt_task_not_found.py]
def match(command):
    return regex.findall(command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/nixos_cmd_not_found.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/nixos_cmd_not_found.py]
def match(command):
    return regex.findall(command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_not_found.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_not_found.py]
def match(command):
    return regex.findall(command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/long_form_help.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/long_form_help.py]
def match(command):
    if re.search(help_regex, command.output, re.I) is not None:
        return True

    if '--help' in command.output:
        return True

    return False

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py]
def match(command):
    return regex.findall(command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_not_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_not_command.py]
def match(command):
    return 'is not a docker command' in command.output or 'Usage:	docker' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/gem_unknown_command.py]
def get_new_command(command):
    unknown_command = _get_unknown_command(command)
    all_commands = _get_all_commands()
    return replace_command(command, unknown_command, all_commands)

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py]
def get_new_command(command):
    broken = command.script_parts[1]
    fix = re.findall(r'Did you mean `([^`]*)`', command.output)[0]

    return replace_argument(command.script, broken, fix)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py]
def get_new_command(command):
    mistake = re.search(MISTAKE, command.output).group(0)
    fix = re.search(FIX, command.output).group(0)
    return command.script.replace(mistake, fix)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_command_replaced.py]
def get_new_command(command):
    return regex.findall(command.output)[0]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/rails_migrations_pending.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/rails_migrations_pending.py]
def get_new_command(command):
    migration_script = re.search(SUGGESTION_REGEX, command.output).group(1)
    return shell.and_(migration_script, command.script)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py]
def get_new_command(command):
    broken = command.script_parts[1]
    fix = re.findall(r'Did you mean [`"](?:yarn )?([^`"]*)[`"]', command.output)[0]

    return replace_argument(command.script, broken, fix)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/pip_unknown_command.py]
def get_new_command(command):
    broken_cmd = re.findall(r'ERROR: unknown command "([^"]+)"',
                            command.output)[0]
    new_cmd = re.findall(r'maybe you meant "([^"]+)"', command.output)[0]

    return replace_argument(command.script, broken_cmd, new_cmd)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py]
def match(command):
    return (re.search(r"([^:]*): Unknown command.*", command.output) is not None
            and re.search(r"Did you mean ([^?]*)?", command.output) is not None)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py]
def match(command):
    return re.search(MISTAKE, command.output) and re.search(FIX, command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py]
def get_new_command(command):
    misspelled_command = regex.findall(command.output)[0]
    return replace_command(command, misspelled_command, _get_operations())

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_image_being_used_by_container.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/docker_image_being_used_by_container.py]
def match(command):
    '''
    Matches a command's output with docker's output
    warning you that you need to remove a container before removing an image.
    '''
    return 'image is being used by running container' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py]
def match(command):
    return 'Warning: Command(s) not found:' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py]
def match(command):
    return 'No such command: ' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py]
def get_new_command(command):
    broken_cmd = re.findall(r"([^:]*): Unknown command.*", command.output)[0]
    matched = re.findall(r"Did you mean ([^?]*)?", command.output)
    return replace_command(command, broken_cmd, matched)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py::_parse_operations [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py]
def _parse_operations(help_text_lines):
    operation_regex = re.compile(r'^([a-z-]+) +', re.MULTILINE)
    return operation_regex.findall(help_text_lines)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_command.py]
def match(command):
    return (command.script_parts
            and command.script_parts[0].endswith('.py')
            and ('Permission denied' in command.output or
                 'command not found' in command.output))

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sed_unterminated_s.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sed_unterminated_s.py]
def match(command):
    return "unterminated `s' command" in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/omnienv_no_such_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/omnienv_no_such_command.py]
def match(command):
    return 'env: no such command ' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_module_error.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/python_module_error.py]
def match(command):
    return "ModuleNotFoundError: No module named '" in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_ag_literal.py::output [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_ag_literal.py]
def output():
    return ('ERR: Bad regex! pcre_compile() failed at position 1: missing )\n'
            'If you meant to search for a literal string, run ag with -Q\n')

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/conda_mistype.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/conda_mistype.py]
def match(command):
    """
    Match a mistyped command
    """
    return "Did you mean 'conda" in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py]
def match(command):
    return 'no such command' in command.output.lower()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_merge.py::get_new_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_merge.py]
def get_new_command(command):
    unknown_branch = re.findall(r'merge: (.+) - not something we can merge', command.output)[0]
    remote_branch = re.findall(r'Did you mean this\?\n\t([^\n]+)', command.output)[0]

    return replace_argument(command.script, unknown_branch, remote_branch)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/touch.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/touch.py]
def match(command):
    return 'No such file or directory' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_go_unknown_command.py::build_misspelled_output [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_go_unknown_command.py]
def build_misspelled_output():
    return '''go bulid: unknown command
Run 'go help' for usage.'''

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/man.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/man.py]
def match(command):
    return True
```
