#!/usr/bin/python

import argparse

import argparse


def and_gate(input1, input2):
    return_val = ""
    for i in range(0, len(input1)):
        if input1[i] == "1" and input2[i] == "1":
            return_val += "1"
        else:
            return_val += "0"

    print(return_val)


def nand_gate(input1, input2):
    val = ""
    for i in range(0, len(input1)):
        if input1[i] == "1" and input2[i] == "1":
            val += "0"
        else:
            val += "1"
    print(val)


def nor_gate(input1, input2):
    val = ""
    for i in range(0, len(input1)):
        if input1[i] == "1" or input2[i] == "1":
            val += "0"
        else:
            val += "1"

    print(val)


def not_gate(input):
    val = ""
    for i in range(0, len(input)):
        if input[i] == "0":
            val = "1"
        else:
            val = "0"
    print(val)


def or_gate(input1, input2):
    val = ""
    for i in range(0, len(input1)):
        if input1[i] == "1" or input2[i] == "1":
            val += "1"
        else:
            val += "0"
    print(val)


def xnor_gate(input1, input2):
    val = ""
    for i in range(0, len(input1)):
        if input1[i] == input2[i]:
            val += "1"
        else:
            val += "0"

    print(val)


def xor_gate(input1, input2):
    val = ""
    for i in range(0, len(input1)):
        if input1[i] == input2[i]:
            val += "0"
        else:
            val += "1"
    print(val)


class AndGateLogic(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            print("Use enter arguments like so: -and [x] [y]\n "
                  "where x = first binary number and y = second binary number")
        else:
            and_gate(values[0], values[1])


class NandGateLogic(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            print("Use enter arguments like so: -nand [x] [y]\n "
                  "where x = first binary number and y = second binary number")
        else:
            nand_gate(values[0], values[1])


class NorGateLogic(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            print("Use enter arguments like so: -nor [x] [y]\n "
                  "where x = first binary number and y = second binary number")
        else:
            nor_gate(values[0], values[1])


class NotGateLogic(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            print("Use enter arguments like so: -not [x]\n "
                  "where x = binary number")
        else:
            not_gate(values[0])


class OrGateLogic(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            print("Use enter arguments like so: -or [x] [y]\n "
                  "where x = first binary number and y = second binary number")
        else:
            or_gate(values[0], values[1])


class XnorGateLogic(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            print("Use enter arguments like so: -xnor [x] [y]\n "
                  "where x = first binary number and y = second binary number")
        else:
            xnor_gate(values[0], values[1])


class XorGateLogic(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            print("Use enter arguments like so: -xor [x] [y]\n "
                  "where x = first binary number and y = second binary number")
        else:
            xor_gate(values[0], values[1])


parser = argparse.ArgumentParser()
parser.add_argument('-and', nargs='*', help="And Gate", action=AndGateLogic)
parser.add_argument('-nand', nargs='*', help="Nand Gate", action=NandGateLogic)
parser.add_argument('-or', nargs='*', help="Or Gate", action=OrGateLogic)
parser.add_argument('-nor', nargs='*', help="Nor Gate", action=NorGateLogic)
parser.add_argument('-xnor', nargs='*', help="Xnor Gate", action=XnorGateLogic)
parser.add_argument('-not', nargs='*', help="Not Gate", action=NotGateLogic)
parser.add_argument('-xor', nargs='*', help="Xor Gate", action=OrGateLogic)

args, sub_args = parser.parse_known_args()
