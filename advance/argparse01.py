
#!  revise it (must be)

import argparse

parser = argparse.ArgumentParser(description = "A simple calculator", epilog="Enjoy your calculations!")
parser.add_argument("num1",type = int, help = "first number")
parser.add_argument("num2",type = int, help = "second number")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help = "operation to perform")

args = parser.parse_args()

# print(args.operation)

if args.operation == "add":
    print(f"{args.num1} + {args.num2} = {args.num1 + args.num2}")
elif args.operation == "sub":
    print(f"{args.num1} - {args.num2} = {args.num1 - args.num2}")       
elif args.operation == "mul":
    print(f"{args.num1} * {args.num2} = {args.num1 * args.num2}")
elif args.operation == "div":
    print(f"{args.num1} / {args.num2} = {args.num1 / args.num2:.2f}")
