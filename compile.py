#! /usr/bin/python3

import subprocess
import sys
import traceback


OPENING_BRACKETS = ['(', '[', '{']
CLOSING_BRACKETS = [')', ']', '}']


def ask(question, yes=['yes', 'y'], no=['no', 'n']):
    print(question)
    answer = input("({}/{})> ".format(yes[0], no[0]))

    if answer in yes:
        return True

    elif answer in no:
        return False

    else:
        return None


def ask_loop(question, yes=None, no=None):
    kwargs = {}
    if yes is not None:
        kwargs['yes'] = yes
    if no is not None:
        kwargs['no'] = no

    answer = None
    while answer is None:
        answer = ask(question, **kwargs)

    return answer


class LatexParseError(Exception):
    def __init__(self, message, *, line=None, column=None):
        if line is not None and column is None:
            message += " at line {}".format(line)
        elif line is not None and column is not None:
            message += " at ({}, {})".format(line, column)

        super(message)


def does_close(opening, character):
    return character == CLOSING_BRACKETS[OPENING_BRACKETS.index(opening)]


def parse_brackets(text, *, strict=True):
    line = 0
    column = 0
    stack = []

    for c in text:
        if c == '\n':
            line += 1
            column = 0
        else:
            column += 1

        if c in OPENING_BRACKETS:
            stack.append(c)

        elif c in CLOSING_BRACKETS:
            if stack and does_close(stack[-1], c):
                stack.pop()
            else:
                message = "Found a closing '{}' without an opening '{}'"
                message.format(c, OPENING_BRACKETS[CLOSING_BRACKETS.index(c)])
                if strict:
                    LatexParseError(message, line=line, column=column)
                else:
                    print(message + " at ({}, {})".format(line, column))


def parse(path, *, strict=True):
    with open(path, 'r') as text:
        try:
            parse_brackets(text, strict=strict)
        except LatexParseError as error:
            traceback.print_exc(error)
            if not ask_loop("Continue anyway?"):
                sys.exit(-1)


def compile_to_pdf(path, flags=None):
    if flags is None:
        flags = []

    subprocess.call(["pdflatex"] + flags + [path])


def main(path, flags=None):
    parse(path)
    compile_to_pdf(path, flags=flags)


if __name__ == '__main__':
    main(sys.argv[1], flags=['-shell-escape'])
