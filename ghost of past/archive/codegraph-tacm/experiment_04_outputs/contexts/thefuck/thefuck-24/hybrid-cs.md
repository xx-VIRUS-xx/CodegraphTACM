# thefuck-24 :: hybrid-cs

query: Make `CorrectedCommand` ignore priority when checking equality

## selected nodes

- rank=1 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand.__eq__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=2 layer=FUNCTION tokens=322 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py::select_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py
- rank=3 layer=FUNCTION tokens=181 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.get_corrected_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=4 layer=FUNCTION tokens=144 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::get_corrected_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py
- rank=5 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py::CommandSelector.value file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py
- rank=6 layer=FUNCTION tokens=157 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.__eq__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=7 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py::CommandSelector.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py
- rank=8 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::TestSelectCommand.commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=9 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand.__repr__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=10 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py::CorrectedCommand.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py
- rank=11 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_choco_install.py::not_test_match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_choco_install.py
- rank=12 layer=FUNCTION tokens=248 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::organize_commands file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py
- rank=13 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/systemctl.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/systemctl.py
- rank=14 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::TestSelectCommand.commands_with_side_effect file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py
- rank=15 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py::fix_command file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/entrypoints/fix_command.py
- rank=16 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py
- rank=17 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py::Rule.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py
- rank=18 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py
- rank=19 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/az_cli.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/az_cli.py
- rank=20 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py::Settings._priority_from_env file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py
- rank=21 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/tmux.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/tmux.py
- rank=22 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/go_unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/go_unknown_command.py
- rank=23 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=24 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py
- rank=25 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py
- rank=26 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py
- rank=27 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=28 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_file.py::_make_pattern file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_file.py
- rank=29 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sudo_command_from_user_path.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sudo_command_from_user_path.py
- rank=30 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.__repr__ file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py
- rank=31 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py
- rank=32 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py
- rank=33 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/man.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/man.py
- rank=34 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dry.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dry.py
- rank=35 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/apt_invalid_operation.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/apt_invalid_operation.py
- rank=36 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py
- rank=37 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py
- rank=38 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sed_unterminated_s.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sed_unterminated_s.py
- rank=39 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/omnienv_no_such_command.py::match file=/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/omnienv_no_such_command.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand.__eq__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
    def __eq__(self, other):
        """Ignores `priority` field."""
        if isinstance(other, CorrectedCommand):
            return (other.script, other.side_effect) == \
                   (self.script, self.side_effect)
        else:
            return False

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py::select_command [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py]
def select_command(corrected_commands):
    """Returns:

     - the first command when confirmation disabled;
     - None when ctrl+c pressed;
     - selected command.

    :type corrected_commands: Iterable[thefuck.types.CorrectedCommand]
    :rtype: thefuck.types.CorrectedCommand | None

    """
    try:
        selector = CommandSelector(corrected_commands)
    except NoRuleMatched:
        logs.failed('No fucks given' if get_alias() == 'fuck'
                    else 'Nothing found')
        return

    if not settings.require_confirmation:
        logs.show_corrected_command(selector.value)
        return selector.value

    logs.confirm_text(selector.value)

    for action in read_actions():
        if action == const.ACTION_SELECT:
            sys.stderr.write('\n')
            return selector.value
        elif action == const.ACTION_ABORT:
            logs.failed('\nAborted')
            return
        elif action == const.ACTION_PREVIOUS:
            selector.previous()
            logs.confirm_text(selector.value)
        elif action == const.ACTION_NEXT:
            selector.next()
            logs.confirm_text(selector.value)

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py::CommandSelector.value [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py]
    def value(self):
        """:rtype thefuck.types.CorrectedCommand"""
        return self._commands[self._index]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.__eq__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
    def __eq__(self, other):
        if isinstance(other, Rule):
            return ((self.name, self.match, self.get_new_command,
                     self.enabled_by_default, self.side_effect,
                     self.priority, self.requires_output)
                    == (other.name, other.match, other.get_new_command,
                        other.enabled_by_default, other.side_effect,
                        other.priority, other.requires_output))
        else:
            return False

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py::CommandSelector.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/ui.py]
    def __init__(self, commands):
        """:type commands: Iterable[thefuck.types.CorrectedCommand]"""
        self._commands_gen = commands
        try:
            self._commands = [next(self._commands_gen)]
        except StopIteration:
            raise NoRuleMatched
        self._realised = False
        self._index = 0

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::TestSelectCommand.commands [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py]
    def commands(self):
        return [CorrectedCommand('ls', None, 100),
                CorrectedCommand('cd', None, 100)]

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand.__repr__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
    def __repr__(self):
        return u'CorrectedCommand(script={}, side_effect={}, priority={})'.format(
            self.script, self.side_effect, self.priority)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py::CorrectedCommand.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py]
    def __init__(self, script='', side_effect=None, priority=DEFAULT_PRIORITY):
        super(CorrectedCommand, self).__init__(
            script, side_effect, priority)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_choco_install.py::not_test_match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/rules/test_choco_install.py]
def not_test_match(command):
    assert not match(command)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py::organize_commands [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/corrector.py]
def organize_commands(corrected_commands):
    """Yields sorted commands without duplicates.

    :type corrected_commands: Iterable[thefuck.types.CorrectedCommand]
    :rtype: Iterable[thefuck.types.CorrectedCommand]

    """
    try:
        first_command = next(corrected_commands)
        yield first_command
    except StopIteration:
        return

    without_duplicates = {
        command for command in sorted(
            corrected_commands, key=lambda command: command.priority)
        if command != first_command}

    sorted_commands = sorted(
        without_duplicates,
        key=lambda corrected_command: corrected_command.priority)

    logs.debug(u'Corrected commands: {}'.format(
        ', '.join(u'{}'.format(cmd) for cmd in [first_command] + sorted_commands)))

    for command in sorted_commands:
        yield command

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/systemctl.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/systemctl.py]
def match(command):
    # Catches "Unknown operation 'service'." when executing systemctl with
    # misordered arguments
    cmd = command.script_parts
    return (cmd and 'Unknown operation \'' in command.output and
            len(cmd) - cmd.index('systemctl') == 3)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py::TestSelectCommand.commands_with_side_effect [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_ui.py]
    def commands_with_side_effect(self):
        return [CorrectedCommand('ls', lambda *_: None, 100),
                CorrectedCommand('cd', lambda *_: None, 100)]

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

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/cargo_no_command.py]
def match(command):
    return ('no such subcommand' in command.output.lower()
            and 'Did you mean' in command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py::Rule.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/utils.py]
    def __init__(self, name='', match=lambda *_: True,
                 get_new_command=lambda *_: '',
                 enabled_by_default=True,
                 side_effect=None,
                 priority=DEFAULT_PRIORITY,
                 requires_output=True):
        super(Rule, self).__init__(name, match, get_new_command,
                                   enabled_by_default, side_effect,
                                   priority, requires_output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dnf_no_such_command.py]
def match(command):
    return 'no such command' in command.output.lower()

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/az_cli.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/az_cli.py]
def match(command):
    return "is not in the" in command.output and "command group" in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py::Settings._priority_from_env [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/conf.py]
    def _priority_from_env(self, val):
        """Gets priority pairs from env."""
        for part in val.split(':'):
            try:
                rule, priority = part.split('=')
                yield rule, int(priority)
            except ValueError:
                continue

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/tmux.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/tmux.py]
def match(command):
    return ('ambiguous command:' in command.output
            and 'could be:' in command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/go_unknown_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/go_unknown_command.py]
def match(command):
    return 'unknown command' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::CorrectedCommand.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
    def __init__(self, script, side_effect, priority):
        """Initializes instance with given fields.

        :type script: basestring
        :type side_effect: (Command, basestring) -> None
        :type priority: int

        """
        self.script = script
        self.side_effect = side_effect
        self.priority = priority

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/unknown_command.py]
def match(command):
    return (re.search(r"([^:]*): Unknown command.*", command.output) is not None
            and re.search(r"Did you mean ([^?]*)?", command.output) is not None)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/tests/test_utils.py]
    def match(command):
        return True

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yum_invalid_operation.py]
def match(command):
    return 'No such command: ' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
    def __init__(self, name, match, get_new_command,
                 enabled_by_default, side_effect,
                 priority, requires_output):
        """Initializes rule with given fields.

        :type name: basestring
        :type match: (Command) -> bool
        :type get_new_command: (Command) -> (basestring | [basestring])
        :type enabled_by_default: boolean
        :type side_effect: (Command, basestring) -> None
        :type priority: int
        :type requires_output: bool

        """
        self.name = name
        self.match = match
        self.get_new_command = get_new_command
        self.enabled_by_default = enabled_by_default
        self.side_effect = side_effect
        self.priority = priority
        self.requires_output = requires_output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_file.py::_make_pattern [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fix_file.py]
def _make_pattern(pattern):
    pattern = pattern.replace('{file}', '(?P<file>[^:\n]+)') \
                     .replace('{line}', '(?P<line>[0-9]+)') \
                     .replace('{col}', '(?P<col>[0-9]+)')
    return re.compile(pattern, re.MULTILINE)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sudo_command_from_user_path.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sudo_command_from_user_path.py]
def match(command):
    if 'command not found' in command.output:
        command_name = _get_command_name(command)
        return which(command_name)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py::Rule.__repr__ [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/types.py]
    def __repr__(self):
        return 'Rule(name={}, match={}, get_new_command={}, ' \
               'enabled_by_default={}, side_effect={}, ' \
               'priority={}, requires_output={})'.format(
                   self.name, self.match, self.get_new_command,
                   self.enabled_by_default, self.side_effect,
                   self.priority, self.requires_output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/yarn_alias.py]
def match(command):
    return 'Did you mean' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/fab_command_not_found.py]
def match(command):
    return 'Warning: Command(s) not found:' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/man.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/man.py]
def match(command):
    return True

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dry.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/dry.py]
def match(command):
    split_command = command.script_parts

    return (split_command
            and len(split_command) >= 2
            and split_command[0] == split_command[1])

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/apt_invalid_operation.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/apt_invalid_operation.py]
def match(command):
    return 'E: Invalid operation' in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/terraform_no_command.py]
def match(command):
    return re.search(MISTAKE, command.output) and re.search(FIX, command.output)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/git_diff_staged.py]
def match(command):
    return ('diff' in command.script and
            '--staged' not in command.script)

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sed_unterminated_s.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/sed_unterminated_s.py]
def match(command):
    return "unterminated `s' command" in command.output

# /Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/omnienv_no_such_command.py::match [/Users/xxvirusxx/PY/CodegraphTACM/thefuck/thefuck/rules/omnienv_no_such_command.py]
def match(command):
    return 'env: no such command ' in command.output
```
