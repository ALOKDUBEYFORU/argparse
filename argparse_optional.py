import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample program for optional argparse")
    parser.add_argument("--number1",help='First Number',type=int,default=10,metavar = '[0,12]')
    parser.add_argument("--number2",help='Second Number',type=int,default=15)
    parser.add_argument("--operation",help='Operation',choices=['add','modify'],default='add')
    args = parser.parse_args()
    args.number1 = int(args.number1)
    args.number2 = int(args.number2)
    result = None
    if args.operation == 'add':
        result = args.number1 + args.number2
    elif args.operation == 'multiply':
        result = args.number1 * args.number2
    else:
        print('Invalid operation')
    print(f'First Number :{args.number1}')
    print(f'Second Number {args.number2}')
    print(f'Operation {args.operation}')
    print(f'Result {result}')
