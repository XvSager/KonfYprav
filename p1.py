#!/usr/bin/env python3

import sys

def parse_command(user_input: str):
    parts = user_input.strip().split()
    if not parts:
        return None, []
    command = parts[0]
    args = parts[1:]
    return command, args

def stub_ls(args):
    print(f"ls called with args: {args}")

def stub_cd(args):
    print(f"cd called with args: {args}")

def main():
    print("VFS shell emulator (Stage 1). Type 'exit' to quit.")
    while True:
        try:
            user_input = input("VFS> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input:
            continue

        command, args = parse_command(user_input)

        if command is None:
            continue

        if command == "exit":
            print("Exiting VFS shell.")
            break
        elif command == "ls":
            stub_ls(args)
        elif command == "cd":
            stub_cd(args)
        else:
            print(f"VFS: command not found: {command}")

if __name__ == "__main__":
    main()